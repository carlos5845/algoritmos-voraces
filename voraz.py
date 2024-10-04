class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.valor_por_peso = valor / peso

def mochila_fraccionaria(objetos, capacidad_mochila):
    # Ordenar los objetos por valor por unidad de peso en orden descendente
    objetos_ordenados = sorted(objetos, key=lambda x: x.valor_por_peso, reverse=True)
    
    valor_total = 0  # Valor total que llevaremos en la mochila
    peso_actual = 0  # Peso total actual en la mochila

    for objeto in objetos_ordenados:
        if peso_actual + objeto.peso <= capacidad_mochila:
            # Si el objeto completo cabe en la mochila, lo llevamos
            peso_actual += objeto.peso
            valor_total += objeto.valor
        else:
            # Si no cabe todo el objeto, llevamos la fracción que pueda caber
            peso_restante = capacidad_mochila - peso_actual
            valor_total += objeto.valor_por_peso * peso_restante
            break  # Ya no podemos añadir más objetos, salimos del bucle

    return valor_total

# Ejemplo de uso
objetos = [
    Objeto(10, 60),  # Objeto 1: Peso = 10, Valor = 60
    Objeto(20, 100), # Objeto 2: Peso = 20, Valor = 100
    Objeto(40, 120)  # Objeto 3: Peso = 30, Valor = 120
]

capacidad_mochila = 50  # Capacidad máxima de la mochila en kg
valor_maximo = mochila_fraccionaria(objetos, capacidad_mochila)

print(f"El valor máximo que se puede obtener es: {valor_maximo}")
