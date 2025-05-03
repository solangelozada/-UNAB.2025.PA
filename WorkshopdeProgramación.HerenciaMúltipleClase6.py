#4. Herencia Múltiple
#Pregunta teórica:
#¿Qué es la herencia múltiple y qué problema puede generar en lenguajes como Python?
#La herencia múltiple ocurre cuando una clase hereda de dos o más clases al mismo tiempo.
#En Python esto es posible, pero puede generar conflictos si las clases base tienen métodos con el mismo nombre.
#Uno de los principales problemas es el orden en que Python decide qué método ejecutar: esto se resuelve mediante el MRO (Method Resolution Order).

#Mini autoevaluación
#1. ¿Qué es el orden de resolución de métodos (MRO)?
#Es el orden en el que Python busca los métodos y atributos en las clases cuando hay herencia múltiple. Se puede ver con Clase.__mro__ o help(Clase).
#2. ¿Qué conflicto puede surgir si dos clases tienen el mismo método y una clase hereda de ambas?
#El conflicto es que Python puede encontrar dos versiones distintas del mismo método. En ese caso, se usará el método según el orden que define el MRO.

#Código con errores para corregir:
class A:
    def greet(self):
        print("Hi from A")

class B:
    def greet(self):
        print("Hi from B")

class C(A, B):
    pass

obj = C()
obj.greet()

#Imprime "Hi from A" porque la clase C hereda primero de A, así que Python busca el método greet en A antes que en B.
#Modificar el orden de herencia para cambiar el resultado:

class C(B, A):  # Se cambia el orden de herencia
    pass

obj = C()
obj.greet()  # Ahora imprime "Hi from B"

#Ejercicio práctico

class Walker:
    def walk(self):
        print("Caminando...")

class Runner:
    def run(self):
        print("Corriendo...")

class Athlete(Walker, Runner):
    pass

deportista = Athlete()
deportista.walk()
deportista.run()

#Resultado:

Caminando...
Corriendo...

#Ahora, si ambas clases tienen un método con el mismo nombre:

class Walker:
    def action(self):
        print("Camina rápido.")

class Runner:
    def action(self):
        print("Corre rápido.")

class Athlete(Walker, Runner):
    pass

a = Athlete()
a.action()  # Se ejecuta el de Walker por el MRO


 #Reflexión individual
#Usaría herencia múltiple cuando quiero combinar comportamientos de distintas clases reutilizables, como por ejemplo clases de mezcla (Mixins).
#Pero prefiero usar composición cuando las clases tienen responsabilidades muy distintas o si quiero evitar problemas de MRO. Me parece más limpio y flexible para mantener el código a largo plazo.


