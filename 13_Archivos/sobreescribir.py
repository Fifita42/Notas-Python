with open("13_Archivos\\archivo\\texto.txt",'w',encoding="UTF-8") as archivo:
    #Sobreescribiendo el archivo
    #archivo.write("Hola")
    archivo.writelines(["Agregando una linea al archivo\n","Agregando una segunda linea 2\n"])
    archivo.writelines(["Agregando una 3 linea al archivo\n","Agregando una segunda linea 4"])
#Con la propiedad 'w' si no encuentra el archivo, lo crea