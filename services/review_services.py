from services.dbconnector import mydb
from mysql.connector.abstracts import MySQLCursorAbstract
import json


dbcontext : MySQLCursorAbstract = None

def initConnection():
    return mydb.cursor()

def getTotalReviews(search_text: str):

    dbcontext = initConnection()

    query = f"SELECT COUNT(*) FROM Reviews"

    if search_text != None and search_text != "":
        query = f"{query} WHERE CompanyName LIKE '%{search_text}%'"

    dbcontext.execute(query)

    data = dbcontext.fetchall()

    return data[0][0]

def getReviews(search_text: str ,page : int, page_size : int, isFilter : bool = False):

    dbcontext = initConnection()

    query = f"SELECT Id, CompanyName, Salary, Position, `Year`, Other, IsHidden, IsReviewed, JsonRawData FROM Reviews"

    total_query = f"SELECT COUNT(*) FROM Reviews"

    isNeedWhere : bool = False

    tailQuery = ""

    if search_text != None and search_text != "":
        isNeedWhere = True
        tailQuery = f"CompanyName LIKE '%{search_text}%'"

    if isFilter:
        isNeedWhere = True
        if tailQuery != "":
            tailQuery = f"{tailQuery} AND IsHidden = 0"

    if isNeedWhere:
        query = f"{query} WHERE {tailQuery}"
        total_query = f"{total_query} WHERE {tailQuery}"

    query = f"{query} LIMIT {page_size} OFFSET {page * page_size};"

    print(query)

    dbcontext.execute(query)

    data = dbcontext.fetchall()

    result = []

    for x in data:
        # print(x[0], x[1], x[2], x[3], x[4], x[5])
        result.append({
            "Id" : x[0],
            "CompanyName" : x[1],
            "Salary" : x[2],
            "Position" : x[3],
            "Year" : x[4],
            "Other" : x[5],
            "IsHidden" : x[6],
            "IsReviewed" : x[7],
            "JsonRawData" : x[8]
        })
    
    dbcontext.execute(total_query)

    total_data = dbcontext.fetchall()

    total = total_data[0][0]

    return {
        "items" : result,
        "total" : total
    }

def UpdateReviewIsHidden(review_id: int, is_hidden: bool):
    dbcontext = initConnection()

    query = f"UPDATE Reviews SET IsHidden = {is_hidden} WHERE Id = {review_id};"

    dbcontext.execute(query)

    mydb.commit()

def UpdateReviewIsReviewed(review_id: int, is_reviewed: bool):
    dbcontext = initConnection()

    query = f"UPDATE Reviews SET IsReviewed = {is_reviewed} WHERE Id = {review_id};"

    dbcontext.execute(query)

    mydb.commit()

#print()
#print(json.dumps(getReviews()))
#getReviews(1, 20)