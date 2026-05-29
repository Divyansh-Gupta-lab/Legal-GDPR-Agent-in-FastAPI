"""Main module for the FastAPI application."""
from fastapi import FastAPI
from routers.notes_router import notes_router

app = FastAPI(
    title="FastAPI Learning",
    description="A simple FastAPI application",
    version="0.1.0",
    contact={
        "name": "John Doe",
        "email": "john.doe@example.com",
    },
    license_info={
        "name": "MIT License",
    },
)

app.include_router(notes_router)
