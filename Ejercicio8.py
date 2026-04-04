def agregar(carrito, nombre, precio):
    carrito.append((nombre, precio))

def descuento(carrito, porcentaje):
    resultado = []
    for nombre, precio in carrito:
        precio = precio - (precio * porcentaje / 100)
        resultado.append((nombre, precio))
    return resultado

def total(carrito):
    suma = 0
    for nombre, precio in carrito:
        suma += precio
    return suma

carrito = []

agregar(carrito, "Camisa", 50000)
agregar(carrito, "Pantalon", 80000)

carrito = descuento(carrito, 10)

print(total(carrito))