import gzip
import base64
import json
import sys
from pathlib import Path

def compile_theme(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            theme_data = json.load(f)

        theme_text = json.dumps(theme_data, separators=(',', ':'))
        compressed = gzip.compress(theme_text.encode('utf-8'))
        encoded = base64.b64encode(compressed).decode('utf-8')

        print(encoded)

    except Exception as e:
        print(f"Okurva error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python compiler.py <theme.json>")
    else:
        compile_theme(sys.argv[1])
    
    input("Press enter to exit...")
