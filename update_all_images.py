import os
import glob
from bs4 import BeautifulSoup
import re

UNSPLASH_IMAGES = {
    'paris': ['1499856871958-5b9627545d1a', '1502602898657-3e91760cbb34', '1511739001486-6bfe10ce785f', '1522093007474-d86e9bf7ba6f'],
    'rome': ['1552832232-0b621470ea24', '1531572753322-ad063cecc140', '1542820224-b49f9976bb2b', '1529260830199-0264ef58f1a1'],
    'swiss': ['1530122037265-a5f1f91d3b99', '1527668752968-14dc70a27c95', '1506929562872-bb421503ef21', '1515488764276-beab7607c1e6'],
    'switzerland': ['1530122037265-a5f1f91d3b99', '1527668752968-14dc70a27c95', '1506929562872-bb421503ef21', '1515488764276-beab7607c1e6'],
    'london': ['1513635269975-59663e0ac1ad', '1520939817895-50bb402456e7', '1529655683823-dc00ed8413b8', '1486299267170-8ee6811bc339'],
    'amsterdam': ['1534351590666-13e3eeb6ba09', '1512470876407-11f81010373c', '1524047934617-1065759bc655', '1517056691345-86f1e63ff3bc'],
    'venice': ['1514890547357-a9ee288728e0', '1523906834658-6e24ef2386f9', '1516480579899-566b6c221a71', '1552693822-0d17daec7f1b'],
    'florence': ['1541359927273-d068c7baaec5', '1543360408422-0a77fae51920', '1582236310243-718a38ecbe5e'],
    'barcelona': ['1583422409516-a5d541f04182', '1539037116271-8b010c2c0192', '1562883676864-45e8f4989025'],
    'madrid': ['1539037116271-8b010c2c0192', '1513813959-19fc13c329fb', '1556956214-49cce54f3b79'],
    'lisbon': ['1580500454378-43d939e6a0fb', '1548695026-6208a0d2f099', '1551061907-7d9fc830f368'],
    'porto': ['1590924970425-4702b8d00d23', '1564819777-6a4a0658ebc5', '1549491632-4d2be7ce0e4b'],
    'dubai': ['1512453979798-5ea266f8880c', '1528702748617-c64d49e9cb08', '1546412414-e1885259563a', '1582672060674-cb276269eb8b', '1512632571407-124b896b0143'],
    'ljubljana': ['1525596662741-e94ff9f26de1', '1585507328905-23c28b73f8a0', '1591410141973-206eeb41a547'],
    'slovenia': ['1525596662741-e94ff9f26de1', '1585507328905-23c28b73f8a0', '1591410141973-206eeb41a547'],
    'croatia': ['1555986877-6f68ccebb258', '1552033662-793540d58852', '1533159938-1ee4b77f1585'],
    'dubrovnik': ['1555986877-6f68ccebb258', '1552033662-793540d58852', '1533159938-1ee4b77f1585'],
    'montenegro': ['1563216393-271578e916a0', '1590240989357-1ff12e2d9ff6', '1598462057774-cbb6dafa1519'],
    'bosnia': ['1581454641951-689e46a78dc1', '1569470914614-7264a7536d1b', '1581454641951-689e46a78dc1'],
    'sarajevo': ['1581454641951-689e46a78dc1', '1569470914614-7264a7536d1b', '1581454641951-689e46a78dc1'],
    'milan': ['1520440229-c876f1cb2792', '1556093845-a7b539c3dc32', '1576402748232-a1f9e5a1b0cd'],
    'prague': ['1519677100203-a0e87281eb20', '1541852074559-0010996c9e0d', '1516087799140-5441d6b052bc'],
    'budapest': ['1511119561937-2fb0739f8263', '1536643243-7036666ba809', '1540306132578-83b63297593c'],
    'georgia': ['1618141444458-7182283e33bf', '1549449852-19e0b8d5a62e', '1596700773822-7f28abecaf64', '1599818816823-1d07ed24817d'],
    'tbilisi': ['1618141444458-7182283e33bf', '1549449852-19e0b8d5a62e', '1596700773822-7f28abecaf64', '1599818816823-1d07ed24817d'],
    'azerbaijan': ['1590412803328-7f28abecaf64', '1587595431973-160d0d94add1', '1590412803328-7f28abecaf64'],
    'baku': ['1590412803328-7f28abecaf64', '1587595431973-160d0d94add1', '1590412803328-7f28abecaf64'],
    'bali': ['1537996137310-85fb9a76af39', '1518548419970-5871b55928d1', '1515238152791-381a153787a4'],
    'indonesia': ['1537996137310-85fb9a76af39', '1518548419970-5871b55928d1', '1515238152791-381a153787a4'],
    'singapore': ['1525625293386-3f8f99389fda', '1505504787994-db7320c2a8ea', '1546738914-1f7c22dbbc2a'],
    'malaysia': ['1596422846543-75c6fc197f04', '1604586431932-3532c2865243', '1583416405796-0cb79743c7b3'],
    'kuala lumpur': ['1596422846543-75c6fc197f04', '1604586431932-3532c2865243', '1583416405796-0cb79743c7b3'],
    'india': ['1524492412937-b28b45410491', '1532087599026-b51c89078fcd', '1595815771614-ade9d652a65d', '1522254338981-d70cb9e46a9a'],
    'arrival': ['1436491865332-7a61a109cc05', '1476483582103-6252e690f058', '1488085061387-422e176c12d4', '1544015699-23c21c7e997a'],
    'departure': ['1436491865332-7a61a109cc05', '1476483582103-6252e690f058', '1488085061387-422e176c12d4', '1544015699-23c21c7e997a'],
    'airport': ['1436491865332-7a61a109cc05', '1476483582103-6252e690f058', '1488085061387-422e176c12d4', '1544015699-23c21c7e997a'],
    'default': ['1476514525535-07fb3b4ae5f1', '1469854523086-cc02fe5d8800', '1499678329028-101435549a4e', '1454388683759-c873b57def2c', '1475924156734-49c17f96cafa']
}

