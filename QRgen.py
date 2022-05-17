import qrcode
import random 
from colorama import Fore, Back, Style
import time as t

# Establecer el nombre del archivo totalmente random

may = "AEIOU"
num = "012345"
str = may + num
length = 5
random = "".join(random.sample(str,length))
total = random


# Banner

t.sleep(1)
print(Back.WHITE, Fore.BLACK + """
    ████████████████████████▀██████████████████████████████████████████████████
    █─▄▄▄─█▄─▄▄▀█▀▀▀▀▀██─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀██▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█
    █─██▀─██─▄─▄████████─██▄─██─▄█▀██─█▄▀─███─▄█▀██─▄─▄██─▀─████─███─██─██─▄─▄█
    ▀───▄▄▀▄▄▀▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀""")

print(Style.RESET_ALL) 

t.sleep(1)
print(Fore.RED + """
                                                        ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                                                        ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                                                        ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█

""")


# Seleccionar el contenido del QR 

print(Fore.GREEN + "Coloca el texto o el link que quieres introducir a tu QR")
contenido = input(Fore.GREEN + '> ')


# Crear el QR con el contenido 

img = qrcode.make(contenido)
type(img) 


# Guardar el QR en /qr/...

img.save('qr/' + total + '-QR.png')
print("""
""")
t.sleep(1.5)
print(Fore.GREEN + "'" + contenido + """' Se ha guardado en:

            /qr/""" + Fore.RED + total + '-QR.png')
print(" ", Style.RESET_ALL)