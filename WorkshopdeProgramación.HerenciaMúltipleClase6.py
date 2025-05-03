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


#5. Metaclases

#Pregunta teórica
#Una metaclase en Python es una "clase de clases", es decir, define cómo se crean las clases.
#A diferencia de una clase común (que crea objetos), una metaclase crea clases.
#Permiten modificar o agregar automáticamente comportamientos a clases en el momento de su creación.

#Mini autoevaluación
#1. ¿Qué es una metaclase y cuándo se ejecuta?
#Es una clase que define cómo se construyen otras clases. Se ejecuta antes de que la clase sea creada, y controla su creación.

#2. ¿Qué diferencia hay entre __new__ y __init__?
#__new__ crea el objeto (en este caso, la clase), mientras que __init__ lo inicializa.
#En metaclases, si queremos modificar la clase antes de que se cree, usamos __new__.

#Código con errores para corregir:
class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.added = True

class MyClass(metaclass=Meta):
    pass

print(MyClass.added)

#Corrección con __new__:
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['added'] = True
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.added)  # Imprime: True

#Ejercicio práctico
#Metaclase que agrega automáticamente un método describe():

class AutoDescribe(type):
    def __new__(cls, name, bases, dct):
        def describe(self):
            print(f"Soy una instancia de la clase {self.__class__.__name__}")
        dct['describe'] = describe
        return super().__new__(cls, name, bases, dct)

class Persona(metaclass=AutoDescribe):
    pass

p = Persona()
p.describe()  # Imprime: Soy una instancia de la clase Persona

#Reflexión individual
#Al principio me pareció confuso el uso de metaclases, sobre todo por __new__, pero después entendí que sirven para agregar funciones o atributos automáticamente sin tener que repetir el código.
#Me parece útil cuando se quieren definir reglas comunes para muchas clases, aunque en la mayoría de los casos prefiero usar herencia o decoradores si el problema se puede resolver con algo más simple.


#6. Decoradores

#Pregunta teórica
#¿Qué es un decorador en Python y para qué se utiliza comúnmente?
#Un decorador en Python es una función que recibe otra función como argumento y devuelve una nueva función con comportamiento modificado.
#Se usan comúnmente para añadir funcionalidades (como validación, logging, autorización) sin tener que modificar el código original de la función decorada.

 #Mini autoevaluación

#1. ¿Cómo se aplica a una función?
#Se usa el símbolo @ encima de la función:
#@mi_decorador
#Esto es equivalente a: mi_función = mi_decorador(mi_función)

#2. ¿Qué función interna suele tener un decorador?
#Un decorador normalmente tiene una función interna o wrapper que encapsula y ejecuta la función original, agregando lógica adicional antes o después.

#Código con errores para corregir
#Código original:
def decorator(func):
    print("Decorating...")
    return func

@decorator
def greet():
    print("Hi!")

greet()

#Corrección con wrapper:
def decorator(func):
    def wrapper():
        print("Decorating...")
        func()
    return wrapper

@decorator
def greet():
    print("Hi!")

greet()

#Salida:
Decorating...
Hi!

Ejercicio práctico: @authorize
def authorize(func):
    def wrapper(user, *args, **kwargs):
        if getattr(user, 'is_admin', False):
            return func(user, *args, **kwargs)
        else:
            print("Acceso denegado")
    return wrapper

class Usuario:
    def __init__(self, nombre, is_admin=False):
        self.nombre = nombre
        self.is_admin = is_admin

@authorize
def ver_datos(user):
    print(f"Accediendo a datos para {user.nombre}")

admin = Usuario("Ana", is_admin=True)
invitado = Usuario("Luis")

ver_datos(admin)    # Accede
ver_datos(invitado) # Acceso denegado


#Reflexión individual
#Conozco decoradores como @staticmethod, @classmethod y @property. Me gustaría usarlos más porque ayudan a mantener el código limpio y reutilizable, sobre todo para validaciones o control de acceso sin repetir lógica.


