import urllib.request
import re
import random

def get_image(query):
    url = f'https://unsplash.com/s/photos/{query}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # match photo IDs
        ids = re.findall(r'"id":"([a-zA-Z0-9_-]{11})"', html)
        if not ids:
            ids = re.findall(r'photo-([a-zA-Z0-9_-]{11})', html)
        ids = list(set(ids))
        if ids:
            return random.choice(ids[:10])
        return 'Not found'
    except Exception as e:
        return str(e)

print('Italy Coastal:', get_image('amalfi-coast'))
print('Swiss Alpine:', get_image('swiss-alps-train'))
print('Italy Train:', get_image('rome-colosseum'))
print('Europe Voyage:', get_image('europe-landmarks'))
