import modulo1
if __name__ == '__main__':
    print("Este modulo (modulo2) esta siendo ejecutado directamente")
    print(__name__)
    print(modulo1.__name__)
else:
    print("Este modulo (modulo2) esta siendo ejecutado indirectamente")
    print('----------------------------------')
