#Ejercicio 2:
#a) Definí una función mensaje y usé un decorador para agregarle texto antes y después:

def decorador_saludo(funcion):
    def funcion_decorada():
        print("Hola")
        funcion()
        print("Chau")
    return funcion_decorada

@decorador_saludo
def mensaje():
    print("Esto es Programación Avanzada.")

# Llamada a la función decorada
mensaje()

#b) Hice un decorador que detecta si se intenta dividir por 0 y da un mensaje de advertencia:

def evitar_division_por_cero(funcion):
    def funcion_decorada(a, b):
        if b == 0:
            print("Error: No se puede dividir por 0.")
            return None
        return funcion(a, b)
    return funcion_decorada

@evitar_division_por_cero
def dividir(a, b):
    return a / b

# Pruebas
print(dividir(10, 2))  # Muestra 5.0
print(dividir(5, 0))   # Muestra mensaje de error


#c) Decorador que imprime fecha y hora (usando el módulo datetime):

from datetime import datetime

def imprimir_fecha_y_hora(funcion):
    def funcion_decorada(*args, **kwargs):
        print("Fecha y hora:", datetime.now())
        return funcion(*args, **kwargs)
    return funcion_decorada

@imprimir_fecha_y_hora
def saludar(nombre):
    print(f"Hola {nombre}")

# Prueba
saludar("Ana")

#i) ¿Cómo invocar a 2 decoradores a la vez?
#Se colocan uno debajo del otro, en el orden en que deben ejecutarse (de arriba hacia abajo):
@decorador1
@decorador2
def funcion():
    pass
#Primero se aplica decorador2, y luego su resultado pasa por decorador1.


#ii) ¿Cómo invocar a un decorador que está programado en otro archivo?
#Se guarda el decorador en otro archivo, por ejemplo mis_decoradores.py:

# mis_decoradores.py
def decorador_saludo(func):
    def decorada():
        print("Hola desde otro archivo")
        func()
    return decorada

#Luego se importa en el archivo principal:

from mis_decoradores import decorador_saludo

@decorador_saludo
def saludar():
    print("Función principal")

saludar()
