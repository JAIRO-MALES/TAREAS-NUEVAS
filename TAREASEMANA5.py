# Programa para calcular el área de un círculo

def calcular_area_circulo(radio):
    pi = 3.1416              # float
    area = pi * radio ** 2   # float
    return area


# Datos de entrada
nombre_usuario = "Tarea Semana 5"   # string
radio_circulo = 10               # integer
es_radio_valido = radio_circulo > 0  # boolean

# Proceso y salida
if es_radio_valido:
    area_circulo = calcular_area_circulo(radio_circulo)
    print("Hola,", nombre_usuario)
    print("Radio del circulo", radio_circulo)
    print("El área del círculo es:", area_circulo)
else:
    print("El radio ingresado no es válido")

#integer: radio_circulo

#float: pi, area_circulo

#string: nombre_usuario

#boolean: es_radio_valido