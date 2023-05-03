import random
#Random con un rango
x = random.randint(1,6)

#De 0 a 1 pero nunca 1. ej: 0.345345345
y = random.random()

#Un elemento random de una lista
myList = ['Piedra','Papel','Tijera']
z = random.choice(myList)

#Reorganiza una lista, en este caso baraja el mazo
cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)
print(cards)