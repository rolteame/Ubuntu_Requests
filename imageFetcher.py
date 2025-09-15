import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    urls_input = input("👉 Enter image URLs (separated by commas): ")

    urls = urls_input.split(",")

    if (not url.startswith("http://") and not url.startswith("https://")):
        print("✗ Invalid URL. Please ensure it starts with http:// or https://")
        return
    
    downloaded_files = set()
    
    for link in urls:
        url = link.strip()
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                print(f"✗ Could not determine filename from URL: {url}")
                continue
            
            # Avoid overwriting files
            if filename in downloaded_files:
                print(f"✗ File '{filename}' already downloaded. Skipping to avoid overwrite.")
                continue
            
            with open(filename, 'wb') as file:
                file.write(response.content)
                downloaded_files.add(filename)
                print(f"✓ Successfully downloaded: {filename}")
        
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to download {url}. Error: {e}")

if __name__ == "__main__":
    main()