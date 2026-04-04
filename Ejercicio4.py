def valortotal(inventario):
    total = 0
    for producto in inventario:
        nombre, precio, cantidad = producto
        total += precio * cantidad
    return total

inventario = [
    ("Laptop", 2500, 2),
    ("Mouse", 50, 10),
    ("Teclado", 100, 5)
]

print(valortotal(inventario))