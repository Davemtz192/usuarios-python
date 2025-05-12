import sqlite3

# Conectar o crear la base de datos
conexion = sqlite3.connect('usuarios.db')

# Crear cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla de usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    nombre TEXT,
    correo TEXT,
    telefono TEXT,
    direccion TEXT,
    contrasena_hash TEXT NOT NULL
)
''')

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()

print("Base de datos y tabla 'usuarios' creada exitosamente.")