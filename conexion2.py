import mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="publico", passwd="123456", database="basedatos2")
cursor1=conexion1.cursor()

cursor1.execute("show tables")

for tabla in cursor1:
    print(tabla)

conexion1.close()