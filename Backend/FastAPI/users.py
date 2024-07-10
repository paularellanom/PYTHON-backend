from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id= 1, name="Pul1", surname="Are1", url="https://pul1.dev", age=41),
              User(id= 2, name="Pul2", surname="Are2", url="https://pul2.dev", age=42),
              User(id= 3, name="Pul3", surname="Are3", url="https://pul3.dev", age=43)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "pul", "surname": "are", "url":"pul.are.com", "age": "40"},
            {"name": "pul", "surname": "are", "url":"pul.are.com", "age": "40"},
            {"name": "pul", "surname": "are", "url":"pul.are.com", "age": "40"}]

@app.get("/users")
async def users():
    return users_list

#path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query
@app.get("/user/")  
async def user(id: int):
    return search_user(id)

def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuaio"}