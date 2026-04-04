def nuevocontacto(agenda, nombre, telefono):
    agenda[nombre] = telefono

def buscarcontacto(agenda, nombre):
    if nombre in agenda:
        return agenda[nombre]
    return None

def eliminarcontacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]

agenda = {}

nuevocontacto(agenda, "Ana", "12345")
nuevocontacto(agenda, "Luis", "67890")

print(buscarcontacto(agenda, "Ana"))

eliminarcontacto(agenda, "Ana")

print(agenda)