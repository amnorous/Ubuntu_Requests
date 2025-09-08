import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url, content):
    """
    Extracts a filename from the URL.
    If none is present, generates one based on the file hash.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename:
        # Use a hash of the content to generate a unique filename
        file_hash = hashlib.md5(content).hexdigest()
        filename = f"image_{file_hash}.jpg"
    
    return filename

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Accept multiple URLs separated by spaces
    urls = input("Please enter one or more image URLs (separated by spaces): ").split()
    
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        try:
            # Fetch the image
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Check Content-Type header before saving
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipping {url} (not an image, Content-Type: {content_type})")
                continue

            # Get content in bytes
            content = response.content

            # Generate filename
            filename = get_filename_from_url(url, content)
            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicate downloads
            if os.path.exists(filepath):
                print(f"✗ Skipping {filename} (already exists).")
                continue

            # Save the image
            with open(filepath, 'wb') as f:
                f.write(content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
