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


#/names (GET(RETRIEVE), POST(CREATE))
@app.get("/names")
def names():
    return name_lst





#/names/:id (GET(RETRIVE),PUT/PATCH(UPDATE),DELETE)
@app.get("/names/{name_id}")
def get_name_detail(name_id:int):
    for name in name_lst:
        if name["id"] == name_id:
            return  name
    return {"detail" : "object not found"}






if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")