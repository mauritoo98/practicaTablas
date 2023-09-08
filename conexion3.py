import cgi, mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="publico", passwd="123456", database="basedatos2")
cursor1=conexion1.cursor()

cursor1.execute("select * from libros")

print("Content-Type: text/html")
print()

print("<html>")
print("<head>")
print('<link rel="stylesheet" href="style.css">')
print("</head>")
print("<body>")
print("<table>")
print("<th>")
print("<tr>")
print("<td>")
print("ID LIBRO")
print("</td>")
print("<td>")
print("NOMBRE LIBRO")
print("</td>")
print("</tr>")
print("<th>")
for linea in cursor1:
    print('<tr class="tabla">')
    for dato in linea:
        print("<td>")
        print(dato)
        print("</td>")
    print("</tr>")
print("<table>")
print("</body>")
print("</html>")
conexion1.close()