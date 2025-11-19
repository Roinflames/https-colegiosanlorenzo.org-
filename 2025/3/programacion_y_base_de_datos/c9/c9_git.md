# Propuesta para la Clase 8: Introducción al Control de Versiones con Git y Gestión de Entornos de Python
 
## Justificación:
 
Después de aprender a navegar y gestionar archivos con la línea de comandos, el siguiente paso lógico es introducir las herramientas que los desarrolladores usan a diario en esa misma interfaz. Git es el estándar para el control de versiones y pip junto con los entornos virtuales son fundamentales para cualquier proyecto de Python. Esta clase sentará las bases para comenzar a construir proyectos más complejos, como la aplicación web que parece estar planificada en la carpeta project.

## Objetivos de la Clase:
1. Comprender qué es el control de versiones y por qué es crucial para el desarrollo de software.

2. Aprender los comandos básicos de Git para inicializar un repositorio, añadir cambios y hacer commits. 

3. Entender la importancia de los entornos virtuales en Python para aislar dependencias.

4. Aprender a crear, activar y gestionar entornos virtuales. 

5. Utilizar pip para instalar paquetes externos y gestionar las dependencias de un proyecto. 

## Contenido y Actividades Propuestas:
### Parte 1: Control de Versiones con Git (Aprox. 1.5 horas pedagógicas) 

### Teoría: 
 * ¿Qué es Git? ¿Qué problema resuelve? (Guardar historial, colaborar, etc.). 
 * Diferencia entre Git y GitHub/GitLab.
 * El flujo de trabajo básico: Working Directory -> Staging Area -> Repository.
### Práctica (usando CMD):
* git --version: Verificar instalación.
* git config: Configurar nombre de usuario y email.
* git init: Inicializar un repositorio en una nueva carpeta de proyecto. 
* git status: Revisar el estado de los archivos.
* git add <archivo>: Añadir archivos al Staging Area.
* git commit -m "Mensaje": Guardar los cambios en el repositorio. 
* git log: Ver el historial de commits.

### Parte 2: Entornos Virtuales y `pip` en Python (Aprox. 1.5 horas pedagógicas)
* Teoría: 
* ¿Por qué necesitamos entornos virtuales? (Evitar conflictos de versiones entre proyectos). 
* ¿Qué es pip? El gestor de paquetes de Python. 
* Práctica (usando CMD):
* Crear un entorno virtual: python -m venv .venv
* Activar el entorno: .venv\Scripts\activate
* Verificar que el entorno está activo (el prompt cambia). 
* Instalar un paquete: pip install flask (o un paquete más simple como cowsay para un ejemplo divertido).
* Ver los paquetes instalados: pip list
* Generar un archivo de dependencias: pip freeze > requirements.txt 
* Desactivar el entorno: deactivate

### Ejercicio Práctico Integrador: 
1. Crear una carpeta para un nuevo proyecto (ej. mi-primer-proyecto-git).
2. Dentro de ella, inicializar un repositorio de Git. 
3. Crear y activar un entorno virtual. 
4. Instalar el paquete flask. 
5. Crear un archivo app.py con un "Hola Mundo" básico de Flask.
6. Crear un archivo .gitignore para excluir la carpeta del entorno virtual (.venv/).
7. Añadir app.py y .gitignore al Staging Area.
8. Hacer el primer commit con el mensaje "Commit inicial del proyecto Flask".
9. Generar el requirements.txt y hacer un segundo commit.

Esta clase conectaría directamente con la siguiente, que podría ser ya el desarrollo de la aplicación Flask (c9), utilizando la estructura y herramientas preparadas en esta clase 8.