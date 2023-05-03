def sumar():
    while True:
        a = input("N1: ")
        b = input("N2: ")
        try:
            resultado = int(a)+int(b)
        except:
            print("Valor invalido.")
        else: 
            break#si no ubo erroes y se pasa correctamente el try
        finally:
            print("Esto se ejecuta siempre")
    return resultado
print(sumar())