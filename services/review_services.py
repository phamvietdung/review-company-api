from services.dbconnector import mydb
from mysql.connector.abstracts import MySQLCursorAbstract
import json


dbcontext : MySQLCursorAbstract = None

def initConnection():
    return mydb.cursor()

def getReviews(page : int, page_size : int):

    dbcontext = initConnection()

    dbcontext.execute(f"SELECT Id, CompanyName, Salary, Position, `Year`, Other FROM Reviews LIMIT {page_size} OFFSET {page * page_size}")
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
            "Other" : x[5]
        })
    
    return result
    

#print()
#print(json.dumps(getReviews()))
getReviews(1, 20)