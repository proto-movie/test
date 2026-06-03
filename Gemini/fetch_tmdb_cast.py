import requests
import csv
import time
import os

# Configuration
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhODRhNmVjNzEyNDFjMjIxMzQ5YTA4NDc4NmE3OTFmZCIsIm5iZiI6MTc4MDMxOTY0My41ODIsInN1YiI6IjZhMWQ4NTliZWE1ODI3MjM0M2NhYjVkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vXdOmi47yVVcCoRFfLqTQ7Z594BCWqe259GdoMFU00s"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"
INPUT_FILE = "Web/tmdb_top_5000.csv"
OUTPUT_FILE = "Web/tmdb_cast.csv"
MOVIES_TO_PROCESS = 500  # Limiting to top 500 for speed

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

def fetch_credits(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            time.sleep(5)
            return fetch_credits(movie_id)
    except Exception as e:
        print(f"Error fetching credits for {movie_id}: {e}")
    return None

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    movie_ids = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= MOVIES_TO_PROCESS:
                break
            movie_ids.append(row['id'])

    unique_cast = {} # name -> image_url

    print(f"Processing {len(movie_ids)} movies to extract cast...")
    
    for i, movie_id in enumerate(movie_ids):
        credits = fetch_credits(movie_id)
        if credits:
            for member in credits.get('cast', [])[:10]: # Top 10 per movie
                name = member.get('name')
                profile_path = member.get('profile_path')
                if name and profile_path and name not in unique_cast:
                    unique_cast[name] = f"{IMAGE_BASE_URL}{profile_path}"
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{len(movie_ids)} movies. Found {len(unique_cast)} unique actors so far.")
        
        time.sleep(0.1) # Respect rate limits

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'image_url'])
        for name, url in unique_cast.items():
            writer.writerow([name, url])

    print(f"Finished! Saved {len(unique_cast)} unique actors to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
