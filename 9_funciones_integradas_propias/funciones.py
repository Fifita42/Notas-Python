numero = [1,2,3,4,5,6,7,8,9]
#encontrar el numero mayor de una lista
numero_alto = max(numero)
print(numero_alto)

#encontrar el numero menonr de una lista
numero_bajo = min(numero)
print(numero_bajo)

#redondeando a 6 decimales
numero2 = round(12.343454565478,6)
print (numero2)

#retornar false -> 0, vacio, false, none
resultado_bool = bool(False)
print(resultado_bool)

#retornar true si todos los valores son verdaderos
resultado_all = all([34,'True',[34,54]])
print(resultado_all)

#sumar todos los valores de un iterable
sum_total = sum(numero)
print(sum_total)

#crear mi propia funcion
def saludar(saludo):
    print(saludo)

saludar('Hola amigo')

#-------
def sumar(n1,n2):
    return n1+n2
suma = sumar(2,3)
print(suma)

#enviar una cantidad de parametros indefinidos
def sumar2(*numeros):
    return sum(numeros) 
print(sumar2(3,4,5,6))

def hello(**kwargs):
    #print("Hello "+kwargs['primero']+" "+kwargs['ultimo']) 
    for key,value in kwargs.items():
        print(value,end=" ")
hello(primero="bro",ultimo="dude")

print("")
#forzar la pertenencia de un parametro
def frase(nombre,apellido,edad):
    print(f'Hola mi nombre es {nombre} {apellido} y tengo {edad} años.')
frase(edad=18,apellido='Molina',nombre='Tobias')


#funcion filter
def es_par(num):
    if(num%2==0):
        return True
    
numeros_pares = filter(es_par,numero)
print(list(numeros_pares))


#funciones lambda, son como las funcines flecha en js
multiplicar_por_dos = lambda x:x*2
print(multiplicar_por_dos(5))
#las usamos para cosas sencillas, retornan automaticamente y no son aptas para muchas lineas de codigo

#funcion filter con lambda
numeros_pares = filter(lambda num:num%2==0,numero)
print(list(numeros_pares))
