def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def descripcion(self):

        print("mi nombre es: ",self.nombre ,"\nApellido: ",self.apellido)

