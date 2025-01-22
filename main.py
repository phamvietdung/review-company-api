from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ReviewSearchModel(BaseModel):
    search_text: str

@app.get("/search")
async def search_reviews(model: ReviewSearchModel):
    return {"result" : model.search_text}

@app.get("/reviews/{review_id}")
async def get_review(review_id: int):
    return {"review_id": review_id}    
