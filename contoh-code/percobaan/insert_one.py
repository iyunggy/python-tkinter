import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_mainan"
)

cursor = db.cursor() #cursor = untuk eksekusi perintah SQL
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Dian", "Mataram")
cursor.execute(sql, val) #ececute = method untuk eksekusi

db.commit() #untuk menyimpan data

print("{} data ditambahkan".format(cursor.rowcount))