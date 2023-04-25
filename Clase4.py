
#def dice(self):
 #print('Guauuuuuu')
#Animal = type('Animal', (), {'nombre':'a definir'})
#Perro = type('Perro', (Animal, ),dict(cantidad_patas=4, dice=dice))
#p = Perro()
#print(p.nombre) # Imprime a definir
#print(p.cantidad_patas) # Imprime 4
#p.dice() # Imprime Guauuuuuu


class Madre():
    
    def __init__(self, nombre):
        self.nombre = nombre
          
    
    def hablar(self):
        return "Hola, soy Mamá"    
    
class Padre():
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def hablar(self):
        return "Hola, soy Papá"

class Hijo(Madre, Padre):
    
    def __init__(self, nombre, apellido, edad):
        
        super().__init__(nombre, apellido, edad)
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
              
    def hablar(self):
        return "Hola, soy {self.nombre}{self.apellido} y tengo {self.edad} años"
    
hijo = Hijo("Oki", "Reynoso", 24) 