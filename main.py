from database import database
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    if database:
        return "Database connection successful"
    else:
        return "Database connection failed,retrying..."
