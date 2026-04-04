def Est_aprobados(lista):
    aprobados = []
    for nombre, nota in lista:
        if nota >= 3.0:
            aprobados.append((nombre, nota))
    return aprobados

estudiantes = [("Ivan", 3.5), ("Tomas", 2.8), ("Julian", 4.0), ("Deiber Yoan", 2.9)]

print(Est_aprobados(estudiantes))