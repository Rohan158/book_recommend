import requests
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key='AIzaSyAtCAiERG1KhfmpqzZhRNzTMLEUHIpujxk')

def fetch_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key=AIzaSyD1hdztRVBeqFl-sATACV8jlO3gPanFdzQ"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        books = []
        for item in data.get("items", []):
            book_info = item.get("volumeInfo", {})
            books.append({
                "title": book_info.get("title", "Unknown"),
                "author": ", ".join(book_info.get("authors", ["Unknown"])),
                "description": book_info.get("description", ""),
                "image_url": book_info["imageLinks"]["thumbnail"] if "imageLinks" in book_info else "",
                "google_books_id": item.get("id", ""),
            })
        return books
    return []

def ai_recommend_books(user_genre):
    prompt = f"Recommend top 5 books based on the genre: {user_genre}"
    
    try:
        response = genai.generate_text(prompt)
        return response.text.split("\n")
    except Exception as e:
        return [f"Error generating recommendations: {str(e)}"]