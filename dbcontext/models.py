from sqlalchemy import Boolean, Column, Integer, String
from dbcontext.mydbconnector import Base


class Reviews(Base):
    __tablename__ = "Reviews"

    Id = Column(Integer, primary_key=True, index=True)
    CompanyName = Column(String(500), nullable=True)
    Salary = Column(String(500), nullable=True)
    Position = Column(String(500), nullable=True)
    Year = Column(String(500), nullable=True)
    Other = Column(String(2000), nullable=True)
    Hash = Column(String(100), nullable=True)
    JsonRawData = Column(String(4000), nullable=True)
    IsReviewed = Column(Boolean, nullable=False, default=False)
    IsHidden = Column(Boolean, nullable=False, default=False)
