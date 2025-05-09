from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    db = mysql.connector.connect(
        host='mysql',
        user='root',
        password='123456',
        database='prueba'
    )
    cursor = db.cursor()
    cursor.execute("SELECT nombre FROM usuarios")
    resultados = cursor.fetchall()
    html = "<h1>Usuarios</h1><ul>"
    for nombre in resultados:
        html += f"<li>{nombre[0]}</li>"
    html += "</ul>"
    db.close()
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')
