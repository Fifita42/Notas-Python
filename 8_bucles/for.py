animales = ['gato','perro','loro']
animales2 = ['gatos','perros','loros']

for animal in animales:
    print(f'Animal: {animal}')
    
print('-------------------')

for animal,animal2 in zip(animales,animales2):
    print(f'Animal: {animal}')
    print(f'Animal 2: {animal2}')

print('-------------------')

for num in range(10,20):
    print(num)
    
print('-------------------')
#devuelbe una tupla con el indice y el valor
for num in enumerate(animales):
    print(num)
    
for num in enumerate(animales):
    indice,animal=num
    print(f'el indice es {indice} y el animal es {animal}')
    
print('-------------------')
#for/else
for num in enumerate(animales):
    indice,animal=num
    print(f'el indice es {indice} y el animal es {animal}')
else: print('El for se ejecuto correctamente')
print('-------------------')

#todo lo anterior funciona para las tuplas y listas y conjuntos
#--------------------------------------------------
#iterar conjuntos
