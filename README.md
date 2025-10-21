# Mini Recipes API

A small FastAPI project for managing recipes.  
This project demonstrates basic CRUD operations and RESTful API design.

## Features
- Create, read, update, and delete recipes
- Uses Pydantic models for data validation
- Designed for easy upgrade to persistent storage with SQLAlchemy

## Tech Stack
- Python 3.12+
- FastAPI
- Pydantic
- Uvicorn (for running the server)

## How to Run
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows

2. Install dependencies:
   pip install -r requirements.txt

3. Run the API:
   fastapi dev main.py (Development)
   fastapi run (Production)


4. Open http://127.0.0.1:8000/docs to explore the endpoints with Swagger UI.