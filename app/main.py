import requests
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# not worried about security for this project so just opening it up
origins = ["*"]

# Existing code
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/api/v1")


@router.get("/books/search/")
def search_books(query: str, offset: int = 0):
    google_books_api_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": 10,
        "key": "AIzaSyDc6YzxM9ff1768dbOft8nGmuMVl9b9xZU",
        "start_index": offset,
    }
    response = requests.get(google_books_api_url, params=params)
    response_data = response.json()

    books = []
    for item in response_data.get("items", []):
        volume_info = item.get("volumeInfo", {})
        book = {
            "id": item.get("id"),
            "title": volume_info.get("title"),
            "authors": volume_info.get("authors", []),
            "publisher": volume_info.get("publisher"),
            "publishedDate": volume_info.get("publishedDate"),
            "description": volume_info.get("description"),
            "pageCount": volume_info.get("pageCount"),
            "categories": volume_info.get("categories", []),
            "thumbnail": volume_info.get("imageLinks", {}).get("thumbnail"),
        }
        books.append(book)
    return {"total": response_data.get("totalItems", 0), "results": books}


app.include_router(router)
