# Para activar el ambiente usamos: .venv\Scripts\activate
# Para correr el proyecto usamos: flask --app hellow run --debug
# Los comentarios anteriores son para la consola cmd, otros comandos pueden no funcionar de la misma manera

from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pos"
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")    
    #return 'Hello, World!'
    
@app.route('/submit', methods=['POST'])
def submit():
    #nombre = request.form['catalogo.html']
    #nombre = "catalogoproductos.html"
    #print("sdfgh")
    #return f'Hola, {nombre}! Tu formulario ha sido enviado exitosamente!'
    #return render_template("catalogoproductos.html")
    #mycursor = mydb.cursor()

    # Obtener datos de la base de datos
    ##mycursor.execute('SELECT * FROM productos')
    #productos = mycursor.fetchall()
    #print(productos)
    # Cerrar la conexión
    #mycursor.close()
    print("Todo bien")
    #return render_template("menu.html", productos=productos)
    return render_template("menu.html")

@app.route('/cp')
def page1():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM productos')
    productos = mycursor.fetchall()
    mycursor.close()
    return render_template('catalogoproductos.html', productos=productos)

@app.route('/cu')
def page2():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM usuarios')
    usuarios = mycursor.fetchall()
    mycursor.close()
    return render_template('catalogousuarios.html', usuarios=usuarios)

@app.route('/cc')
def page3():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM empleados')
    clientes = mycursor.fetchall()
    mycursor.close()
    return render_template('catalogoclientes.html', clientes=clientes)

if __name__ == '__main__':
    app.run()