current_index = {k: 0 for k in UNSPLASH_IMAGES.keys()}

def get_best_image(text):
    text = text.lower()
    key = None
    
    # Check for arrival/departure first if it's explicitly Cochin to avoid using Kerala scenery for flights
    if "cochin" in text and ("arrival" in text or "departure" in text or "flight" in text):
        key = 'airport' if 'airport' in UNSPLASH_IMAGES else 'arrival'
    else:
        for k in UNSPLASH_IMAGES.keys():
            if k in text and k not in ['arrival', 'departure', 'cochin', 'default', 'airport']:
                key = k
                break
        
        # Fallback checks for generics
        if not key:
            if 'arrive' in text or 'arrival' in text or 'departure' in text or 'flight' in text or 'cochin' in text:
                key = 'arrival'
            else:
                key = 'default'
                
    images = UNSPLASH_IMAGES[key]
    idx = current_index[key]
    current_index[key] = (idx + 1) % len(images)
    
    return f"https://images.unsplash.com/photo-{images[idx]}?auto=format&fit=crop&w=800&q=80"

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath == 'template.html': continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    modified = False
    
    # 1. Update Itinerary Accordion Images
    accordion_items = soup.select('.accordion-item')
    for item in accordion_items:
        title_span = item.select_one('.accordion-title')
        body_img = item.select_one('.accordion-body img')
        
        if title_span and body_img:
            title_text = title_span.get_text().strip()
            new_src = get_best_image(title_text)
            
            if body_img['src'] != new_src:
                body_img['src'] = new_src
                modified = True
                print(f"[{filepath}] Itinerary Day '{title_text[:20]}...' -> updated image".encode('utf-8', 'ignore').decode('utf-8'))
                
    # 2. Update Package Card Images (Main pages)
    titles = soup.select('h3')
    for title in titles:
        # Check if it's a package title (usually in a card)
        # Look for the closest relative container that has an img
        parent = title.find_parent('div', class_=re.compile(r'rounded-[23]xl'))
        if parent:
            img = parent.select_one('img')
            # Exclude flag badges (flagcdn.com)
            if img and 'flagcdn' not in img.get('src', ''):
                title_text = title.get_text().strip()
                # Exclude if it's not a package card (e.g. "Featured Packages")
                if len(title_text) > 3:
                    new_src = get_best_image(title_text)
                    if img['src'] != new_src:
                        img['src'] = new_src
                        modified = True
                        print(f"[{filepath}] Package Card '{title_text[:20]}...' -> updated image".encode('utf-8', 'ignore').decode('utf-8'))
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))

print("Done updating all images.")
