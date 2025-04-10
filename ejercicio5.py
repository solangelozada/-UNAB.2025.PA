#Ejercicio N°5
class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
        
    def __str__(self):
        return f"{self._apellido}, {self._nombre}"
    
class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, ciudad, pais, fecha):
        self.titulo = titulo
        self.autor = autor  
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha = fecha

    def leer_info(self):
        return vars(self)

    def mostrar_info(self):
        print(f"Título: {self.titulo} {self.edicion} edición")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"{self.editorial}, {self.ciudad} ({self.pais})")
        print(f"{self.fecha}")
        print(f"{self.paginas} páginas")
        
if __name__ == "__main__":
    autor = Persona("Y. Daniel", "Liang")
    libro = Libro(
        "Introduction to Java Programming", autor,
        "0-13-031997-X", 784, "3a.", "Prentice-Hall",
        "New Jersey", "USA", "viernes 16 de noviembre de 2001"
    )
    libro.mostrar_info()
