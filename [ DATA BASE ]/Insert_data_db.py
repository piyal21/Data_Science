import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password= "1234",
    database = "test001"
)

my_cursor = db.cursor()


#my_cursor.execute ("CREATE TABLE  Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT )")



#my_cursor.execute("CREATE TABLE test001.Practice_Table (c1 int , c2 varchar(50), c3 float, c4 int, c5 varchar(50))")

#my_cursor.execute("insert into test001.practice_table values(107,'piyal',3.05,200104107,'ahmed'  )")
my_cursor.execute("insert into test001.practice_table values(113,'Yusha',3.05,200104113,'Abdullah'  )")
my_cursor.execute("insert into test001.practice_table values(144,'Shuvo',3.05,200104144,'Ashraf'  )")
my_cursor.execute("insert into test001.practice_table values(110,'Mahy',3.05,200104110,'Arman'  )")
my_cursor.execute("insert into test001.practice_table values(109,'Mahir',3.05,200104109,'Sadman'  )")
my_cursor.execute("insert into test001.practice_table values(108,'Shakir',3.05,200104108,'ahmed'  )")


db.commit()
db.close()