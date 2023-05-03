import pandas as pd
df=pd.read_csv("14_ArchivoCSV\\datos.csv",names=["Nombre","Apellido","Edad"])
df2=pd.read_csv("14_ArchivoCSV\\datos.csv",names=["Nombre","Apellido","Edad"])

#Obteniendo los datos de la columna nombre
nombres = df['Nombre']
print(df)
df_ordenado = df.sort_values("Edad")
print(df_ordenado)

concatenando_df = pd.concat([df,df2])
print(concatenando_df)

#obteniendo filas individualmente
primer_fila = df.head(0)
print(primer_fila)
 
#Obteniendo la cantidad de filas y columnas con shape
filas_columnas = df.shape
print(filas_columnas)

#Accediendo a un elemento especifico por indice y nombre de columna
elemento_espesifico = df.loc[2,"Edad"]
#Accediendo a un elemento especifico por indices
elemento_espesifico = df.iloc[2,2]


#Accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#Accediendo a filas con edad mayor a 18
mayor18 = df.loc[df["Edad"]>18:,1]
