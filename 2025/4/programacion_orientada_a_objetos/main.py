import json

# Abrir el archivo JSON
with open('bdd.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Mostrar los primeros registros
for estudiante in data[:5]:
    print(estudiante)

# Pasar a un dataframe pandas
import json
import pandas as pd

# Assuming the file is now accessible, load the data
try:
    with open('bdd.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: 'bdd.json' not found. Please ensure the file is in the correct directory.")
    data = None

print(data)

# Generar graficos con matplotlib