import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password= "1234",
    database = "test001"
)

my_cursor = db.cursor()


#my_cursor.execute ("CREATE TABLE  Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT )")



my_cursor.execute("CREATE TABLE test001.Practice_Table (c1 int , c2 varchar(50), c3 float, c4 int, c5 varchar(50))")

db.close()