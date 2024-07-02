"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------
carrito = []

def revisaMenu(listaMenu):
    for producto in listaMenu:
        print(f"Producto = {producto['nombre']} -> Precio = {producto['precio']}") 
    while True:
        select = input("Desea agregar un Producto? (si/no): ").lower()
        if select == "si":
            i = input("Seleccione Producto al carrito: ").lower()
            for elemento in listaMenu:
                if i in elemento.values():
                    carrito.append(elemento)
        if select == "no":
            break

def buscaIngrediente(listaCarrito,ingrediente):
    for comida in listaCarrito:
        ingred = comida["ingredientes"]
        if ingrediente in ingred:
            print(comida)

def pagar(listaCarrito):
    for pago in listaCarrito:
        precio = pago['precio']
        print(f"{precio}")