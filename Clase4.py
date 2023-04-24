def dice(self):
 print('Guauuuuuu')

Animal = type('Perro', (), {'nombre':'a definir'})
Perro = type('Perro', (Animal, ),dict(cantidad_patas=4, dice=dice))

p = Perro()

print(p.nombre) # Imprime a definir
print(p.cantidad_patas) # Imprime 4
p.dice() # Imprime Guauuuuuu