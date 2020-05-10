import json
import requests
import validators
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
letras = {}
for x in abecedario:
    letras[x] = {}
    names = []
resp = requests.get('http://demo7130536.mockable.io/contacts')
contactosjson = json.loads(resp.content)
for k in contactosjson:
    letras[k].update(contactosjson[k])
    for agregarnombres in contactosjson[k]:
            names.append(agregarnombres)
print("Bienvenido al contactbook.\n1.Agregar contactos\n2.Buscar contactos\n3.Listar contactos\n4.Borrar contactos\n5.Llamar contactos\n6.Enviar mensaje a contactos\n7.Enviar correo a contactos\n8.Exportar contactos\n9.Salir\n")
while(5):
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
            if validators.email(m) == True:
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
        while(11):
            usuario = input('Presione "enter" para salir...')
            if usuario == "":
                break
    def BuscarContacto():
        buscador = input("Buscar: ")
        print("")
        print("Resultados:")
        for u in names:
            if u.find(buscador) != -1:
                print(u)
        while(10):
            usuario2 = input('Presione "enter" para salir...')
            if usuario2 == "":
                break
    def ListarContacto():
        print("Listar Contacto")
        contador = 0
        for c in letras:
            separador = 0
            for h in letras[c]:               
                if len(h) >= 1 and separador == 0:
                    print("")
                    separador += 1
                    print(c + ":")
                if len(h) >= 1 and separador == 1:
                    contador += 1
                    print("     " + str(contador) + "." + " " + h)
        print("")
        print("---------------------------")
        numero = 0
        Vercontacto = input("Ver contacto: ")
        for i in range(contador):
            if Vercontacto == str(i+1) or Vercontacto == names[i]:
                print(names[i] + ":")
                print("     " + "telefono" + ":" + " " + "".join(map(str, letras[names[i][0]][names[i]]['telefono'])))
                print("     " + "email" + ":" + " " + "".join(map(str, letras[names[i][0]][names[i]]['email'])))
                print("     " + "company" + ":" + " " + letras[names[i][0]][names[i]]['company'])
                print("     " + "extra" + ":" + " " + letras[names[i][0]][names[i]]['extra'])
        while(19):
            usuario3 = input("Presione enter para salir...")
            if usuario3 == "":
                break          
    if opcion == '1':
        AgregarContactos()
    if opcion == '2':
        BuscarContacto()
    if opcion == '3':
        ListarContacto()



    








