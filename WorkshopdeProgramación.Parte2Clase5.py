#4. Herencia Múltiple
#Pregunta teórica:
#¿Qué es la herencia múltiple y qué problema puede generar en lenguajes como Python?
#La herencia múltiple ocurre cuando una clase hereda de dos o más clases al mismo tiempo.
#En Python esto es posible, pero puede generar conflictos si las clases base tienen métodos con el mismo nombre.
#Uno de los principales problemas es el orden en que Python decide qué método ejecutar: esto se resuelve mediante el MRO (Method Resolution Order).

#Mini autoevaluación
#1. ¿Qué es el orden de resolución de métodos (MRO)?
#El MRO es el orden en el que Python busca los métodos cuando hay herencia múltiple. Se puede ver con Clase.__mro__ o help(Clase).
#Usa un algoritmo llamado C3 Linearization.

#2. ¿Qué conflicto puede surgir si dos clases tienen el mismo método y una clase hereda de ambas?
#El conflicto es que Python no sabría de qué clase ejecutar el método si no se respeta el orden de herencia. El MRO determina cuál se elige.
#i no se define bien, puede causar errores o comportamientos inesperados.

