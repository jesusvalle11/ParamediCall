import speech_recognition as sr
import pywhatkit
import time
recognizer = sr.Recognizer()

# Número de WhatsApp del hospital
numero_hospital = "+573054039480"  

def enviar_mensaje_whatsapp_instantaneo(mensaje):
    try:
        print(f" Enviando mensaje al hospital: {mensaje}")
        pywhatkit.sendwhatmsg_instantly(numero_hospital, mensaje, wait_time=10, tab_close=True)
        print(" Mensaje enviado correctamente al hospital.")
        time.sleep(3)
    except Exception as e:
        print(f" Error al enviar el mensaje: {e}")

def escuchar_comando():
    
    with sr.Microphone() as source:
        print(" Escuchando... di algo como: 'El paciente tiene una fractura'")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language="es-ES")
            print(f" Mensaje reconocido: {comando}")
            enviar_mensaje_whatsapp_instantaneo(comando)
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de voz: {e}")

# Bucle principal
while True:
    escuchar_comando()
    continuar = input("¿Deseas enviar otro mensaje? (s/n): ")
    if continuar.lower() != "s":
        print(" Finalizando sistema de envío de mensajes.")
        break
