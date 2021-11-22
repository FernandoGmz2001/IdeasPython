from ctypes import string_at
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import pyautogui
import time
import sonido
from playsound import playsound
import pyttsx3
PATH="C:\Program Files (x86)\chromedriver.exe"

correo = input("Ingrese su correo: \n")
contraseña = input("Ingrese su Contraseña: \n")

driver  = webdriver.Chrome(PATH)
driver.get("https://siie.nlaredo.tecnm.mx/EvaluacionDocente/Encuesta/Index")
driver.find_element_by_name("Input.Email").send_keys(correo)
driver.find_element_by_name("Input.Password").send_keys(contraseña)

Asistente = pyttsx3.init('sapi5')
voces = Asistente.getProperty('voices') #voices es el nombre de la propiedad, no se puede modificar 
Asistente.setProperty('voices',voces[0].id)
Asistente.setProperty('rate',150)

def habla(audio):
    print(" ")
    Asistente.say(audio)
    print(f": {audio}")
    Asistente.runAndWait()

habla("Acontinuación se hará la captura de la posición del cursor. Ponga el cursor encima del botón de iniciar sesión. NO de click")
time.sleep(2)
sonido.function_sound()
print(pyautogui.position())
habla("Posición del mouse capturada")
IniciarSesion = pyautogui.position()
pyautogui.click(IniciarSesion)

habla("Acontinuación se hará la captura del botón de siguiente pregunta. Ponga el cursor encima del botón de siguiente pregunta. NO de click")
time.sleep(2)
sonido.function_sound()
print(pyautogui.position())
habla("Posición del mouse capturada")
SiguientePregunta = pyautogui.position()
pyautogui.click(SiguientePregunta)

