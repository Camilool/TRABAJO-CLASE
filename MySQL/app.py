from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Función para conectar a MySQL
def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # 🔹 Cambia esto por tu usuario de MySQL
        password="camilin0823",  # 🔹 Cambia esto por tu contraseña
        database="libreria"
    )

# Página principal con lista de usuarios
@app.route('/')
def index():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template('index.html', usuarios=usuarios, usuario_editar=None)

# Agregar usuario
@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    email = request.form['email']
    numero = request.form['numero']
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email, numero) VALUES (%s, %s, %s)", (nombre, email, numero))
    conexion.commit()
    cursor.close()
    conexion.close()
    
    return redirect(url_for('index'))

# Eliminar usuario.
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()
    
    return redirect(url_for('index'))

# Cargar usuario para editar en la misma página.
@app.route('/editar/<int:id>')
def editar(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    return render_template('index.html', usuarios=usuarios, usuario_editar=usuario)

# Actualizar usuario
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    nombre = request.form['nombre']
    email = request.form['email']
    numero = request.form['numero']
    
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre = %s, email = %s, numero = %s WHERE id = %s", (nombre, email, numero, id))
    conexion.commit()
    cursor.close()
    conexion.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
