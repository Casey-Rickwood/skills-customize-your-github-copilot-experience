# 📘 Assignment: Database Persistence with FastAPI & SQLAlchemy

## 🎯 Objective

Learn how to build persistent REST APIs using FastAPI and SQLAlchemy ORM to store and manage data in a SQLite database. Understand database schema design, CRUD operations with ORM, and how to handle relationships between entities.

## 📝 Tasks

### 🛠️ Task 1: Database Setup and Schema Definition

#### Description
Set up SQLAlchemy with a SQLite database and define your first database model for a "Todo" resource.

#### Requirements
Your implementation should:

- Import and configure SQLAlchemy with SQLite (`sqlite:///todos.db`)
- Create a SQLAlchemy `Base` class using `declarative_base()`
- Define a `Todo` model with the following attributes:
  - `id` (Integer, primary key, auto-increment)
  - `title` (String, required, max 200 characters)
  - `description` (String, optional)
  - `completed` (Boolean, default False)
  - `created_at` (DateTime, default current timestamp)
- Create a database engine and initialize tables using `Base.metadata.create_all()`
- Ensure the database file is created when the application starts

#### Example Schema
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
```

### 🛠️ Task 2: CRUD Operations with Database Persistence

#### Description
Implement complete CRUD operations for todos that persist data to the database.

#### Requirements
Your implementation should:

- Define a Pydantic `TodoCreate` schema for input validation
- Define a Pydantic `TodoResponse` schema for API responses (include id and created_at)
- Implement a POST endpoint at `/todos` to create a new todo in the database
- Implement a GET endpoint at `/todos` to retrieve all todos from the database
- Implement a GET endpoint at `/todos/{id}` to retrieve a specific todo by ID
- Implement a PUT endpoint at `/todos/{id}` to update an existing todo
- Implement a DELETE endpoint at `/todos/{id}` to delete a todo
- Return appropriate HTTP status codes (201 for create, 404 for not found)
- Use SQLAlchemy sessions to query and manipulate the database

#### Example Usage
```python
# POST /todos
Request: {"title": "Learn FastAPI", "description": "Complete the FastAPI tutorial"}
Response: {
    "id": 1, 
    "title": "Learn FastAPI", 
    "description": "Complete the FastAPI tutorial",
    "completed": false,
    "created_at": "2026-08-13T10:30:00"
}

# GET /todos
Response: [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Complete the FastAPI tutorial",
        "completed": false,
        "created_at": "2026-08-13T10:30:00"
    }
]

# PUT /todos/1
Request: {"title": "Learn FastAPI", "completed": true}
Response: {"id": 1, "title": "Learn FastAPI", "completed": true, ...}

# DELETE /todos/1
Response: {"message": "Todo deleted successfully"}
```

### 🛠️ Task 3: Query Filtering and Advanced Database Operations

#### Description
Add filtering capabilities to query todos based on completion status and implement pagination.

#### Requirements
Your implementation should:

- Modify the GET `/todos` endpoint to accept optional query parameters:
  - `skip` (default 0): number of records to skip
  - `limit` (default 10): maximum number of records to return
  - `completed` (optional): filter by completion status (true/false)
- Implement database filtering using SQLAlchemy query methods
- Return a total count of matching records
- Handle edge cases (invalid parameters, out-of-range values)

#### Example Usage
```python
# GET /todos?skip=0&limit=5
Response: {
    "todos": [...],
    "total": 15,
    "skip": 0,
    "limit": 5
}

# GET /todos?completed=true
Response: {
    "todos": [...],  # Only completed todos
    "total": 5,
    "skip": 0,
    "limit": 10
}

# GET /todos?completed=false&skip=5&limit=10
Response: {
    "todos": [...],  # Incomplete todos, paginated
    "total": 10,
    "skip": 5,
    "limit": 10
}
```

### 🛠️ Task 4 (Bonus): Database Relationships

#### Description
Create a second model to demonstrate one-to-many relationships in SQLAlchemy.

#### Requirements
Your implementation should:

- Create a `TodoCategory` model with:
  - `id` (Integer, primary key)
  - `name` (String, required, unique)
- Add a `category_id` foreign key to the `Todo` model
- Define a relationship between `Todo` and `TodoCategory`
- Implement endpoints to:
  - Create a new category: POST `/categories`
  - List all categories: GET `/categories`
  - Get todos by category: GET `/categories/{category_id}/todos`
- Update the Todo response schema to include category information
- Handle cascading deletes (when a category is deleted, associated todos are handled appropriately)

#### Example Usage
```python
# POST /categories
Request: {"name": "Work"}
Response: {"id": 1, "name": "Work"}

# POST /todos (with category)
Request: {
    "title": "Finish report",
    "description": "Complete quarterly report",
    "category_id": 1
}
Response: {
    "id": 1,
    "title": "Finish report",
    "category_id": 1,
    "category": {"id": 1, "name": "Work"},
    ...
}

# GET /categories/1/todos
Response: [
    {"id": 1, "title": "Finish report", "category_id": 1, ...}
]
```

## 🎓 Learning Outcomes

By completing this assignment, you will:

- Understand how to integrate databases with REST APIs
- Learn SQLAlchemy ORM and database schema design
- Practice CRUD operations with persistent storage
- Understand how to handle database relationships
- Learn about pagination and filtering in APIs
- Work with transactions and database sessions
- Build production-ready API endpoints with data persistence
