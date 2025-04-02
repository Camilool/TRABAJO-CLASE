from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Conectar con MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.biblioteca
usuarios = db.usuarios

# Página principal con formulario y lista de usuarios
@app.route('/')
def index():
    usuarios_list = list(usuarios.find())
    return render_template('index.html', usuarios=usuarios_list, usuario_editar=None)

# Agregar usuario
@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    usuarios.insert_one({'nombre': nombre, 'email': email, 'telefono': telefono})
    return redirect(url_for('index'))

# Eliminar usuario
@app.route('/eliminar/<id>')
def eliminar(id):
    usuarios.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

# Cargar usuario para editar en la misma página
@app.route('/editar/<id>')
def editar(id):
    usuario = usuarios.find_one({'_id': ObjectId(id)})
    usuarios_list = list(usuarios.find())
    return render_template('index.html', usuarios=usuarios_list, usuario_editar=usuario)

# Actualizar usuario
@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    usuarios.update_one({'_id': ObjectId(id)}, {'$set': {'nombre': nombre, 'email': email, 'telefono': telefono}})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
