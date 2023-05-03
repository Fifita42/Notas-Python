import pandas as pd
import matplotlib.pyplot as plt #lobreria de visualizacion de datos de froma graafica
import seaborn as sns #libreria de graficos estadisticos

df = pd.read_csv("16_graficos\\pedos.csv")
sns.lineplot(x="Fecha",y="Pedos",data=df)
plt.plot("01-16",14,"o")#colocar un punto en el valor maximo
plt.show()