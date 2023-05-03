#creando diccionario con dict()
diccionario = dict(nombre='tobias',apellid='molina')

#crear diccionario con fromkeys, que lo crea con sus keys conteniendo none
diccionario = dict.fromkeys(['nombre','apellido'])
print(diccionario)
#podemos usarlo para asignarle el mismo valor a muchas keys
diccionario = dict.fromkeys("ABCDE","Valor")
print(diccionario)

