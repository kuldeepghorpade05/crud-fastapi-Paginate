# Books API

A simple CRUD API created with FastAPI and SQLAlchemy for PostgreSQL

## Available APIs

It is recommended to test the available APIs from ``[GET] /docs``

- ``[GET] /`` - Root (Check API status)
- ``[POST] /books`` - Create Book
- ``[GET] /books/{id}`` - Find Book
- ``[GET] /books`` - Get Books
- ``[PUT] /books`` - Update Book
- ``[DELETE] /books`` - Delete Book

## Usage

1. Install [poetry](https://python-poetry.org/)
2. Copy `.env.sample` to create `.env` and fill the environment variables accordingly
3. Run `poetry install` to install dependencies
4. Run `poetry run uvicorn app.main:app` to serve the app


Description:
A high-performance web API built with FastAPI that supports asynchronous operations, data validation, and database interactions. Features include:

FastAPI for building RESTful APIs.

SQLAlchemy and psycopg2 for database ORM and PostgreSQL integration.

Pydantic for data validation and settings management.

Uvicorn as the ASGI server for high-speed async handling.

Asynchronous support via AnyIO and Starlette.

Environment management using python-dotenv.

Development tools like Black for code formatting, isort for import sorting, and Click for CLI utilities.

<!-- cmd  -->
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000