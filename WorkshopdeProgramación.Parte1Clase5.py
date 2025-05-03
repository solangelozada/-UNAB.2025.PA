#2. Pilares de la POO

#Pregunta teórica:

#Los cuatro pilares de la POO son:

#-Abstracción: Ocultar los detalles complejos de implementación y mostrar solo lo esencial. Permite simplificar la interfaz de un objeto.

#-Encapsulamiento: Proteger los atributos y métodos de una clase de accesos directos desde fuera de la clase. Utiliza modificadores de acceso como private, protected o convenciones en Python (uso de _ o __).

#-Herencia: Permite crear nuevas clases a partir de clases existentes, reutilizando y extendiendo sus funcionalidades. Las clases hijas heredan atributos y métodos de las clases padres.

#-Polimorfismo: Permite que diferentes clases implementen el mismo método de manera diferente. Las subclases pueden sobrescribir métodos de la clase base.

#Mini autoevaluación
#1. ¿Cuál es la diferencia entre encapsulamiento y abstracción?

#Encapsulamiento se refiere a ocultar los detalles internos de los objetos y restringir el acceso directo a sus atributos y métodos.

#Abstracción implica ocultar la complejidad del sistema y exponer solo la interfaz esencial para interactuar con el objeto.

#2. ¿Qué pilar permite a las subclases sobrescribir métodos?

#Polimorfismo permite a las subclases sobrescribir métodos de la clase base para proporcionar implementaciones específicas.


#Código con errores para corregir

class Dog:
    def __init__(self, name):
        name = name
    def speak(self):
        return "woof"

dog = Dog("Bobby")
print(dog.name)

#Errores:

#El atributo name no se asigna correctamente a self.name en el constructor, por lo que no está disponible como atributo de la clase.

#Debemos usar self.name para almacenar el valor de name como atributo de la clase.

#Código corregido:

class Dog:
    def __init__(self, name):
        self.name = name  # Se debe asignar el nombre a un atributo de instancia
    def speak(self):
        return "woof"

dog = Dog("Bobby")
print(dog.name)  # Ahora imprime correctamente "Bobby"


#Ejercicio práctico: Jerarquía simple de vehículos
#Defino una jerarquía simple para vehículos con una clase base y dos clases hijas:

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def info(self):
        return f"Vehículo de marca: {self.marca}"

# Clase hija Coche
class Coche(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def info(self):
        return f"Coche {self.marca} con {self.puertas} puertas."

# Clase hija Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, cilindrada):
        super().__init__(marca)
        self.cilindrada = cilindrada

    def info(self):
        return f"Motocicleta {self.marca} con {self.cilindrada} cc."

# Función que recibe un vehículo y llama a su método info()
def mostrar_info_vehiculo(vehiculo):
    print(vehiculo.info())

# Prueba con objetos de cada clase
coche = Coche("Ford", 4)
motocicleta = Motocicleta("Yamaha", 600)

mostrar_info_vehiculo(coche)         # Coche Ford con 4 puertas.
mostrar_info_vehiculo(motocicleta)   # Motocicleta Yamaha con 600 cc.


#Reflexión individual
#¿Qué pilar sentís que dominás mejor? ¿Cuál te cuesta más aplicar en la práctica?
#A mí, personalmente, la herencia me parece más fácil de aplicar, ya que me permite reutilizar código y extender funcionalidades de manera clara. Lo que más me cuesta a veces es el polimorfismo, ya que implica que las subclases redefinan métodos de una manera correcta y consistente.

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


