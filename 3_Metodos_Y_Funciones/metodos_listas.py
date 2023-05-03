lista = list([3,4,5])#no es la manera optima de crear una lista, pero sirve para crear listas vacias

#ordenar los elementos
lista.sort()
lista.sort(reverse=True)#ordenar al revez

#agregando con append
lista.append("auida")

#agregando un elemento en un indice especifico
lista.insert(2,"amiog")

#agregando varios elementos
lista.extend([5,6,7,3,2])

#invertir la lista 3,9,5 -> 5,9,3 
lista.reverse()

#eliminando un elemento de la lista
lista.pop(0)#para eliminar el ultimo elemento puedo colocar -1

#buscar un elemento para borrarlo
lista.remove(4)


#borra todos los elementos
lista.clear()

#Unir todos los elementos
import functools
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y,:x*y,factorial)
print(result)