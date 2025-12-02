# Biblioteca Back

A FastAPI-based backend API for managing a library system with book inventory and reporting capabilities.

## 📋 Overview

This project is a RESTful API built with FastAPI that manages a library's book collection across multiple rooms and bookshelves. It provides endpoints for CRUD operations on books and tracking reports of where books are found.

## 🏗️ Architecture

The project follows a **layered architecture** pattern with clear separation of concerns:

```
biblioteca-back/
├── controllers/          # API endpoints and route handlers
│   ├── book_controller. py
│   └── report_controller.py
├── services/            # Business logic layer
│   ├── book_service.py
│   └── report_service.py
├── repositories/        # Data access layer
│   ├── book_repository. py
│   └── report_repository.py
├── models/              # Database models (SQLModel)
│   ├── book.py
│   └── report.py
├── schemas/             # Pydantic schemas for validation
│   ├── book_schema.py
│   └── report_schema.py
├── database. py          # Database configuration and session management
├── main.py              # Application entry point
└── pyproject.toml       # Project dependencies and configuration
```

### Architecture Layers

1. **Controllers Layer**: Handles HTTP requests/responses and route definitions
2. **Services Layer**: Contains business logic and orchestrates operations
3. **Repositories Layer**: Manages database operations and queries
4. **Models Layer**: Defines database table structures using SQLModel
5. **Schemas Layer**: Defines Pydantic models for request/response validation

## 🚀 Features

- **Book Management**: Create, read, update, and delete books
- **Book Organization**: Track books across rooms (sala1, sala3, sala4) and bookshelves (1-40)
- **Reporting System**: Record and track where books are found
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation
- **Database**: PostgreSQL with SQLModel ORM

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.123.0+
- **ORM**: SQLModel 0.0.27
- **Database**: PostgreSQL
- **Database Driver**: psycopg2-binary 2.9.11
- **Python Version**: 3.13+
- **Package Manager**: uv (instead of pip)

## 📦 Installation

This project uses **[uv](https://github.com/astral-sh/uv)** as the package manager instead of pip for faster and more reliable dependency management.

### Prerequisites

- Python 3.13+
- PostgreSQL
- uv package manager

### Install uv

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip (if you prefer)
pip install uv
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/parZival26/biblioteca-back.git
cd biblioteca-back
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Start PostgreSQL database using Docker Compose:
```bash
docker-compose up -d
```

The docker-compose.yml sets up PostgreSQL with the following credentials:
- **Database**: biblioteca
- **User**: biblioteca_user
- **Password**: biblioteca_pass
- **Port**: 5432

## 🏃 Running the Application

### Using uv

```bash
# Run the FastAPI development server
uv run fastapi dev main.py
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Endpoints

### Books

- `POST /books/` - Create a new book
- `GET /books/` - List all books (with pagination)
- `GET /books/{book_id}` - Get a specific book
- `PUT /books/{book_id}` - Update a book
- `DELETE /books/{book_id}` - Delete a book

### Reports

- `POST /reports/` - Create a new report
- `GET /reports/` - List all reports (sorted by date, newest first)

## 🗃️ Database Models

### Book
- `id`: Primary key
- `title`: Book title (indexed)
- `author`: Book author (indexed)
- `year`: Publication year (optional)
- `room`: Room location (sala1, sala3, or sala4)
- `bookShelf`: Bookshelf number (1-40)

### Report
- `id`: Primary key
- `bookId`: Foreign key to Book
- `roomFound`: Room where book was found
- `bookShelfFound`: Bookshelf where book was found
- `date`: Timestamp of report creation

## 🔧 Development

### Project Dependencies

Dependencies are managed in `pyproject.toml`:
- fastapi[standard] >= 0.123.0
- sqlmodel >= 0.0.27
- psycopg2-binary >= 2.9.11
- pymysql >= 1. 1.2

### Adding New Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name
```

### Running in Production

For production deployment, use a production-grade server like uvicorn with multiple workers:

```bash
uv run

