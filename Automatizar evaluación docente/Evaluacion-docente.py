import pyautogui
import time
import pyttsx3
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from playsound import playsound
#pip install -Iv playsound==1.2.2

def sonidos():
    playsound('D:\\Documentos\\Proyectos python\\SonidoIDA.mp3')

sonidos()
Asistente = pyttsx3.init('sapi5')
voces = Asistente.getProperty('voices') #voices es el nombre de la propiedad, no se puede modificar 
Asistente.setProperty('voices',voces[0].id)
Asistente.setProperty('rate',150)
def habla(audio):
    print(" ")
    Asistente.say(audio)
    print(f": {audio}")
    Asistente.runAndWait()


PATH="C:\Program Files (x86)\chromedriver.exe"

i=0
preguntas=0
botonSiguientePregunta=0
# correo="l19100196@nlaredo.tecnm.mx"
# contraseña="GODB.MMRa7"
correo = input("Ingrese su correo: \n")
if(correo==""):
    while(correo==""):
        print("No puede dejar este campo vacío")
        correo = input("Ingrese su correo: \n")
contraseña = input("Ingrese su Contraseña: \n")
if(contraseña==""):
    while(contraseña==""):
        print("No puede dejar este campo vacío")
        contraseña = input("Ingrese su contraseña: \n")
preguntas = int(input("Ingrese el número de preguntas que hay: \n"))
Continuar =""
driver  = webdriver.Chrome(PATH)
driver.get("https://siie.nlaredo.tecnm.mx/EvaluacionDocente/Encuesta/Index")
driver.find_element_by_name("Input.Email").send_keys(correo)
driver.find_element_by_name("Input.Password").send_keys(contraseña)
habla("A continuación se hará la captura de la posición del cursor. Ponga el cursor encima del botón de iniciar sesión. NO de click, ni mueva el cursor aunque haya terminado la captura")
sonidos()
print(pyautogui.position())
habla("Posición del mouse capturada")
IniciarSesion = pyautogui.position()
pyautogui.click(IniciarSesion)


while(i!=preguntas):
    i+=1
    pyautogui.scroll(1000)
    select = Select(driver.find_element_by_name("respuesta[0].valor"))
    select.select_by_visible_text('De acuerdo')
    select.select_by_value('4')
    select = Select(driver.find_element_by_name("respuesta[1].valor"))
    select.select_by_visible_text('De acuerdo')
    select.select_by_value('4')
    select = Select(driver.find_element_by_name("respuesta[2].valor"))
    select.select_by_visible_text('De acuerdo')
    select.select_by_value('4')
    select = Select(driver.find_element_by_name("respuesta[3].valor"))
    select.select_by_visible_text('De acuerdo')
    select.select_by_value('4')
    select = Select(driver.find_element_by_name("respuesta[4].valor"))
    select.select_by_visible_text('De acuerdo')
    select.select_by_value('4')
    select = Select(driver.find_element_by_name("respuesta[5].valor"))
    select.select_by_visible_text('De acuerdo')
    select.select_by_value('4')
    select = Select(driver.find_element_by_name("respuesta[6].valor"))
    select.select_by_visible_text('De acuerdo')
    time.sleep(1)
    if(botonSiguientePregunta<1):
        botonSiguientePregunta+=1
        habla("Acontinuación se hará la captura del botón de siguiente pregunta. Ponga el cursor encima del botón de siguiente pregunta. NO de click , ni mueva el cursor")
        sonidos()
        print(pyautogui.position())
        habla("Posición del mouse capturada")
        SiguientePregunta = pyautogui.position()
        pyautogui.click(SiguientePregunta)
        time.sleep(1)
    else:
        pyautogui.click(SiguientePregunta)
        time.sleep(1)

# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
# select = Select(driver.find_element_by_name("respuesta[0].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[1].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[2].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[3].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[4].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[5].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# select = Select(driver.find_element_by_name("respuesta[6].valor"))
# select.select_by_visible_text('De acuerdo')
# select.select_by_value('4')
# time.sleep(1)
# pyautogui.click(1205,603)
# confirmar = pyautogui.scroll(1000)
    