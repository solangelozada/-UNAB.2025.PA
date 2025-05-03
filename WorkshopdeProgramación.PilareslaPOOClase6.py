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

