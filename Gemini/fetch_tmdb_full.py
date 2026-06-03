import requests
import csv
import time
import json
import os

# Configuration
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhODRhNmVjNzEyNDFjMjIxMzQ5YTA4NDc4NmE3OTFmZCIsIm5iZiI6MTc4MDMxOTY0My41ODIsInN1YiI6IjZhMWQ4NTliZWE1ODI3MjM0M2NhYjVkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vXdOmi47yVVcCoRFfLqTQ7Z594BCWqe259GdoMFU00s"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"
ID_LIST_FILE = "tmdb_all_ids.csv"
OUTPUT_FILE = "tmdb_full_metadata.csv"
PROGRESS_FILE = "metadata_progress.json"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {"last_processed_index": -1, "completed_ids": []}

def save_progress(index):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump({"last_processed_index": index}, f)

def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?append_to_response=credits"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 10))
            print(f"Rate limit hit. Sleeping for {retry_after}s...")
            time.sleep(retry_after)
            return fetch_movie_details(movie_id)
        elif response.status_code == 404:
            return "NOT_FOUND"
    except Exception as e:
        print(f"Error fetching {movie_id}: {e}")
        time.sleep(2)
        return fetch_movie_details(movie_id)
    return None

def main():
    progress = load_progress()
    start_index = progress["last_processed_index"] + 1
    
    # Fieldnames same as the popular script
    fieldnames = [
        'id', 'title', 'release_date', 'vote_average', 'vote_count', 
        'popularity', 'runtime', 'budget', 'revenue', 'genres', 
        'overview', 'poster_url', 'backdrop_url', 'cast', 'director'
    ]
    
    # Read all IDs from the previously created list
    ids_to_process = []
    with open(ID_LIST_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ids_to_process.append(row['id'])
    
    total_ids = len(ids_to_process)
    print(f"Total IDs to process: {total_ids}. Starting from index {start_index}.")

    # Open file in append mode if it exists, otherwise write headers
    file_exists = os.path.isfile(OUTPUT_FILE)
    
    with open(OUTPUT_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
            
        for i in range(start_index, total_ids):
            movie_id = ids_to_process[i]
            details = fetch_movie_details(movie_id)
            
            if details and details != "NOT_FOUND":
                cast = ", ".join([m['name'] for m in details.get('credits', {}).get('cast', [])[:5]])
                director = ""
                for crew_member in details.get('credits', {}).get('crew', []):
                    if crew_member['job'] == 'Director':
                        director = crew_member['name']
                        break
                
                genres = ", ".join([g['name'] for g in details.get('genres', [])])
                
                row = {
                    'id': details.get('id'),
                    'title': details.get('title'),
                    'release_date': details.get('release_date'),
                    'vote_average': details.get('vote_average'),
                    'vote_count': details.get('vote_count'),
                    'popularity': details.get('popularity'),
                    'runtime': details.get('runtime'),
                    'budget': details.get('budget'),
                    'revenue': details.get('revenue'),
                    'genres': genres,
                    'overview': details.get('overview'),
                    'poster_url': f"{IMAGE_BASE_URL}{details.get('poster_path')}" if details.get('poster_path') else "",
                    'backdrop_url': f"{IMAGE_BASE_URL}{details.get('backdrop_path')}" if details.get('backdrop_path') else "",
                    'cast': cast,
                    'director': director
                }
                writer.writerow(row)
            
            # Save progress every 100 movies
            if i % 100 == 0:
                save_progress(i)
                print(f"Progress: {i}/{total_ids} ({round((i/total_ids)*100, 2)}%)")
            
            # Rate limit buffer
            time.sleep(0.2)

    print("Extraction complete!")

if __name__ == "__main__":
    main()
