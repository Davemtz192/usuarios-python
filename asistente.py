import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Inicializa el motor de voz
engine = pyttsx3.init()

# Obtener las voces disponibles y seleccionar la voz en español
voices = engine.getProperty('voices')
for voice in voices:
    if 'spanish' in voice.languages[0].decode('utf-8'):
        engine.setProperty('voice', voice.id)
        break

# Configura velocidad, volumen y tono
engine.setProperty('rate', 150)  # Velocidad moderada
engine.setProperty('volume', 1)  # Volumen máximo
engine.setProperty('pitch', 50)  # Tono ajustado

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-MX")
        print("Dijiste:", comando)
        return comando.lower()
    except sr.UnknownValueError:
        hablar("No entendí, repite por favor.")
        return ""
    except sr.RequestError:
        hablar("Error de conexión con el servicio de reconocimiento.")
        return ""

def ejecutar_comando(comando):
    if "reproduce" in comando:
        cancion = comando.replace("reproduce", "")
        hablar(f"Reproduciendo {cancion}")
        pywhatkit.playonyt(cancion)

    elif "hora" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        hablar(f"Son las {hora}")

    elif "busca" in comando:
        tema = comando.replace("busca", "")
        info = wikipedia.summary(tema, sentences=2, auto_suggest=False)
        hablar("Esto encontré en Wikipedia")
        print(info)
        hablar(info)

    elif "salir" in comando:
        hablar("Hasta luego.")
        exit()

    else:
        hablar("No entendí el comando, ¿puedes repetirlo?")

# Bucle principal
if __name__ == "__main__":
    hablar("Hola, ¿en qué puedo ayudarte?")
    while True:
        comando = escuchar_comando()
        if comando:
            ejecutar_comando(comando)
