import pandas as pd
import matplotlib.pyplot as plt #lobreria de visualizacion de datos de froma graafica
import seaborn as sns #libreria de graficos estadisticos

df = pd.read_csv("16_graficos\\cofla_ingresos.csv")
sns.barplot(x="Fuente",y="Ingresos",data=df)
total_ingresos = df['Ingresos'].sum()
print(f'El total de ingresos es de ${total_ingresos} dolares.')
plt.show()