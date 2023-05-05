#A diferencia de los hilos normales, estos no se detienen al cerrar el programa
#Continuaran vivos hasta terminar su tarea
import time
import threading
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count+=1
        print("logged in for: ",count," seconds")
x = threading.Thread(target=timer,daemon=True)
x.start()
#si no tiene la propiedad daemon=True puedo agregarla: x.setDaemon(True)
print(x.isDaemon())

#Al finalizar una tarea que es un hilo no daemon, el daemon thread sera aniquilado
answer = input("Quieres salir?")