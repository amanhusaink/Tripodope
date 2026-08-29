import urllib.request
import re

destinations = [
    "Florence, Italy", "Swiss Alps", "Rome, Italy", "Europe Landmark", "European Church",
    "Bernina Express", "Spain", "Europe Architecture", "Dubai",
    "Vatican City", "Zurich", "Paris", "Monte Carlo", "Berlin", "Vienna",
    "Amsterdam", "Barcelona", "Dubrovnik"
]

results = {}

for dest in destinations:
    try:
        url = f"https://unsplash.com/s/photos/{dest.replace(' ', '-')}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Find the first image ID
        # Unsplash images usually have links like /photos/something-ID
        # Or image srcs like images.unsplash.com/photo-ID
        match = re.search(r'images\.unsplash\.com/photo-([a-zA-Z0-9\-]+)\?', html)
        if match:
            results[dest] = match.group(1)
        else:
            results[dest] = "NOT FOUND"
    except Exception as e:
        results[dest] = f"ERROR: {e}"

for dest, photo_id in results.items():
    print(f"{dest}: {photo_id}")
