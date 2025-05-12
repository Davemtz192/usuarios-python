import sqlite3
import hashlib

# Datos de entrada
usuario = "davidmtz"
contrasena = "MiContrasenaSegura123"
nombre = "David Misael"
correo = "davidmtz20009@gmail.com"
telefono = "8110845907"
direccion = "Calle Madrid 515"

# Encriptar la contraseña con SHA-256
contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()

# Conectar a la base de datos
conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

# Insertar datos en la tabla
cursor.execute('''
INSERT INTO usuarios (usuario, nombre, correo, telefono, direccion, contrasena_hash)
VALUES (?, ?, ?, ?, ?, ?)
''', (usuario, nombre, correo, telefono, direccion, contrasena_hash))

# Guardar y cerrar
conexion.commit()
conexion.close()

print("Usuario insertado con contraseña encriptada.")
