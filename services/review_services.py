from mysql_connector import mydb
from mysql.connector.abstracts import MySQLCursorAbstract


dbcontext : MySQLCursorAbstract = mydb.cursor() 

def getReviews(page : int, page_size : int):
    dbcontext.execute("SELECT Id, CompanyName, Salary, Position, `Year`, Other FROM Reviews LIMIT ")
    data = dbcontext.fetchall()

    result = []

    for x in data:
        print(x[0], x[1], x[2], x[3], x[4], x[5])
        result.append({
            "Id" : x[0]
        })
    return result
    

print(getReviews())