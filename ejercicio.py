#Ejercicio N°4
class Cancion:
    def __init__(self, titulo, autor):
     self.titulo = titulo
     self.autor = autor
    
    def get_titulo(self):
        return self.titulo 
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def set_autor(self, autor):
        self.autor = autor
        
    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"
    
c = Cancion("It's My Life", "Bon Jovi")
print(c)  
c.titulo = "Livin' On a Prayer"
c.autor = "Bon Jovi"
print(c)  
