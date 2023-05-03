import re
email = "example@example.com"
#Pueden ser válidos las coincidencias que tengan:
#De la A a la Z.
#De la A mayúscula a la Z mayúscula. 
#Del 0 al 9.
#Todo lo que no sea un espacio en línea.
#Los _ tambien estan permitidos
#Igualmente los % que hace que todo lo que encuentre antes y despues de el lo valide
#El + busca una o mas coincidencias

#El siguiente + despues del ] es para decir que si o si, almenos 1 de las anteriores coincidencias tiene que haber
#despues debe haber un @
#despues otravez las mismas condiciones
#despues buscar un .
#por ultimo debe haber valores de la a-z o A-Z almenos 2 veces
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"