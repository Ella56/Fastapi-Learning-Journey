import uvicorn
from fastapi import FastAPI
 
app = FastAPI()

name_lst = [
    {'id':1,'name':'arash'},
    {'id':2,'name':'rouya'},
    {'id':3,'name':'saman'},
    {'id':4,'name':'payam'},
    {'id':5,'name':'arash'},
]




@app.get("/")
def root():
    return {'message':'Hello World!'}

@app.get("/name")
def names():
    return name_lst

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")