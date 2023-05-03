diccionario = {
    "nombre":'tobias',
    "apellido":'molina',
    "edad":19
}

#devuelbe un elemento dic_item
claves = diccionario.keys()
print(claves)

#devuelbe un elemento dic_item iterable
claves2 = diccionario.items()
print(claves2)

#recoger un valor del diccionario. se diferencia del ["key"] en que si no hay un resultado, devuelve none
valor = diccionario.get("edad")
print(valor)




#eliminar un elemento del diccionario
diccionario.pop("apellido","edad")

#eliminar todo del diccionario
diccionario.clear()