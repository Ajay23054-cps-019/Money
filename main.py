from database import database
from fastapi import FastAPI

app = FastAPI()
db = database()


@app.get("/")
def main():
    if db.conn:
        db.add_data()
        return "Database connection successful"
    return "Database connection failed, retrying..."
