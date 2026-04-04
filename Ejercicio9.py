def agrupar(lista):
    diccionario = {}
    for producto, categoria in lista:
        if categoria in diccionario:
            diccionario[categoria].append(producto)
        else:
            diccionario[categoria] = [producto]
    return diccionario

datos = [
    ("Manzana", "Fruta"),
    ("Pera", "Fruta"),
    ("Zanahoria", "Verdura"),
    ("Lechuga", "Verdura")
]

print(agrupar(datos))