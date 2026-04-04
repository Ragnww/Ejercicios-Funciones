def funtemperaturas(datos):
    ciudad_max = ""
    ciudad_min = ""
    temp_max = None
    temp_min = None

    for ciudad in datos:
        for temp in datos[ciudad]:
            if temp_max is None or temp > temp_max:
                temp_max = temp
                ciudad_max = ciudad
            if temp_min is None or temp < temp_min:
                temp_min = temp
                ciudad_min = ciudad

    return (ciudad_max, temp_max), (ciudad_min, temp_min)

temperaturas = {
    "Bogota": [18, 20, 17, 19, 21],
    "Medellin": [28, 30, 27, 29, 31],
    "Cali": [32, 33, 31, 34, 35]
}

print(funtemperaturas(temperaturas))