from pydantic import BaseModel

class ReviewSearchModel(BaseModel):
    search_text: str
    page : int
    page_size: int

class ReviewUpdateModel(BaseModel):
    # review_id: int
    company_name: str
    salary: str
    position: str
    year: str
    other: str
    # hash: str
    # json_raw_data: str