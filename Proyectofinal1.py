import json

with open('data.json') as file:
    letras = json.load(file)

#print("Bienvenido al contactbook.\n1.Agregar contactos\n2.Buscar contactos\n3.Listar contactos\n4.Borrar contactos\n5.Llamar contactos\n6.Enviar mensaje a contactos\n7.Enviar correo a contactos\n8.Exportar contactos\n9.Salir\n")
#opcion = input("Elija una opcion: ")

print(letras)
