import json
import requests
import validators
import pandas as pd
import os
from win10toast import ToastNotifier
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
letras = {}
for x in abecedario:
    letras[x] = {}
    names = []
resp = requests.get('http://demo7130536.mockable.io/final-contacts-100')
contactosjson = json.loads(resp.content)
for k in contactosjson:
    letras[k].update(contactosjson[k])
    for agregarnombres in contactosjson[k]:
            names.append(agregarnombres)
toaster = ToastNotifier()
while(5):
    print("Bienvenido al contactbook.\n1.Agregar contactos\n2.Buscar contactos\n3.Listar contactos\n4.Borrar contactos\n5.Llamar contactos\n6.Enviar mensaje a contactos\n7.Enviar correo a contactos\n8.Exportar contactos\n9.Salir\n")
    names.sort()
    opcion = input("Elija una opcion: ")
    def AgregarContactos():
        nombres = {}
        while (1):
            nombre = input("Introduzca nombre: ")
            if ' ' in nombre:
                if len(nombre.split()) == 2:
                    nombre = nombre.title()
                    nombres[nombre] = {}
                    break
                else:
                    print("Nombre no valido")
            else:
                print("Nombre no valido")
        numero = {}
        numero['telefono'] = []
        while(2):   
            x = input("Introduzca numero: ")
            if x.isdigit() == True:
                numero['telefono'].append({x})
                Otro = input("Desea ingresar otro numero? (y/n): ")
                if Otro == 'n':
                    break
            else:
                print("Numero no valido")
        nombres[nombre].update(numero)
        email = {}
        email['email'] = []
        while(3):
            m = input("Introduzca su email: ")
            veremail = m.split('@')
            if (validators.email(m) == True) and (validators.domain(veremail[1])):
                email['email'].append({m})
                em = input("Desea ingresar otro email? (y/n): ")
                if em == 'n':
                    break
            else:
                print("Correo incorrecto ingrese uno valido.")
        nombres[nombre].update(email)      
        empresa = input("Escriba la empresa del contacto: ")
        demas = {}
        company = {}
        company['company'] = empresa
        extra = input("Escriba algo extra que quiera agregar: ")
        demas['extra'] = extra
        nombres[nombre].update(company)
        nombres[nombre].update(demas)
        names.append(nombre)
        for q in abecedario:
            if q == nombre[0]:
                letras[q].update(nombres)
                toaster.show_toast("Contacto Guardado \U0001F601", "Puedes verlo en 'Listar contactos'",duration=3)
        while(11):
            usuario = input('Presione "enter" para salir...')
            if usuario == "":
                break
    def BuscarContacto():
        salida = True
        while(salida == True):
            sumar = 0
            buscador = input("Buscar: ")
            print("")
            print("Resultados:")
            if names:
                for u in names:
                    if u.find(buscador) != -1:
                        print(u)
                        sumar += 1
                if sumar == 0:
                    toaster.show_toast("Atencion:","Sin resultados \U0001F61E",duration=3)
            else:
                toaster.show_toast("Atencion:","No hay contactos \U0001F610",duration=3)
            while (1):
                usuario = input("Presione enter para salir: ")
                if usuario == "":
                    salida = False
                    break 
    def ListarContacto():
        print("Listar Contacto")
        salida = True
        while salida == True:
            contador = 0
            sacar = 0
            sumador = 0
            for c in letras:
                separador = 0
                for h in letras[c]:               
                    if len(h) >= 1 and separador == 0:
                        print("")
                        separador += 1
                        print(c + ":")
                    if len(h) >= 1 and separador == 1:
                        contador += 1
                        print("     " + str(contador) + "." + " " + names[contador-1])
            print("")
            print("---------------------------")
            Vercontacto = input("Ver contacto: ")
            contar = 0
            telefonos = []
            ems = []
            contaremail = 0
            if contador == 0:
                contador += 1
                sacar += 1
            for i in range(contador):
                if sacar == 1:
                    toaster.show_toast("Atencion:","No hay contactos \U0001F610",duration=3)
                    sumador +=1
                    break
                if Vercontacto == str(i+1) or Vercontacto == names[i]:
                    x = "".join(map(str, letras[names[i][0]][names[i]]['telefono']))
                    em = "".join(map(str, letras[names[i][0]][names[i]]['email']))
                    for y in range(len(x.split("}" + "{"))):
                        contar += 1
                    for y in range(len(em.split("}" + "{"))):
                        contaremail += 1
                    if contar == 1 and contaremail == 1:
                        if type(letras[names[i][0]][names[i]]['telefono'][0]) == set and type(letras[names[i][0]][names[i]]['email'][0]) == set:
                            for tel in letras[names[i][0]][names[i]]['telefono'][0]:
                                telefonos.append(tel)
                            for tel in letras[names[i][0]][names[i]]['email'][0]:
                                ems.append(tel)
                            print(names[i] + ":")
                            print("     " + "telefono" + ":" + " " + "".join(map(str, telefonos)))
                            print("     " + "email" + ":" + " " + "".join(map(str, ems)))
                            print("     " + "company" + ":" + " " + letras[names[i][0]][names[i]]['company'])
                            print("     " + "extra" + ":" + " " + letras[names[i][0]][names[i]]['extra'])
                            sumador +=1
                            break
                        else: 
                            print(names[i] + ":")
                            print("     " + "telefono" + ":" + " " + "".join(map(str, letras[names[i][0]][names[i]]['telefono'])))
                            print("     " + "email" + ":" + " " + "".join(map(str, letras[names[i][0]][names[i]]['email'])))
                            print("     " + "company" + ":" + " " + letras[names[i][0]][names[i]]['company'])
                            print("     " + "extra" + ":" + " " + letras[names[i][0]][names[i]]['extra'])
                            sumador +=1
                            break
                    else:
                        if contar == 1:
                            print(names[i] + ":")
                            for tel in letras[names[i][0]][names[i]]['telefono'][0]:
                                print("     " + "telefono" + ":" + " " + tel)
                            print("     " + "email" + ":" + " ", end="")
                            for y in range(contaremail):
                                for tel in letras[names[i][0]][names[i]]['email'][y]:
                                    ems.append(tel)
                            print(ems[0], end='')
                            for m in range(contaremail-1):
                                print(", ", end='')
                                print(ems[m+1], end='')
                            print("\n", end='')
                            print("     " + "company" + ":" + " " + letras[names[i][0]][names[i]]['company'])
                            print("     " + "extra" + ":" + " " + letras[names[i][0]][names[i]]['extra'])
                            sumador +=1
                            break
                        print(names[i] + ":")
                        print("     " + "telefono" + ":" + " ", end="")
                        for y in range(contar):
                            for tel in letras[names[i][0]][names[i]]['telefono'][y]:                           
                                telefonos.append(tel)
                        print(telefonos[0], end='')
                        for m in range(contar-1):
                            print(", ", end='')
                            print(telefonos[m+1], end='')
                        print("\n", end='')
                        if contaremail == 1:
                            for tel in letras[names[i][0]][names[i]]['email'][0]:
                                print("     " + "email" + ":" + " " + tel)
                            print("     " + "company" + ":" + " " + letras[names[i][0]][names[i]]['company'])
                            print("     " + "extra" + ":" + " " + letras[names[i][0]][names[i]]['extra'])
                            sumador+=1
                            break
                        else:
                            print("     " + "email" + ":" + " ", end="")
                            for y in range(contaremail):
                                for emal in letras[names[i][0]][names[i]]['email'][y]:
                                    ems.append(emal)
                            print(ems[0], end='')
                            for m in range(contaremail-1):
                                print(", ", end='')
                                print(ems[m+1], end='')
                            print("\n", end='')
                            print("     " + "company" + ":" + " " + letras[names[i][0]][names[i]]['company'])                
                            print("     " + "extra" + ":" + " " + letras[names[i][0]][names[i]]['extra'])
                            sumador+=1
                            break
            if sumador == 0:
                toaster.show_toast("Atencion:","Inserte un nombre o numero valido \U0001F620",duration=3)
            while (sumador == 1):
                    usuario = input("Presione enter para salir: ")
                    if usuario == "":
                        sumador = 0
                        salida = False
                        break


    


            

    








