import random
elecciones = ["piedra","papel","tijera"]
pc = random.choice(elecciones)
player = None
#Mientras el valor de player no esta en elecciones
while player not in elecciones:
    player = input("Piedra, Papel o Tijera?: ").lower()
print(f"Computadora: {pc}")
print(f"Jugador: {player}")
if player == pc:
    print("Empate") 
elif player=="piedra":
    if pc == "papel":
        print("Perdiste")
    else:
        print("Ganaste")
elif player=="papel":
    if pc == "piedra":
        print("Ganaste")
    else:
        print("Perdiste")