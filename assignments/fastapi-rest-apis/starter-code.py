"""
FastAPI REST API Starter Code
Complete the tasks below to build a functional REST API for managing books.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI(title="Book Management API", version="1.0.0")

# ============================================================================
# DATA MODELS
# ============================================================================
# TODO: Define a Pydantic model for Book with fields: id, title, author, year
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# ============================================================================
# IN-MEMORY DATABASE
# ============================================================================
# TODO: Create a list to store books in memory
books_db: List[Book] = []
next_id = 1


# ============================================================================
# TASK 1: HEALTH CHECK ENDPOINT
# ============================================================================
# TODO: Implement a GET endpoint at /health that returns a status message
@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify the API is running.
    Returns a JSON response with status and message.
    """
    # TODO: Implement this endpoint
    pass


# ============================================================================
# TASK 2: CRUD OPERATIONS
# ============================================================================
# TODO: Implement POST /books - Create a new book
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    """
    Create a new book.
    TODO: Implement this endpoint
    """
    pass


# TODO: Implement GET /books - List all books
@app.get("/books")
async def list_books():
    """
    Retrieve all books.
    TODO: Implement this endpoint
    """
    pass


# TODO: Implement GET /books/{id} - Get a specific book
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    """
    Retrieve a specific book by ID.
    TODO: Implement this endpoint
    """
    pass


# TODO: Implement PUT /books/{id} - Update a book
@app.put("/books/{book_id}")
async def update_book(book_id: int, updated_book: Book):
    """
    Update an existing book.
    TODO: Implement this endpoint
    """
    pass


# TODO: Implement DELETE /books/{id} - Delete a book
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    """
    Delete a book by ID.
    TODO: Implement this endpoint
    """
    pass


# ============================================================================
# TASK 3: QUERY PARAMETERS AND ADVANCED FILTERING
# ============================================================================
# TODO: Implement GET /books/search - Search books by author or year
@app.get("/books/search")
async def search_books(author: Optional[str] = None, year: Optional[int] = None):
    """
    Search for books by author or year.
    TODO: Implement this endpoint with query parameters
    """
    pass


# ============================================================================
# RUN THE SERVER
# ============================================================================
# To run this server, use:
# uvicorn main:app --reload
#
# Then visit http://localhost:8000/docs to see the interactive API documentation
