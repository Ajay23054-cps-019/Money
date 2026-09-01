from database import get_db_connection
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    if get_db_connection():
        return "Database connection successful"
    else:
        return "Database connection failed,retrying..."
