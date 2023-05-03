from multiprocessing import Process, cpu_count
import time
def counter(num):
    count = 0
    while count < num:
        count += 1
def main():
    #Cantidad de nucleos del procesador
    print(cpu_count())
    
    #Uso solo un nucleo para hacer esta tarea
    a = Process(target=counter,args=(100000,))
    a.start()
    a.join()
    print("Terminado en: ",time.perf_counter()," segundos")

if __name__ == '__main__':
    main()
    
#Se diferencia de los hilos en que:
# multithreading: utiliza múltiples hilos dentro de un solo proceso para lograr la multitarea. Cada hilo se ejecuta en paralelo y puede 
# realizar una tarea diferente. Los hilos comparten recursos, como la memoria y los archivos, pero solo uno de ellos puede ejecutarse en un 
# momento dado en el procesador (a menos que se tenga más de un núcleo o CPU).

# multiprocessing: utiliza múltiples procesos separados para lograr la multitarea. Cada proceso es independiente y tiene su propio espacio 
# de memoria y recursos. Los procesos se ejecutan en paralelo en el procesador y pueden realizar tareas diferentes al mismo tiempo.