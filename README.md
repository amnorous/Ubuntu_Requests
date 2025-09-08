# Ubuntu Image Fetcher 🖼️🌍

> *“I am because we are.” – Ubuntu Philosophy*  

The **Ubuntu Image Fetcher** is a mindful Python program that connects to the global web community, respectfully fetches images, and organizes them for later sharing.  

Inspired by the spirit of **Ubuntu** — community, respect, sharing, and practicality — this tool ensures safe, graceful, and purposeful image fetching.  

---

## ✨ Features
- 📥 Fetch images from one or more URLs  
- 🗂️ Saves all downloads into a dedicated folder: `Fetched_Images`  
- 🔒 Skips non-image files by checking HTTP headers  
- 🛡️ Prevents duplicate downloads  
- 🌐 Handles errors gracefully (timeouts, connection issues, invalid URLs)  
- 🙌 Embodies Ubuntu values in design and interaction  

---

## 🚀 Usage

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/Ubuntu_Requests.git
cd Ubuntu_Requests
2. Install dependencies

This project uses the requests
 library:

pip install requests

3. Run the program
python fetch_image.py

4. Example Output
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by spaces): https://example.com/ubuntu-wallpaper.jpg

✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
