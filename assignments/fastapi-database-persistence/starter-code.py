"""
Starter code for Database Persistence with FastAPI & SQLAlchemy

This is a template to get you started. Complete the tasks in the assignment README.md
"""

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# ============================================================================
# DATABASE SETUP
# ============================================================================

# TODO: Create database URL pointing to SQLite database (sqlite:///todos.db)
DATABASE_URL = ""  # Replace with your database URL

# TODO: Create SQLAlchemy engine
# engine = create_engine(DATABASE_URL, connect_args={...})

# TODO: Create session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# TODO: Create declarative base
Base = declarative_base()


# ============================================================================
# DATABASE MODELS
# ============================================================================

# TODO: Define Todo model
# Requirements:
# - Table name: "todos"
# - Fields: id, title, description, completed, created_at
# - See assignment README for full specifications


# ============================================================================
# PYDANTIC SCHEMAS
# ============================================================================

# TODO: Define TodoCreate schema for input validation
# Fields: title (required), description (optional)

# TODO: Define TodoResponse schema for API responses
# Fields: id, title, description, completed, created_at


# ============================================================================
# FASTAPI APP
# ============================================================================

app = FastAPI(title="Todo API with Database")


# TODO: Create all database tables on startup
@app.on_event("startup")
def startup():
    pass


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================================================
# API ENDPOINTS - Task 2: CRUD Operations
# ============================================================================

# TODO: POST /todos - Create a new todo
# Returns: TodoResponse (with status code 201)
@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = get_db()):
    pass


# TODO: GET /todos - List all todos
# Returns: List of TodoResponse
@app.get("/todos")
def list_todos(db: Session = get_db()):
    pass


# TODO: GET /todos/{id} - Get a specific todo
# Returns: TodoResponse or 404 error
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = get_db()):
    pass


# TODO: PUT /todos/{id} - Update a todo
# Returns: Updated TodoResponse or 404 error
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoCreate, db: Session = get_db()):
    pass


# TODO: DELETE /todos/{id} - Delete a todo
# Returns: Success message or 404 error
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = get_db()):
    pass


# ============================================================================
# BONUS: Task 3 - Query Filtering and Pagination
# ============================================================================

# TODO: Modify GET /todos to support:
# - skip: int = 0 (query parameter)
# - limit: int = 10 (query parameter)
# - completed: Optional[bool] = None (query parameter)
# Return: {"todos": [...], "total": int, "skip": int, "limit": int}


# ============================================================================
# BONUS: Task 4 - Database Relationships
# ============================================================================

# TODO: Create TodoCategory model
# TODO: Add category relationship to Todo
# TODO: Implement /categories endpoints
# TODO: Implement /categories/{category_id}/todos endpoint


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
