import requests
from datetime import datetime, timedelta
import gzip
import json
import csv
import os

def download_id_export():
    # Try today, then yesterday, then the day before
    for i in range(3):
        date_str = (datetime.now() - timedelta(days=i)).strftime("%m_%d_%Y")
        url = f"http://files.tmdb.org/p/exports/movie_ids_{date_str}.json.gz"
        print(f"Checking {url}...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open("movie_ids.json.gz", "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            print(f"Successfully downloaded: {url}")
            return True
    print("Could not find any recent ID export files.")
    return False

def convert_to_csv():
    if not os.path.exists("movie_ids.json.gz"):
        return
    
    print("Converting ID export to CSV...")
    with gzip.open("movie_ids.json.gz", "rt", encoding="utf-8") as f_in:
        with open("tmdb_all_ids.csv", "w", newline="", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            writer.writerow(["id", "title", "popularity", "adult"])
            
            count = 0
            for line in f_in:
                data = json.loads(line)
                writer.writerow([
                    data.get("id"),
                    data.get("original_title"),
                    data.get("popularity"),
                    data.get("adult")
                ])
                count += 1
                if count % 100000 == 0:
                    print(f"Processed {count} IDs...")
    
    print(f"Finished! Total {count} IDs saved to tmdb_all_ids.csv")

if __name__ == "__main__":
    if download_id_export():
        convert_to_csv()
