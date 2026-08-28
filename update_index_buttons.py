import re

index_file = "c:/Users/aman/Desktop/Tripodope/index.html"

with open(index_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. We need to find each card that has a button with onclick="openServiceModal('KEY')"
# A card starts with <div class="snap-start and ends with the closing div of the card.
# This is a bit tricky with regex, so let's do it with a more targeted approach.
# We will match the button and extract the KEY.
# Then we will replace the button with nothing (or empty string).
# We also need to add onclick and cursor-pointer to the parent card div.
# Instead of parsing HTML, we can do string manipulation.

keys = re.findall(r"onclick=\"openServiceModal\('([^']+)'\)\"", content)

for key in set(keys):
    # Find the button for this key
    button_regex = r'<button[^>]*onclick="openServiceModal\(\'' + re.escape(key) + r'\'\)"[^>]*>.*?</button>'
    content = re.sub(button_regex, '', content, flags=re.DOTALL)

# Now we need to add onclick="window.location.href='services.html?service=KEY'" to the cards.
# Since we removed the button, we need another way to map the card to the key.
# Actually, it's easier to find the card, extract the key from the button, modify the card div, and remove the button in one go.

with open(index_file, "r", encoding="utf-8") as f:
    original_content = f.read()
    
# Let's write a function to replace each card manually.
def process_cards(text):
    # A card starts with: <div class="snap-start shrink-0 ...">
    # and ends after the button's closing div or something. 
    # Actually, let's just find the buttons, and then backtrack to the nearest <div class="snap-start
    out_text = text
    matches = list(re.finditer(r'<button[^>]*onclick="openServiceModal\(\'([^\']+)\'\)"[^>]*>.*?</button>', out_text, re.DOTALL))
    
    # We must replace from the end to not mess up indices
    for match in reversed(matches):
        key = match.group(1)
        btn_start = match.start()
        btn_end = match.end()
        
        # Find the preceding <div class="snap-start
        card_start = out_text.rfind('<div class="snap-start', 0, btn_start)
        
        if card_start != -1:
            # We insert onclick and cursor-pointer to this div.
            # The div opening tag ends at the first '>'
            tag_end = out_text.find('>', card_start)
            div_tag = out_text[card_start:tag_end+1]
            
            # Add cursor-pointer to class
            if 'class="' in div_tag:
                div_tag = div_tag.replace('class="', 'class="cursor-pointer ', 1)
            
            # Add onclick
            div_tag = div_tag[:-1] + f' onclick="window.location.href=\'services.html?service={key}\'">'
            
            # Reconstruct the text:
            # from 0 to card_start
            # + modified div_tag
            # + from tag_end+1 to btn_start (this is the content before the button)
            # + from btn_end to end (skipping the button)
            out_text = out_text[:card_start] + div_tag + out_text[tag_end+1:btn_start] + out_text[btn_end:]
            
    return out_text

content = process_cards(original_content)

# 3. Remove the modal overlay and its content
# The modal has id="serviceModal"
# Let's find <!-- Services Modal (Hidden by default) --> and its ending.
# It ends right before <!-- Floating Action Buttons (FAB) --> or similar.
modal_start = content.find('<!-- Services Modal (Hidden by default) -->')
if modal_start != -1:
    modal_end = content.find('<!-- Floating Action Buttons (FAB) -->', modal_start)
    if modal_end != -1:
        content = content[:modal_start] + content[modal_end:]
    else:
        # Fallback if FAB comment is not exactly that
        # Look for the ending div of the modal. This is harder.
        pass

# 4. Remove the openServiceModal script logic
# Look for function openServiceModal
script_start = content.find('function openServiceModal(serviceKey)')
if script_start != -1:
    # Find the end of this script block, maybe the closing </script>
    script_end = content.find('</script>', script_start)
    # Actually, we should just remove the functions: openServiceModal, closeServiceModal
    # and maybe some event listeners. 
    # The simplest is to replace the whole block if we know where it starts and ends.
    # It's inside the existing <script> tags at the bottom.
    pass

# To be safe and precise with script removal:
content = re.sub(r'function openServiceModal.*?\}\n', '', content, flags=re.DOTALL)
content = re.sub(r'function closeServiceModal.*?\}\n', '', content, flags=re.DOTALL)
content = re.sub(r'document\.getElementById\(\'serviceModal\'\)\.addEventListener\(\'click\'.*?\}\);\n', '', content, flags=re.DOTALL)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(content)
print("Done")
