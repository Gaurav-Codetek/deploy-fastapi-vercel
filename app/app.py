from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()

# Define the request body using Pydantic model
class PromptRequest(BaseModel):
    prompt: str
class dataReq(BaseModel):
    title: str
    content: str

uri = os.getenv('URI')
db = 'knowledge_base'
col = 'Tempo'
client = MongoClient(uri)
database = client[db]
collection = database[col]

print("Server ran once")
@app.post("/addData")
async def add_data(request: dataReq):
    title = request.title
    content = request.content

    collection.insert_one({"title": title, "content": content})
    print("Data added")

    return {"title": title, "content": content}
@app.get('/')
def hello_world():
    return "Hello,World"

# To run the application, use the command below:
# uvicorn {file name}:app --reload
