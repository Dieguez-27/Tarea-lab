#Introducción a la programación Seccción 17
#Fecha de creación del programa: 26/10/2023
#Autor: Sofia Diéguez
#Objetivo: Mostrar la administración de una lista de contactos
#Entrada: Ingresar el nombre y numero telefonico del contacto
""""
Proceso principal
1. Declarar una variable tipo lista
2. Pedirle al usuario que ingrese la cantidad de contactos con sus nombres y números de teléfono que desea agregar a la lista
3. Mostrar en pantalla la lista de contactos final
4. Darle la opcion al usuario de poder eliminar cualquier contacto 
5. Ordenar la lista en orden alfabetico
6. Se verá la lista de conctactos actualizada
7. Crear una copua de la lista de contactos originaly en orden alfabetico 
8. Dar solución
"""
#Salida
ListadeContactos = []
no = int(input("Ingrese la cantidad de contactos deseados para agregar: "))

for i in range(no):
    Nombre = input("Ingrese nombre del contacto: ")
    Número = input("Ingrese número de teléfono del contacto: ")
Contacto = [Nombre, Número]
ListadeContactos.append(Contacto)

print("Lista de contactos: ")
for contacto in ListadeContactos:
    print(contacto)

eliminarnom = input("Ingrese nombre del contacto que se desea eliminar: ")
for contacto in ListadeContactos:
    if contacto[0] == eliminarnom:
        ListadeContactos.remove(contacto)
        break

print("Lista de contactos actualizada:")
for contacto in ListadeContactos:
    print(contacto)
ListadeContactos.sort()

nuevonom = input("Ingrese el nombre de su nuevo contacto en mayúsculas: ")
nuevonum = input("Ingrese el número de teléfono del nuevo contacto: ")
newcontacto = [nuevonom.upper(), nuevonum]
ListadeContactos.append(newcontacto)

print("Lista de contactos en orden alfabéticamente:")
for contacto in ListadeContactos:
    print(contacto)

lugar = int(input("Ingrese la posición donde desea agregar un nuevo contacto: "))
nombrenue = input("Ingrese el nombre del nuevo contacto: ")
numeronue = input("Ingrese el número de teléfono del nuevo contacto: ")
contactonue = [nombrenue, numeronue]
ListadeContactos.insert(lugar, contactonue)

print("Lista de contactos completa:")
for contacto in ListadeContactos:
    print(contacto)

lista = ListadeContactos.copy()
lista.sort(reverse=True)

print("Lista ordenada de forma descendente:")
for contacto in lista:
    print(contacto)

print("Lista original:")
for contacto in ListadeContactos:
   print(contacto)
