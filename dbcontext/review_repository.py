from sqlalchemy.orm import Session
from dbcontext.models import Reviews

def get_reviews(db: Session, search_text: str, page: int, page_size: int, isFilter: bool = False):
    query = db.query(Reviews)
    if search_text:
        query = query.filter(Reviews.CompanyName.like(f"%{search_text}%"))
    if isFilter:
        query = query.filter(Reviews.IsHidden == 0)

    items = query.offset((page) * page_size).limit(page_size).all()
    total = query.count()

    return {
        "items": items,
        "total": total
    }

def get_review(db: Session, review_id: int):
    return db.query(Reviews).filter(Reviews.Id == review_id).first()

def update_review_is_hidden(db: Session, review_id: int, is_hidden: bool):
    db.query(Reviews).filter(Reviews.Id == review_id).update({Reviews.IsHidden: is_hidden})
    db.commit()

def update_review_is_reviewed(db: Session, review_id: int, is_reviewed: bool):
    db.query(Reviews).filter(Reviews.Id == review_id).update({Reviews.IsReviewed: is_reviewed})
    db.commit()
    
def update_review(db: Session, review_id: int, company_name: str, salary: str, position: str, year: str, other: str):
    db.query(Reviews).filter(Reviews.Id == review_id).update({Reviews.CompanyName: company_name, Reviews.Salary: salary, Reviews.Position: position, Reviews.Year: year, Reviews.Other: other})
    db.commit()