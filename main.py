from fastapi import FastAPI, Response
from pydantic import BaseModel
from dbcontext.review_repository import get_reviews, update_review_is_hidden, update_review_is_reviewed, update_review
from fastapi.middleware.cors import CORSMiddleware
from services.dbconnector import token
from sqlalchemy.orm import Session
from dbcontext.mydbconnector import SessionLocal

print("runngin?")

app = FastAPI()

origins = [
    "http://localhost:5678",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ReviewSearchModel(BaseModel):
    search_text: str
    page : int
    page_size: int

class ReviewUpdateModel(BaseModel):
    review_id: int
    company_name: str
    salary: str
    position: str
    year: str
    other: str
    hash: str
    json_raw_data: str

@app.post("/search")
async def search_reviews(model: ReviewSearchModel, key : str = None):
    db: Session = SessionLocal()
    return get_reviews(db, model.search_text, model.page, model.page_size, key != token)

@app.get("/reviews/{review_id}")
async def get_review(review_id: int):
    return {"review_id": review_id}    

@app.put("/reviews/{review_id}/is_hidden/{is_hidden}")
async def update_review_is_hidden(review_id: int, is_hidden: bool, key: str, response : Response):
    db: Session = SessionLocal()
    if(key != token):
        response.status_code = 401
        return {"error": "Invalid key"}
    update_review_is_hidden(db, review_id, is_hidden)
    return {"review_id": review_id, "is_hidden": is_hidden}


@app.put("/reviews/{review_id}/is_reviewed/{is_reviewed}")
async def update_review_is_reviewed(review_id: int, is_reviewed: bool, key: str, response : Response):
    db: Session = SessionLocal()
    if(key != token):
        response.status_code = 401
        return {"error": "Invalid key"}
    update_review_is_reviewed(db, review_id, is_reviewed)
    return {"review_id": review_id, "is_reviewed": is_reviewed}

@app.put("/reviews/{review_id}")
async def update_review(review_id: int, model: ReviewUpdateModel, key: str, response : Response):
    db: Session = SessionLocal()
    if(key != token):
        response.status_code = 401
        return {"error": "Invalid key"}
    update_review(db, review_id, model.company_name, model.salary, model.position, model.year, model.other, model.hash, model.json_raw_data)
    return {"review_id": review_id}