#!/usr/bin/python
#-*- coding: iso-8859-1 -*-
#SimpleScript 12/07/2018
import os
import time
# Version
os.system("clear")
print ("\033[1;33mCREATED BY: Real Strategy\033[0m")
print ("\033[1;32mVERSION: cc-genpro1.2 \033[0m")
print ("\033[1;32mModificado por: PowerMX \033[0m")
os.system("neofetch")
print ("")
## Show menu ##
print (30 * '-') 
print ("\033[1;32mGENERADOR DE BIN RS\033[0m") 
print (30 * '-') 
print ("\033[1;33m1.\033[1;36mGenerar bin\033[0m") 
print ("\033[1;33m2.\033[1;36mGuardar bins en texto\033[0m") 
print ("\033[1;33m3.\033[1;36mGenerador de correo temporal\033[0m")
print ("\033[1;33m4.\033[1;36mBin Checker\033[0m")
print ("\033[1;33m5.\033[1;36mVer bin guardados\033[0m")
print ("\033[1;33m6.\033[1;36mCreditos al creador\033[0m")
print ("\033[1;33m7.\033[1;36mInformacion\033[0m")
print ("\033[1;33m8.\033[1;31mSalir...!!\033[0m")
print (30 * '-')
 
## Get input ###
choice = raw_input('\033[1;33mingresa tu opcion: \033[0m')
 
### Convert string to int type ##
choice = int(choice)
 
### Take action as per selected menu-option ###
if choice == 1:
        print ("Generador bin validos...") 
        os.system("python2 cc-genpro.py")
        time.sleep(3)

elif choice == 2:
    os.system("clear")
    os.system("bash guardar")

elif choice == 3:
        os.system("clear")
        print("Ingresando al generador de correo temporal")
        print("Inicie una nueva ventana para usar el generador")
        print("para salir del navegador digite [ Q ] ")
        time.sleep(5)
        os.system("w3m https://temp-mail.org/es/")
elif choice == 4:
         os.system("python2 checker")
elif choice == 5:
         os.system("cat BinGuardados.txt")

elif choice == 6:
         os.system("clear")
         os.system("bash creditos")
         time.sleep(8)
         os.system("python2 cc-genpro1.2.py")
elif choice == 7:
         print ("")
         print ("MENSAJE: Este es un simple script para generar bins y ahorrar tiempo al momento de binear en el navegador.")
         
elif choice == 8:
          exit ()
else: 
## default ##
        print ("Opcion invalida...Sigue intentando")
