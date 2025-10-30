#Importar bibliotecas
import json
import pandas as pd
import matplotlib.pyplot as plt

# Abrir el archivo JSON
with open('bdd.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Mostrar los primeros registros
for estudiante in data[:5]:
    print(estudiante)

# Assuming the file is now accessible, load the data
try:
    with open('bdd.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: 'bdd.json' not found. Please ensure the file is in the correct directory.")
    data = None

print(data)
# Pasar a un dataframe pandas
df = pd.DataFrame(data)

# Generar graficos con matplotlib
# a) Gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(df['curso'], df['edad'], color='skyblue')
plt.title('Edades en el Curso')
plt.xlabel('Curso')
plt.ylabel('Edad')
plt.xticks(rotation=45)
plt.show()

# b) Histograma
# plt.figure(figsize=(8,5))
# plt.hist(df['nota'], bins=10, color='lightgreen', edgecolor='black')
# plt.title('Distribución de Notas')
# plt.xlabel('Nota')
# plt.ylabel('Cantidad de Estudiantes')
# plt.show()

# c) Gráfico de línea
# df['fecha'] = pd.to_datetime(df['fecha'])  # Asegúrate de que la columna sea datetime

# plt.figure(figsize=(10,6))
# plt.plot(df['fecha'], df['nota'], marker='o', linestyle='-')
# plt.title('Notas en el tiempo')
# plt.xlabel('Fecha')
# plt.ylabel('Nota')
# plt.grid(True)
# plt.show()
