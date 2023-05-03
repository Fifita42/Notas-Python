#creando un conjunto con set
conjunto = set(['dato 1','dato 2'])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato 1','dato 2'])#crea un conjunto congelado
conjunto2 = {conjunto1,'dato 3'}

#teoria de conjuntos 
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
print(resultado)
#de otra forma seria
resultado = conjunto2<=conjunto1
print(resultado)

#verificar si hay solo UN resultado en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
