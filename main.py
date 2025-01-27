from fastapi import FastAPI, Response
from pydantic import BaseModel
from services.review_services import getReviews, getTotalReviews, UpdateReviewIsHidden, UpdateReviewIsReviewed
from fastapi.middleware.cors import CORSMiddleware
from services.dbconnector import token

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

@app.post("/search")
async def search_reviews(model: ReviewSearchModel, key : str = None):
    return getReviews(model.search_text, model.page, model.page_size, key != token)

@app.get("/reviews/{review_id}")
async def get_review(review_id: int):
    return {"review_id": review_id}    

@app.put("/reviews/{review_id}/is_hidden/{is_hidden}")
async def update_review_is_hidden(review_id: int, is_hidden: bool, key: str, response : Response):
    if(key != token):
        response.status_code = 401
        return {"error": "Invalid key"}
    UpdateReviewIsHidden(review_id, is_hidden)
    return {"review_id": review_id, "is_hidden": is_hidden}


@app.put("/reviews/{review_id}/is_reviewed/{is_reviewed}")
async def update_review_is_reviewed(review_id: int, is_reviewed: bool, key: str, response : Response):
    if(key != token):
        response.status_code = 401
        return {"error": "Invalid key"}
    UpdateReviewIsReviewed(review_id, is_reviewed)
    return {"review_id": review_id, "is_reviewed": is_reviewed}