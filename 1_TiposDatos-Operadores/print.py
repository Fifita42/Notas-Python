from operator import truediv

nombreDeTuTioMaster = "camelCase"
nombre_de_tu_tio_master = "snake_case"

string1 ="string"

"""
Este tambien es un string
"""



entero = 10
flotantte = 10.5
booleano = False
booleano2 = True
texto = f"Hola esto es un {string1}"

tipo_de_dato = type(texto)
print(tipo_de_dato)

#la f me permite tomar un dato y transformarlo en texto para concatenar
del string1#del borra una variable que declare
print("hola")

#operadores de pertenencia in y not in
print("Hol" in texto)#busca cierta cadena de texto
print("Hol" not in texto)

#Asignar valores a una variable que es parte de una expresion mas larga
print(feliz:=True)

foods = list()
while food:=input("Que comida tegusta?: ") != "quit":
    foods.append(food)

#lista
lista = ["tobias",3,3,3]
print(lista)
print(lista[0])
lista[0] = "otro texto"

#tupla. se diferencia del anterior en que a una tupla no le puedo cambiar los valores
tupla =  ("tobias",3,3,3)
print(tupla[0])

#conjunto (set). son elementos deesordenados, los valores no pueden ser modificados pero el conjunt si.
#no puedo acceder por indice a sus  valores y estos valores solo pueden ser unicos
conjunto = {"tobias",3,5,6}
print(conjunto)


#creando un diccionario, basicamente un json
diccionario = {
    'nombre': 'tobias molina',
    'altura':1.66,
    'casado':False
    #key:valor
}

print(diccionario['nombre'])

numero1 = 4
numero2 = 2

#suma
print(numero1+numero2)
#resta
print(numero1-numero2)
#divicion
print(numero1/numero2)#devuelbe siempre numero flotante
#multiplicacion
print(numero1*numero2)
#potencia
print(numero1**numero2)
#division baja
print(numero1//numero2)#devuelbe un entero redondeado hacia abajo
#resto o modulo
print(numero1%numero2)

#slicing, mostrar desde un punto a otro punto los datos de una lista
cadena ="0123456789"
print(cadena[3:6])#La primera posicion la incluye pero a la segunda no