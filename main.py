from database import database
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    if database:
        database_instance = database
        database_instance.add_data()
        return "Database connection successful"
    else:
        return "Database connection failed,retrying..."
