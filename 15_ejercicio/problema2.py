#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("15_ejercicio\\datos.csv")

#convierte a string
df['edad'] = df['edad'].astype(str)
print(type(df['edad'][0]))

#reemplazar dato
df['nombre'].replace("Malvada","Melina",inplace=True)
print(df['nombre'])
df['nombre'].replace("Melina","Malvada",inplace=True)
print(df['nombre'])

#borrar filas que no tengan todos los datos
df = df.dropna()

#Eliminar columnas con datos faltantes
df = df.dropna(axis=1)

#eliminar filas repetidas
df = df.drop_duplicates()

#crear un dataframe
df.to_csv("15_ejercicio\\datos2.csv")