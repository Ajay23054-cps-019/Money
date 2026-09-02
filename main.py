from database import database
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
db = database()


class Transaction(BaseModel):
    username: str
    name: str
    value: str


@app.get("/")
def main():
    if db.conn:
        db.add_data()
        return "Database connection successful"
    return "Database connection failed, retrying..."


@app.post("/add")
def add_transaction(transaction: Transaction):
    if not db.conn:
        raise HTTPException(status_code=500, detail="Database not connected")
    db.insert_transaction(transaction.username, transaction.name, transaction.value)
    return {"message": "Transaction added successfully"}
