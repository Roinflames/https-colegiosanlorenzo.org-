import json

# Abrir el archivo JSON
with open('lista_estudiantes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Mostrar los primeros registros
for estudiante in data[:5]:
    print(estudiante)

# Pasar a un dataframe pandas

# Generar graficos con matplotlib