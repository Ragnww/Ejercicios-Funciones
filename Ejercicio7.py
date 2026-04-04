def convertirnotas(estudiantes):
    rangos = [
        (4.5, "A"),
        (4.0, "B"),
        (3.0, "C"),
        (2.0, "D"),
        (0, "F")
    ]

    reporte = []

    for nombre, nota in estudiantes:
        for limite, letra in rangos:
            if nota >= limite:
                reporte.append((nombre, nota, letra))
                break

    return reporte

estudiantes = [
    ("Sebastian", 4.7),
    ("Diego", 3.8),
    ("Santiago", 2.9),
    ("Wilson", 1.5)
]

print(convertirnotas(estudiantes))