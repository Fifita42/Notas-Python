texto1 = "soy el texto 1"
texto2 = "soy ele texto 2"

#dir() es una funcion
print(dir(texto1))#nos devuelve todo lo que le podemos hacer al parametro

#.upper() es un metodo
mayusculas = texto1.upper()#transforma el texto a mayuscula
minusculas = texto1.lower()#transforma el texto a minuscula
primer_letra_mayuscula = texto1.capitalize()#solo la primera letra a mayuscula

#buscamos una cadena en otra cadena, si no existe devuelve -1
busquea_find = texto1.find('a')

#buscamos una cadena en otra cadena, si no existe devuelve un error
busquea_index = texto1.index('a')

#si es numerico devuelbe true, numerico permite que sea "34545346..."
es_numerico = texto1.isnumeric()

#si es alfanumerico devuelve true, solo permite "qwertyuiopasdfghjklñzxcvbnm"
es_alfanumerico = texto1.isalpha()

#contamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = texto1.count('a')

#contamos la cantidad de caracteres de una cadena
caracteres = len(texto1)

#modificar una cadena
cadena_nueva = texto1.replace("soy","No soy")
print(cadena_nueva)

#separar cadenas a partir de una cadena dada
cadena_separada = texto1.split(" ")
