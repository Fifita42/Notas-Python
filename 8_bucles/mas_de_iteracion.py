frutas = ['banana','pera','naranja','manzana']

#evitando comer una pera con la sentencia continue
for fruta in frutas:
    if fruta == 'pera':
        continue#ignora todo lo de abajo
    print(f'Me voy a comer una {fruta}')
print('--------------------------------')
#evitar que el bucle continue iterando
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')
    
print('--------------------------------')

numeros = [3,4,5,6,7]
#for en una linea de codigo
numeros_duplicados = [x*2 for x in numeros]#para realizar un for en una linea, obligatoriamente tiene que estar entre []
print(numeros_duplicados)