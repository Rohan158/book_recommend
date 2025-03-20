import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv  # For loading environment variables

# Load environment variables from .env file
load_dotenv()

# Configure API keys securely
GEMINI_API_KEY='AIzaSyAtCAiERG1KhfmpqzZhRNzTMLEUHIpujxk'
GOOGLE_BOOKS_API_KEY='AIzaSyD1hdztRVBeqFl-sATACV8jlO3gPanFdzQ'

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def fetch_books(query):
    """Fetch books from Google Books API."""
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        books = []

        for item in data.get("items", []):
            book_info = item.get("volumeInfo", {})

            books.append({
                "title": book_info.get("title", "Unknown"),
                "author": ", ".join(book_info.get("authors", ["Unknown"])),
                "description": book_info.get("description", "No description available."),
                "image_url": book_info.get("imageLinks", {}).get("thumbnail", ""),
                "google_books_id": item.get("id", ""),
            })

        return books
    return []

def ai_recommend_books(genre):
    """Get AI-based book recommendations using Gemini API."""
    try:
        # Use a correct Gemini model version
        model = genai.GenerativeModel("gemini-1.0-pro")

        # Generate AI-based book recommendations
        response = model.generate_content(f"Suggest some books in the {genre} genre.")

        # Extract recommendations correctly
        if hasattr(response, "text"):
            recommendations = response.text.strip().split("\n")
            return recommendations
        else:
            return ["Error: Unexpected response format from Gemini API."]
    
    except Exception as e:
        return [f"Error generating recommendations: {str(e)}"]
