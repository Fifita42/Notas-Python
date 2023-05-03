diccionario = {
    'nombre':'tobias',
    'apellido':'molina',
    'edad':18
}

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es {value}')
print("-----------------------------------")
for datos in diccionario:
    key = datos
    print(f'la clave es: {key}')
print("-----------------------------------")
for datos in diccionario:
    key = diccionario.get(datos)
    print(f'el valor es: {key}')
