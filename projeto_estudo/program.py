import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database_py"
)

mycursor = mydb.cursor()

nome = input("insira o seguinte nome na database:")

queryc1 = "INSERT INTO usuarios (Nome) VALUES (%s)"
values = (nome,)
mycursor.execute(queryc1,values)
mydb.commit()

querys1 = "SELECT * FROM usuarios"
mycursor.execute(querys1)
result = mycursor.fetchall()

for row in result:
    print(row)


