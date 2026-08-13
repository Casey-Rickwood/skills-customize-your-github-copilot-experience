# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using FastAPI framework to understand HTTP methods, request/response handling, data validation, and modern API development practices.

## 📝 Tasks

### 🛠️ Task 1: Basic API Setup and Health Check Endpoint

#### Description
Create a FastAPI application with a basic health check endpoint to verify the server is running.

#### Requirements
Your implementation should:

- Import and initialize FastAPI
- Create a GET endpoint at `/health` that returns a status message
- Return a JSON response with format: `{"status": "healthy", "message": "API is running"}`
- Be able to run the server using `uvicorn main:app --reload`

#### Example Output
```
GET /health
Response: {"status": "healthy", "message": "API is running"}
```

### 🛠️ Task 2: CRUD Operations for a Simple Resource

#### Description
Implement a complete CRUD (Create, Read, Update, Delete) API for managing a simple "Book" resource with properties like id, title, author, and year.

#### Requirements
Your implementation should:

- Define a Pydantic model for Book with fields: `id` (int), `title` (str), `author` (str), `year` (int)
- Create an in-memory list to store books
- Implement a POST endpoint at `/books` to create a new book
- Implement a GET endpoint at `/books` to list all books
- Implement a GET endpoint at `/books/{id}` to retrieve a specific book by ID
- Implement a PUT endpoint at `/books/{id}` to update a book
- Implement a DELETE endpoint at `/books/{id}` to delete a book
- Return appropriate HTTP status codes (201 for create, 200 for success, 404 for not found)

#### Example Usage
```python
# POST /books
{"title": "Python Basics", "author": "John Doe", "year": 2023}
# Response: {"id": 1, "title": "Python Basics", "author": "John Doe", "year": 2023}

# GET /books
# Response: [{"id": 1, "title": "Python Basics", ...}]

# GET /books/1
# Response: {"id": 1, "title": "Python Basics", ...}

# PUT /books/1
{"title": "Advanced Python", "author": "Jane Smith", "year": 2024}
# Response: {"id": 1, "title": "Advanced Python", ...}

# DELETE /books/1
# Response: {"message": "Book deleted successfully"}
```

### 🛠️ Task 3: Query Parameters and Input Validation

#### Description
Add advanced features to handle query parameters and validate user input.

#### Requirements
Your implementation should:

- Add a GET endpoint at `/books/search` that accepts optional query parameters: `author` and `year`
- Filter books based on the provided query parameters
- Use Pydantic for automatic request validation
- Return a 400 error for invalid input
- Return an empty list if no matches are found

#### Example Usage
```python
# GET /books/search?author=John%20Doe
# Response: [{"id": 1, "title": "Python Basics", ...}]

# GET /books/search?year=2023
# Response: [{"id": 1, "title": "Python Basics", ...}]

# GET /books/search?author=Unknown
# Response: []
```

## 🎓 Learning Outcomes

By completing this assignment, you will:

- Understand HTTP methods (GET, POST, PUT, DELETE)
- Learn how to build REST APIs following REST principles
- Work with Pydantic for data validation
- Understand request/response handling in FastAPI
- Practice CRUD operations and data persistence
- Learn about HTTP status codes and proper API design

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [HTTP Status Codes](https://httpwg.org/specs/rfc9110.html#status.codes)
- [REST API Best Practices](https://restfulapi.net/)

## 🚀 Getting Started

1. Install FastAPI and Uvicorn:
   ```bash
   pip install fastapi uvicorn
   ```

2. Start with the provided `starter-code.py`
3. Implement each task progressively
4. Test your endpoints using a tool like Postman, curl, or the built-in FastAPI docs at `/docs`

## ✅ Submission Checklist

- [ ] All endpoints are implemented and working
- [ ] Data validation is in place using Pydantic
- [ ] Proper HTTP status codes are returned
- [ ] Code is clean and well-commented
- [ ] All tests pass (if applicable)
