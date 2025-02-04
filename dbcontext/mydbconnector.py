from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import os
from urllib.parse import quote_plus

dotenv_path = find_dotenv()
print(f"Loading .env file from: {dotenv_path}")

print("DATABASE_URL:", os.getenv("MYSQL_USER"))

print(os.path.dirname(__file__))

# load_dotenv()

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Cấu hình URL của MySQL
# DATABASE_URL = os.getenv("DATABASE_URL")
password = quote_plus(os.getenv("MYSQL_PASSWORD"))
DATABASE_URL = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{password}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"

print(DATABASE_URL)

# Khởi tạo engine kết nối
engine = create_engine(DATABASE_URL, echo=True)

# engine = create_engine(
#     f"mysql+pymysql://",
#     username=os.getenv("MYSQL_USER"),
#     password=os.getenv("MYSQL_PASSWORD"),
#     host=os.getenv("MYSQL_HOST"),
#     database=os.getenv("MYSQL_DATABASE")
# )

# Tạo SessionLocal để làm việc với database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base để định nghĩa các model
Base = declarative_base()

# Dependency (dùng trong FastAPI nếu cần)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# from sqlalchemy.orm import Session
# db: Session = SessionLocal()

# a = db.query(Reviews).all()

# for i in a:
#     print(i.CompanyName)