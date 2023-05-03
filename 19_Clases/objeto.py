class veiculo:
    #variables de la clase
    ruedas = 0
    #constructor
    def __init__(self,modelo,anio,color):
        #atributos
        self.modelo = modelo
        self.anio = anio
        self.color = color
    #metodos
    def conducir(self):
        print("Esta conduciendo")
    def stop(self):
        print("Esta quieto")   

class Car(veiculo):
    ruedas = 4

class moto(veiculo):
    ruedas = 2
