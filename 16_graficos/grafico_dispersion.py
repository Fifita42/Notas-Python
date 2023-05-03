import pandas as pd
import matplotlib.pyplot as plt #lobreria de visualizacion de datos de froma graafica
import seaborn as sns #libreria de graficos estadisticos

df = pd.read_csv("16_graficos\\dispersion.csv")
sns.scatterplot(x="Tiempo",y="Dinero",data=df)
plt.show()