from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import fetch_books, ai_recommend_books

def search_books(request):
    """Search for books using Google Books API."""
    query = request.GET.get("q", "")
    if not query:
        return JsonResponse({"error": "Please provide a search query."}, status=400)
    
    books = fetch_books(query)
    return JsonResponse({"books": books})

def recommend_books(request, genre):
    """Get AI-based book recommendations using Gemini API."""
    if not genre:
        return JsonResponse({"error": "Genre is required for recommendations."}, status=400)

    recommendations = ai_recommend_books(genre)
    return JsonResponse({"recommended_books": recommendations})
