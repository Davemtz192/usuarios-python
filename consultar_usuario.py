
import sqlite3

usuario = input("Ingresa el nombre de usuario a consultar: ")

conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
resultado = cursor.fetchone()

if resultado:
    print("Datos del usuario:")
    print(f"ID: {resultado[0]}")
    print(f"Usuario: {resultado[1]}")
    print(f"Nombre: {resultado[2]}")
    print(f"Correo: {resultado[3]}")
    print(f"Teléfono: {resultado[4]}")
    print(f"Dirección: {resultado[5]}")
    print(f"Contraseña (hash): {resultado[6]}")
else:
    print("Usuario no encontrado.")

conexion.close()
