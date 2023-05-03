def obtener_compañeros(cantidad):
    compañeros= []
    for i in range(cantidad):
        nombre = input('Ingrese el nombre del alumno: ')
        edad = int(input('Ingrese la edad del alumno: '))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asitente = compañeros[0][0]
    maestro = compañeros[-1][0]
    return asitente,maestro
