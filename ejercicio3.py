#Ejercicio N°3
from ejercicio2 import Punto  
class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b
        
    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia
        
    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia
        
    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia
    
    def mueve_abajo(self, distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia
        
    def __str__(self):
        return f"Línea de {self._punto_a} a {self._punto_b}"
