import modulo2
if __name__ == '__main__':
    print("Este modulo (modulo1) esta siendo ejecutado directamente")
    #Cuando ejecutas un modulo su nombre es main, pero si lo ejecutas desde otro modulo, su nombre sera el por defecto
    print(__name__)
    print(modulo2.__name__)
else:
    print("Este modulo (modulo1) esta siendo ejecutado indirectamente")
    print('----------------------------------')

