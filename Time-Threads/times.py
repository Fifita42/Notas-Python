import threading
import time
#Devolber la fecha de inicio que cree tu computadora
print(time.ctime(0))

#Mostrar la fecha despues de cierta cantidad de milisegundos
print(time.ctime(1683042305.6863256))

#devolver la cantidad de segundos desde esa epoca
print(time.time())

#Fecha actual
print(time.ctime(time.time()))

#Objeto con la fecha
time_object = time.localtime()
print(time_object)

#Hay muchos formatos a parte de %B, investigar. 
#String de la fecha a partir de un objeto time
local_time=time.strftime("%B %d %Y %H:%M:%S",time_object)
# En este caso el formato:
# %B devuelbe el nombre completo del mes local
# %d devuelbe el dia del mes como un numero decimal 01-31
# %Y Año como un numero decimal
# %H La hora coomo un numero decimal 00-23
# %M Los minutos como numeros decimales 00-59
# %S Los segundos como numeros decimales 00-61
print(local_time)

#Retrasos
def comer():
    print("comiendo...")
    time.sleep(3)
    print("termine de comer")
comer()

#Hilos
#Son para ejecutar mas de una cosa a la vez

def cantar():
    time.sleep(3)
    print("termine de cantar")
def correr():
    time.sleep(4)
    print("termine de correr")
def volar():
    time.sleep(5)
    print("termine de volar")
    
x = threading.Thread(target=cantar,args=())
x.start()
y = threading.Thread(target=correr,args=())
y.start()
z = threading.Thread(target=volar,args=())
z.start()
#esperar a que termine el hilo x para pasasr a lo demas
x.join()
print("Prosesando...")
