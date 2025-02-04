from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

# print("MYSQL_PASSWORD", os.getenv("MYSQL_PASSWORD"))

password = quote_plus(os.getenv("MYSQL_PASSWORD"))
DATABASE_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{password}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency (dùng trong FastAPI nếu cần)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
