def votos(lista, candidatos):
    conteo = {}
    invalidos = 0

    for candidato in candidatos:
        conteo[candidato] = 0

    for voto in lista:
        if voto in conteo:
            conteo[voto] += 1
        else:
            invalidos += 1

    total = 0
    for c in conteo:
        total += conteo[c]

    ganador = ""
    mayor = -1

    for c in conteo:
        if conteo[c] > mayor:
            mayor = conteo[c]
            ganador = c

    porcentaje = (mayor * 100) / total

    return conteo, invalidos, ganador, porcentaje

candidatos = ["Ana", "Luis", "Carlos"]
lista = ["Ana", "Luis", "Ana", "Pedro", "Carlos", "Ana"]

print(votos(lista, candidatos))
