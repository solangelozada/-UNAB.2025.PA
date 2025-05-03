#1) Verdadero o Falso:
 #a) El acoplamiento bajo favorece que una clase se pueda reutilizar con menos dependencias. (VERDADERO)
 #b) La encapsulación impide el acceso a los atributos de una clase desde fuera de sus métodos.(VERDADERO)
 #c) type(objeto) devuelve la clase a la que pertenece objeto.(VERDADERO)
 #d) La abstracción consiste en ocultar la complejidad interna y mostrar solo lo esencial.(VERDADERO)

#2) Herencia simple
#Define en Python dos clases:
#- Vehiculo: con atributo marca (string) y método info() que devuelve "Vehículo: <marca>".
#- Coche: hereda de Vehiculo, añade atributo pasajeros (int) y redefine info() para devolver
#"Coche: <marca>, pasajeros: <pasajeros>"

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def info(self):
        return f"Vehículo: {self.marca}"
      
class Coche(Vehiculo):
    def __init__(self, marca, pasajeros):
        super().__init__(marca)  # Llamo al constructor de Vehiculo
        self.pasajeros = pasajeros

    def info(self):
        return f"Coche: {self.marca}, pasajeros: {self.pasajeros}"
v = Vehiculo("Toyota")
print(v.info())  # Vehículo: Toyota

c = Coche("Ford", 5)
print(c.info())  # Coche: Ford, pasajeros: 5


#3) Decoradores básicos
   #a) Explica en 1–2 líneas qué es un decorador en Python.
   #b)escribe un decordor anunciar que imprima "Ejecutando funcion..." antes de llamar a la
  #función decorada y luego retorne su resultado. Aplica @anunciar a sumar(a, b).

#a) Explicación:
#Un decorador en Python es una función que recibe otra función como argumento y la modifica o extiende su comportamiento sin cambiar su código original.

 #b)escribe un decordor anunciar que imprima "Ejecutando funcion..." antes de llamar a la
  #función decorada y luego retorne su resultado. Aplica @anunciar a sumar(a, b).
# Defino el decorador anunciar

def anunciar(func):
    def funcion_decorada(*args, **kwargs):
        print("Ejecutando función...")
        return func(*args, **kwargs)
    return funcion_decorada

# Aplico el decorador @anunciar a la función sumar
@anunciar
def sumar(a, b):
    return a + b

# Prueba
print(sumar(3, 4))  # Ejecutando función... 7



