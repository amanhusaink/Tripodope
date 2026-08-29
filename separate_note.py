import glob
import re

html_files = glob.glob('*.html')
count = 0

pattern = re.compile(r'<p class="text-xs md:text-sm text-gray-300 leading-relaxed font-medium mt-1">Every package is fully customizable based on the traveler’s comfort and convenience\.</p>\s*</div>\s*</div>', re.MULTILINE)

replacement = r'''</div>
</div>
<!-- Customizable Note Alert Box -->
<div class="mt-4 bg-[#11223A] rounded-xl p-5 md:p-6 flex flex-col md:flex-row gap-4 items-center shadow-md border border-[#11223A]/80 text-white group hover:shadow-lg transition-shadow duration-300 relative overflow-hidden">
<div class="absolute inset-0 bg-gradient-to-r from-[#C19A58]/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
<div class="w-10 h-10 rounded-full bg-[#C19A58]/20 flex items-center justify-center shrink-0 border border-[#C19A58]/30">
<svg class="w-5 h-5 text-[#C19A58]" fill="none" stroke="currentColor" viewbox="0 0 24 24"><path d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
</div>
<div class="relative z-10 text-center md:text-left">
<p class="text-sm md:text-base font-bold text-white mb-1 tracking-wide uppercase text-[#C19A58]">Note</p>
<p class="text-xs md:text-sm text-gray-300 leading-relaxed font-medium">
  Every package is fully customizable based on the traveler’s comfort and convenience.
</p>
</div>
</div>'''

for filepath in html_files:
    if filepath == 'template.html': continue
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    if pattern.search(html):
        new_html = pattern.sub(replacement, html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f'Separated note in {filepath}')
        count += 1

print(f'Total files modified: {count}')
