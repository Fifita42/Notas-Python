import re
texto = '''
Hola maestro, esta es la cadena 1. como estas mi capitan
Esta es la linea 2243552 de texto.
Y esta es la final (linea 3) definitiva mi capitan'''
#Haciendo una busqueda simple
resultado = re.findall("Esta",texto)#podria agregar ,flags=re.IGNORECASE para ignorar el camelcase
print(resultado)
print("-----------------")

#\d -> busca digitos numericos del 0-9
resultado = re.findall(r"\d",texto)
print(resultado)
print("-----------------")

#en la mayoria de los casos, reemplazar la expresion regular en minuscula por su mayuscula, hace que busque lo contrario como en \d y \D
#\D -> busca TODO MENOS digitos numericos del 0-9
resultado = re.findall(r"\D",texto)
print(resultado)
print("-----------------")

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)
print(resultado)
print("-----------------")

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)
print(resultado)
print("-----------------")

#\s -> busca espacios en blanco -> espacios,tabs,saltos de linea. tambien existe \S
resultado = re.findall(r"\s",texto)
print(resultado)
print("-----------------")

#. -> busca todo menos saltos en linea
resultado = re.findall(r".",texto)
print(resultado)
print("-----------------")

#\n -> busca saltos en linea
resultado = re.findall(r"\n",texto)
print(resultado)
print("-----------------")

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\.",texto)
print(resultado)
print("-----------------")

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r'\d\.\s',texto)
print(resultado)
print("-----------------")

#^ -> busca el comienzo de una linea
resultado = re.findall(r'^Hola',texto,re.M)#el re.M hace que cada lina despues de un \n sea interpretada como una nueva linea
print(resultado)
print("-----------------")

#$ -> busca el final de una linea
resultado = re.findall(r'capitan$',texto,re.M)
print(resultado)
print("-----------------")

#{n}-> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{3}",texto)
print(resultado)
print("-----------------")

#{n,m}-> busca almenos n cantidad de veces y maximo m cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{2,3}",texto)
print(resultado)
print("-----------------")

#| -> busca una cosa o la otra
resultado = re.findall(r"\d{2}|Hola",texto)
print(resultado)
print("-----------------")