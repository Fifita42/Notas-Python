# archivo_sin_leer = open("13_Archivos\\archivo\\texto.txt",encoding="UTF-8")
# archivo = archivo_sin_leer.read()
# print(archivo)

archivo_sin_leer = open("13_Archivos\\archivo\\texto.txt",encoding="UTF-8")
lineas = archivo_sin_leer.readlines()
print(lineas)


#Cerrar el archivo
archivo_sin_leer.close()
