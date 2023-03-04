import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password= "1234",
    database = "test001"
)

my_cursor = db.cursor()





my_cursor.execute("select * from test001.practice_table")

for i in my_cursor.fetchall():
    print(i)

db.close()