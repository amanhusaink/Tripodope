import re

def get_hero_image(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        # Find first unsplash image
        match = re.search(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9_\-]+[^\'\"\s]+', html)
        return match.group(0) if match else None
    except:
        return None

print('Grand Italian:', get_hero_image('grand-italian-11-days.html'))
print('Swiss Alpine:', get_hero_image('swiss-italian-9-days.html'))
print('Italian Express:', get_hero_image('italy-5-days.html'))
print('Euro Voyage:', get_hero_image('europe-10-days.html'))
