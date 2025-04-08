#Ejercicio N°2
class Punto():
    def __init__(self,x,y):
        self.x = x
        self.y = y 
        
    def eje_x(self):
     return self.x
 
    def eje_y(self):
     return self.y
 
    def impreso(self):
     return f"({self.x},{self.y})"

    def opuesto(self):
     return Punto(-self.x,-self.y)
 
    def distancia_origen(self):
     return (self.x**2 + self.y**2)** 0.5

    def __str__(self):
     return self.impreso()
