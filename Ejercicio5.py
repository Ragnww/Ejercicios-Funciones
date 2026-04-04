def contar(palabras):
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]

print(contar(palabras))