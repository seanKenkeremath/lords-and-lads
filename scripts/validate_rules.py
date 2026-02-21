import re
import sys
import os

def validate_markdown(filename):
    root_dir = os.getcwd() 
    file_path = os.path.join(root_dir, filename)

    if not os.path.exists(file_path):
        print(f"❌ Error: {filename} not found at {file_path}")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Checks that all links are working
    headers = re.findall(r'^#+\s+(.*)$', content, re.MULTILINE)
    slugs = {re.sub(r'[^\w\- ]', '', h).lower().replace(' ', '-') for h in headers}
    links = re.findall(r'\[.*?\]\(#([^\)]+)\)', content)

    errors = [f"Broken link: '#{l}'" for l in links if l not in slugs]

    if errors:
        for err in errors: print(f"❌ {err}")
        sys.exit(1)
    print(f"🔨🔨 {filename} is valid")

if __name__ == "__main__":
    validate_markdown('README.md')
