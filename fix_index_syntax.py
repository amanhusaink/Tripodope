import re

index_file = "c:/Users/aman/Desktop/Tripodope/index.html"

with open(index_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove the modal HTML
start_html = content.find('<!-- UNIFIED SERVICE INQUIRY MODAL -->')
end_html = content.find('<!-- WhatsApp Floating Button -->')

if start_html != -1 and end_html != -1:
    content = content[:start_html] + content[end_html:]

# 2. Remove the modal scripts
start_script = content.find('<!-- Service Inquiry Modal Scripts -->')
end_script = content.find('</body>')

if start_script != -1 and end_script != -1:
    content = content[:start_script] + content[end_script:]

with open(index_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed")
