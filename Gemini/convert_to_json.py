import csv
import json
import os

input_file = 'Web/tmdb_top_5000.csv'
cast_file = 'Web/tmdb_cast.csv'
output_file = 'Web/movie_data.js'

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    exit(1)

# Load cast images
cast_images = {}
if os.path.exists(cast_file):
    with open(cast_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cast_images[row['name']] = row['image_url']

movies = []
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Process cast names into objects with images
        cast_names = [c.strip() for c in row['cast'].split(',')] if row['cast'] else []
        rich_cast = []
        for name in cast_names:
            rich_cast.append({
                'name': name,
                'image_url': cast_images.get(name, '') # Empty if not found
            })

        movies.append({
            'id': row['id'],
            'title': row['title'],
            'poster_url': row['poster_url'],
            'year': row['release_date'][:4] if row['release_date'] else '',
            'rating': row['vote_average'],
            'popularity': float(row['popularity']) if row['popularity'] else 0,
            'genres': row['genres'],
            'overview': row['overview'],
            'runtime': row['runtime'],
            'cast': rich_cast, # Now a list of objects
            'director': row['director']
        })

# Sort by popularity
movies.sort(key=lambda x: x['popularity'], reverse=True)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("const allMovieData = ")
    json.dump(movies, f, indent=2)
    f.write(";")

print(f"Converted {len(movies)} movies with rich cast data to movie_data.js.")
