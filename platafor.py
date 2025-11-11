import speech_recognition as sr
import subprocess
import pyautogui
import time
import psutil

recognizer = sr.Recognizer()
proceso = None

saludo = "Hola muchachos, ¿como van?\n soy jesus."

def ejecutar_comando(comando):
    global proceso
    if "abrir notepad" in comando:
        print("Abriendo el bloc de notas...")
        proceso = subprocess.Popen(["notepad.exe"])
        time.sleep(1)  

    elif "saludar profesor" in comando:
        print("Escribiendo saludo completo...")
        # Se escribe carácter por carácter con una pequeña pausa
        for letra in saludo:
            pyautogui.write(letra)
            time.sleep(0.02)  # Ajusta el tiempo si quieres que escriba más rápido o lento

    elif "cerrar notepad" in comando:
        print("Cerrando el bloc de notas...")
        if proceso and proceso.poll() is None:
            proceso.terminate()
            print("Bloc de notas cerrado correctamente.")
        else:
            # Cierra cualquier notepad abierto, incluso si el proceso original se perdió
            for p in psutil.process_iter(['name']):
                if p.info['name'] and 'notepad.exe' in p.info['name'].lower():
                    p.terminate()
                    print("Bloc de notas cerrado manualmente.")
                    break

def escuchar_comandos():
    with sr.Microphone() as source:
        print("¿En qué te puedo ayudar?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language="es-ES")
            print(f"Comando reconocido: {comando}")
            ejecutar_comando(comando)
        except sr.UnknownValueError:
            print("No se pudo entender el comando.")
        except sr.RequestError as e:
            print(f"Error al realizar la solicitud: {e}")

while True:
    escuchar_comandos()
