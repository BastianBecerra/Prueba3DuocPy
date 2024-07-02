# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----

user = {}
menu = ["Revisar menú",
        "Revisar carrito",
        "Buscar ingrediente",
        "Modificar ítem del menú",
        "Pagar"
        "Salir"]

#Acciones iniciales
preguntas = []
nombreUsuario = str(input("Cual es su Nombre?: "))
comidaFav = str(input("Cual es tu comida favorita?: "))
alergias = [str(input("Tienes alguna alergia? (dinos cual): "))]

for x in preguntas:
   x = nombreUsuario.append(preguntas)
   x = comidaFav.append(preguntas)
   x = alergias.append(preguntas)

print(preguntas)  # Se que me falto algo aui porque al momento de dhacer append no se guardo en ningun lado otra vez los nervios me ganaron.


#menu principal
while (True):
    for listita, opcion in enumerate(menu):
        print(f"{listita+1}:{opcion}")
    
    while True:
        MenuAccion = int(input("Ingrese la acción a realizar: "))
        seleccion = menu[MenuAccion-1]
        break

    print(seleccion)

    if MenuAccion == 1:
        revisaMenu(var)

    if MenuAccion == 2:
        if carrito:
            print(carrito)
        else:
            print("No se ah agregado ningun Producto")

    if MenuAccion == 3:
        while True:

            ingrediente = input("Ingrese el ingrediente para buscar: ").lower()
            buscaIngrediente(var,ingrediente)

            opcion = input("Quiere buscar otro ingrediente? (si/no): ").lower()

            if opcion == "si":
                continue
            if opcion == "no":
                break
            
    if MenuAccion == 4:

        for i, elementos in enumerate(var):
            print(f"{i+1} , {elementos}\n")

        contraseña = input("Ingrese la contraseña: ")

        if check_password(contraseña):
            id = int(input("Ingrese el id del producto: "))

            select = input("Ingrese que desea modificar (nombre,precio,kcal,ingredientes): ")

            producto = var[id-1]

            if select in producto.keys():
                modificar = input("Ingrese nuevo dato para modificar: ")
                producto[select] = modificar

        print(var)

    if MenuAccion == 5:
        pagar(var)

    if MenuAccion == 6:
        print("Adios!!!!")
        break