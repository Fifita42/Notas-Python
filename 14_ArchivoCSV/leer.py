import csv
with open("14_ArchivoCSV\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)