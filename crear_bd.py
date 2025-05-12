import sqlite3

conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        nombre TEXT,
        correo TEXT,
        telefono TEXT,
        direccion TEXT,
        contrasena_hash TEXT
    )
''')

conexion.commit()
conexion.close()

print("Base de datos y tabla creada correctamente.")
