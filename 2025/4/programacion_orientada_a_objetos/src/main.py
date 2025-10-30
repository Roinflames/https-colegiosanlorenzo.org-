#Importar bibliotecas
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

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

# Limpiar columna 'edad' para quedarnos solo con números
def limpiar_edad(valor):
    match = re.search(r'\d+', valor)  # Extrae el primer número
    return int(match.group()) if match else None

df['edad_num'] = df['edad'].apply(limpiar_edad)

# Verificar
print(df[['nombre', 'curso', 'edad', 'edad_num']])

# Generar graficos con matplotlib
# a) Gráfico de barras
edad_counts = df['edad_num'].value_counts().sort_index()

plt.figure(figsize=(6,4))
plt.bar(edad_counts.index, edad_counts.values, color='skyblue')
plt.title(f'Distribución de edades - Curso {df["curso"].iloc[0]}')
plt.xlabel('Edad')
plt.ylabel('Cantidad de estudiantes')
plt.tight_layout()
plt.show()

# b) Histograma
# Lista de respuestas que consideraremos como "sin aprendizaje"
sin_aprendizaje = ['nada', 'ninguna', 'no recuerdo', 'nose', 'no se', 'muy poco', 'poco']

# Creamos una nueva columna categorizando
df['categoria_aprendizaje'] = df['aprendizaje'].apply(
    lambda x: 'Sin aprendizaje' if str(x).strip().lower() in sin_aprendizaje else 'Con aprendizaje'
)

conteo = df['categoria_aprendizaje'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(conteo.index, conteo.values, color=['salmon', 'lightgreen'], edgecolor='black')
plt.title('Distribución de respuestas sobre aprendizaje')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de estudiantes')
plt.tight_layout()
plt.show()

# c) Gráfico de línea
# Meses del año
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

# Asistencia inventada (%)
asistencia = [95, 92, 90, 88, 93, 97, 96, 94, 91, 89, 90, 92]

# Crear gráfico de línea
plt.figure(figsize=(10,5))
plt.plot(meses, asistencia, marker='o', linestyle='-', color='blue')
plt.title("Asistencia General del Año")
plt.xlabel("Mes")
plt.ylabel("Asistencia (%)")
plt.ylim(0, 100)
plt.grid(True)
plt.show()