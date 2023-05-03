nombres = ["Tobias","Lucas","Matias","Camila","Pedro"]
apellidos = ["Molina","Dalto","Zing","Rovetix","Tarado"]

with open("15_ejercicio\\personas.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n------------\n") for n,a in zip(nombres,apellidos)]