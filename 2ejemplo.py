# Clase para representar una actividad
class Actividad:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

# Función para seleccionar las actividades utilizando el algoritmo voraz
def seleccionar_actividades(actividades):
    # Ordenar las actividades por su hora de finalización
    actividades_ordenadas = sorted(actividades, key=lambda x: x.fin)
    
    actividades_seleccionadas = []  # Lista de actividades seleccionadas
    ultima_hora_fin = 0  # Variable para almacenar la hora de finalización de la última actividad seleccionada

    for actividad in actividades_ordenadas:
        if actividad.inicio >= ultima_hora_fin:
            # Si la actividad no se solapa con la última seleccionada, la añadimos
            actividades_seleccionadas.append(actividad)
            ultima_hora_fin = actividad.fin  # Actualizamos la hora de finalización

    return actividades_seleccionadas

# Ejemplo de uso
actividades = [
    Actividad(13, 15),  # Actividad 1: 1 PM - 3 PM
    Actividad(14, 17),  # Actividad 2: 2 PM - 5 PM
    Actividad(16, 19),  # Actividad 3: 4 PM - 7 PM
    Actividad(17, 21),  # Actividad 4: 5 PM - 9 PM
    Actividad(20, 22)   # Actividad 5: 8 PM - 10 PM
]

actividades_seleccionadas = seleccionar_actividades(actividades)

print("Actividades seleccionadas:")
for i, actividad in enumerate(actividades_seleccionadas, start=1):
    print(f"Actividad {i}: ({actividad.inicio} - {actividad.fin})")
