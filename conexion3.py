import cgi, mysql.connector

conexion1 = mysql.connector.connect(host="localhost", user="publico", passwd="123456", database="basedatos2")
cursor1=conexion1.cursor()

cursor1.execute("select * from libros")

print("Content-Type: text/html")
print()

print("<html>")
print("<head>")
print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">')
print("</head>")
print("<body>")
print('<table class="table container-sm text-center ">')
print('<tr class="table-success">')
print('<th scope="col">')
print("ID LIBRO")
print('</th>')
print('<th scope="col">')
print("NOMBRE LIBRO")
print('</th>')
print("<tr>")
for linea in cursor1:
    print('<tr>')
    for dato in linea:
        print("<td>")
        print(dato)
        print("</td>")
    print("</tr>")
print("<table>")
print("</body>")
print("</html>")
conexion1.close()