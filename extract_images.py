import re
import glob

files_to_check = [
    'europe-packages.html',
    'worldwide-packages.html',
    'india-packages.html',
    'destinations.html',
    'index.html'
]

results = {}

for file in files_to_check:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Use regex to find images within cards
            # We look for img tags with class containing "responsive-card-img" or similar
            # And then look for the nearest h3 text which is the package name.
            
            cards = re.findall(r'<div[^>]*class="[^"]*group[^"]*"[^>]*>.*?<img[^>]*src="([^"]+)"[^>]*>.*?<h3[^>]*>([^<]+)</h3>', content, re.DOTALL | re.IGNORECASE)
            
            if cards:
                results[file] = cards
                
    except Exception as e:
        print(f"Error reading {file}: {e}")

for file, cards in results.items():
    print(f"\n--- {file} ---")
    for img_src, title in cards:
        print(f"Title: {title.strip()}")
        print(f"Image: {img_src}")

