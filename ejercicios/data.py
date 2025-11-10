import pandas as pd

try:
    df = pd.read_csv('Product_v6.csv')
    print("CSV cargado correctamente!")
except FileNotFoundError:
    print("Error: CSV 'Product_v6.csv' no encontrado")

#print("First columns from csv file")
#print(df.head())
#print(df.info())
#print(df.describe())       # Análisis de la estructura de datos
#print(df.shape)            # (Filas, Columnas)


tipo_producto = df.index[df['status'] == 'INACTIVE']
print(tipo_producto)
    