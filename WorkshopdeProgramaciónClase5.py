#1. Revisión de Programación Imperativa
#Pregunta teórica:
#¿Qué caracteriza a la programación imperativa y en qué se diferencia de la programación declarativa?
#-En programación imperativa, se define cómo se realizan las operaciones, es decir, se especifican los pasos exactos para lograr el resultado.
#En programación declarativa, se describe qué se quiere lograr sin detallar los pasos exactos. Un ejemplo común de programación declarativa es SQL, donde solo indicamos qué datos necesitamos.

 #1.Verdadero o falso
#La programación imperativa se basa en describir qué se quiere lograr, no cómo.
 #Falso
#La programación imperativa se basa en describir cómo se debe realizar un proceso (detallar los pasos), mientras que la programación declarativa describe qué se quiere lograr sin especificar los pasos.

#2. ¿Qué estructuras básicas componen la programación imperativa?
#Las estructuras básicas son:
#Secuencia: Ejecución lineal de instrucciones.
#Condicionales (if, else): Permiten ejecutar diferentes bloques de código según condiciones.
#Bucles (for, while): Repetición de instrucciones.
#Asignaciones: Definir y cambiar el valor de variables.

#Errores a corregir:
#El valor de i no se guarda en ninguna lista. Solo se multiplica i, pero no se agrega a una nueva lista.
#La print(i) se ejecuta en cada iteración, pero no queremos imprimir cada número, sino la lista resultante.

#Código corregido:
nums = [1, 2, 3, 4]
result = []  # Lista para almacenar los resultados
for i in nums:
    if i % 2 == 0:
        result.append(i * 2)  # Multiplicamos solo los pares y los agregamos a la lista
print(result)  # Imprime la nueva lista con los pares duplicados

#Salida
[4, 8]

#Ejercicio práctico
#Función que recibe una lista de números y devuelve otra lista con solo los números pares multiplicados por 3 (usando solo estructuras imperativas):

def multiplicar_pares(nums):
    result = []  # Lista para almacenar los resultados
    for num in nums:
        if num % 2 == 0:  # Verificamos si es par
            result.append(num * 3)  # Multiplicamos el número par por 3 y lo agregamos a la lista
    return result

# Prueba
print(multiplicar_pares([1, 2, 3, 4, 5, 6]))  # Salida: [6, 12, 18]

#Reflexión individual
#Diferencias entre escribir código imperativo y usar comprensiones o funciones como map o filter:
#Imperativo: Es más detallado, ya que se tienen que escribir explícitamente todos los pasos, como inicializar la lista, usar bucles, y hacer las verificaciones.
#Declarativo: El código es más conciso y expresivo. Con funciones como map o filter, o usando comprensiones de listas, se evita la necesidad de escribir el ciclo y las condiciones explícitas, lo que puede hacer el código más fácil de leer y mantener.


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


#3. Cohesión y Acoplamiento
#teórica:
#Una clase con alta cohesión tiene responsabilidades bien definidas y relacionadas entre sí, lo que la hace más fácil de entender, mantener y reutilizar.
#Tener bajo acoplamiento significa que una clase depende poco de otras, lo que permite que los cambios en una clase no afecten directamente a otras.
#Esto es una buena práctica porque favorece un diseño modular, flexible y fácil de testear.

#Mini autoevaluación
#1. ¿Qué significa que una clase esté “altamente acoplada”?
#Que depende fuertemente de otras clases para funcionar. Si una clase cambia, las clases acopladas también deben cambiar, lo que hace el código más frágil y difícil de mantener.
#2. ¿Verdadero o falso? Una clase con alta cohesión tiene muchas responsabilidades distintas.
#Falso
#Una clase con alta cohesión tiene una responsabilidad clara o responsabilidades que están estrechamente relacionadas. Si tiene muchas responsabilidades diferentes, se considera de baja cohesión.

#Código con errores
class InvoiceHandler:
    def handle_invoice(self, invoice):
        print("Total:", invoice['amount'])
        self.save_to_db(invoice)

    def save_to_db(self, invoice):
        print("Saving invoice…")

#Corrección separando responsabilidades en dos clases:

class InvoiceCalculator:
    def calculate_total(self, invoice):
        return invoice['amount']

class InvoiceSaver:
    def save_to_db(self, invoice):
        print("Saving invoice…")

# Uso de ejemplo
invoice = {'amount': 250}

calc = InvoiceCalculator()
total = calc.calculate_total(invoice)
print("Total:", total)

saver = InvoiceSaver()
saver.save_to_db(invoice)

#Ejercicio práctico
#Diseño con bajo acoplamiento usando un objeto intermedio:

class InvoiceCalculator:
    def calculate_total(self, invoice):
        return sum(invoice['items'])  # Suma los valores de la factura

class InvoiceDisplay:
    def show_invoice(self, invoice, total):
        print("Factura:")
        for item in invoice['items']:
            print(f"- Ítem: ${item}")
        print(f"Total: ${total}")

# Ejemplo de uso
invoice = {'items': [100, 150, 50]}

calc = InvoiceCalculator()
total = calc.calculate_total(invoice)

display = InvoiceDisplay()
display.show_invoice(invoice, total)

#Reflexión individual
#Para detectar un alto acoplamiento en mi código, suelo observar si una clase necesita conocer demasiados detalles internos de otras o si los cambios en una clase obligan a modificar varias más. Esto complica el mantenimiento y hace más difícil reutilizar componentes.
#Trato de mantener bajo acoplamiento separando funciones en clases específicas, usando interfaces claras y pasando solo la información necesaria.




