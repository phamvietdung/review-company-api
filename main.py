from fastapi import FastAPI
from pydantic import BaseModel
from services.review_services import getReviews
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173",
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
async def search_reviews(model: ReviewSearchModel):
    return getReviews(model.page, model.page_size)
    #return {"result" : model.search_text}

@app.get("/reviews/{review_id}")
async def get_review(review_id: int):
    return {"review_id": review_id}    
