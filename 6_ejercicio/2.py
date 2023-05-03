frase = input("decime una frase y calculo el tiempo de habla: ")
palabras_separadas = frase.split(" ")
cantidad_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras/2} segundos en decirlo')
print(f"dalto lo diaria en {cantidad_palabras *100//2*1.3/100} segundos")
if cantidad_palabras > 120:
    print("no escribas un testamento")