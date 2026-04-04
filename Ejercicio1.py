def promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def alta(notas):
    mayor = notas[0]
    for nota in notas:
        if nota > mayor:
            mayor = nota
    return mayor

def baja(notas):
    menor = notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor

notas = [3.5, 4.2, 2.8, 5.0, 4.7]

print(promedio(notas))
print(alta(notas))
print(baja(notas))