import glob
import re

html_files = glob.glob('*.html')
count = 0

pattern = re.compile(r'(<p[^>]*>\s*All final inclusions are tailored specifically to your customized itinerary and agreed package tier\.\s*</p>)', re.IGNORECASE)

# We use raw string with single quotes, and double quotes inside.
replacement = r'\1\n<p class="text-xs md:text-sm text-gray-300 leading-relaxed font-medium mt-1">Every package is fully customizable based on the traveler’s comfort and convenience.</p>'

for filepath in html_files:
    if filepath == 'template.html': continue
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    if pattern.search(html):
        new_html = pattern.sub(replacement, html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f'Added note to {filepath}')
        count += 1

print(f'Total files modified: {count}')
