import requests
import csv
import time
import os

# Configuration
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhODRhNmVjNzEyNDFjMjIxMzQ5YTA4NDc4NmE3OTFmZCIsIm5iZiI6MTc4MDMxOTY0My41ODIsInN1YiI6IjZhMWQ4NTliZWE1ODI3MjM0M2NhYjVkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vXdOmi47yVVcCoRFfLqTQ7Z594BCWqe259GdoMFU00s"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"
TOTAL_MOVIES_TO_FETCH = 5000
OUTPUT_FILE = "tmdb_top_5000.csv"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json;charset=utf-8"
}

def fetch_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?append_to_response=credits"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print("Rate limit hit, sleeping...")
        time.sleep(10)
        return fetch_movie_details(movie_id)
    return None

def main():
    movies_data = []
    movies_fetched = 0
    page = 1
    
    # CSV Headers
    fieldnames = [
        'id', 'title', 'release_date', 'vote_average', 'vote_count', 
        'popularity', 'runtime', 'budget', 'revenue', 'genres', 
        'overview', 'poster_url', 'backdrop_url', 'cast', 'director'
    ]
    
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        while movies_fetched < TOTAL_MOVIES_TO_FETCH:
            print(f"Fetching page {page} of popular movies...")
            list_url = f"{BASE_URL}/movie/popular?page={page}"
            list_response = requests.get(list_url, headers=headers)
            
            if list_response.status_code != 200:
                print(f"Error fetching page {page}: {list_response.status_code}")
                break
                
            results = list_response.json().get('results', [])
            if not results:
                break
                
            for movie_summary in results:
                if movies_fetched >= TOTAL_MOVIES_TO_FETCH:
                    break
                    
                movie_id = movie_summary['id']
                details = fetch_movie_details(movie_id)
                
                if details:
                    # Process cast (Top 5)
                    cast = ", ".join([member['name'] for member in details.get('credits', {}).get('cast', [])[:5]])
                    
                    # Process director
                    director = ""
                    for crew_member in details.get('credits', {}).get('crew', []):
                        if crew_member['job'] == 'Director':
                            director = crew_member['name']
                            break
                    
                    # Process genres
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
                    movies_fetched += 1
                    
                    if movies_fetched % 10 == 0:
                        print(f"Progress: {movies_fetched}/{TOTAL_MOVIES_TO_FETCH} movies fetched.")
                
                # Small sleep to respect rate limits (40 req / 10s)
                time.sleep(0.2)
            
            page += 1

    print(f"Finished! Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
