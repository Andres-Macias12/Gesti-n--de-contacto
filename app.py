from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Definir la clase Contacto
class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

# Lista para almacenar los contactos con algunos ya agregados
contactos = [
    Contacto("Juan Pérez", "123-456-7890"),
    Contacto("María López", "234-567-8901"),
    Contacto("Carlos Ruiz", "345-678-9012")
]

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar los contactos
@app.route('/contactos')
def mostrar_contactos():
    return render_template('contactos.html', contactos=contactos)

# Ruta para agregar un nuevo contacto
@app.route('/agregar', methods=['POST'])
def agregar_contacto():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    nuevo_contacto = Contacto(nombre, telefono)
    contactos.append(nuevo_contacto)
    return redirect(url_for('mostrar_contactos'))

# Ruta para buscar un contacto por nombre
@app.route('/buscar', methods=['POST'])
def buscar_contacto():
    nombre = request.form['nombre']
    resultados = [contacto for contacto in contactos if contacto.nombre.lower() == nombre.lower()]
    return render_template('contactos.html', contactos=resultados)

# Ruta para eliminar un contacto por nombre
@app.route('/eliminar', methods=['POST'])
def eliminar_contacto():
    nombre = request.form['nombre']
    global contactos
    contactos = [contacto for contacto in contactos if contacto.nombre.lower() != nombre.lower()]
    return redirect(url_for('mostrar_contactos'))

if __name__ == '__main__':
    app.run(debug=True)
