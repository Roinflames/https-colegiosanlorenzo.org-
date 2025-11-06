# Informe de Eventos de Implementación Piloto: Gestor de Datos Académicos

## 1. Introducción
Este informe detalla la implementación piloto de un sistema de gestión de datos académicos, desarrollado para optimizar el registro y consulta de información estudiantil. El objetivo principal fue evaluar la funcionalidad y usabilidad de la aplicación en un entorno controlado, identificando áreas de mejora antes de un despliegue a mayor escala.

## 2. Descripción y Alcance de la Aplicación
### 2.1. Descripción de la App
**Nombre:** Gestor Académico v1.0
**Propósito:** Facilitar la administración de calificaciones, asistencia y datos personales de estudiantes.
**Funcionalidades:** CRUD (Crear, Leer, Actualizar, Eliminar) para estudiantes, cursos y calificaciones; generación de reportes básicos.
**Público Objetivo:** Docentes y personal administrativo de instituciones educativas.

### 2.2. Alcance de la Implementación Piloto
**Objetivos:** Validar la interfaz de usuario, probar la persistencia de datos y recopilar feedback inicial.
**Ubicación y Duración:** Laboratorio de informática del colegio San Lorenzo, durante 2 semanas (Octubre 2025).
**Usuarios Involucrados:** 5 docentes y 2 administrativos.
**Nivel de Satisfacción:** Inicialmente moderado, con potencial de mejora.

### 2.3. Consideraciones Adicionales
**Desafíos:** Curva de aprendizaje inicial para usuarios no técnicos, problemas menores de rendimiento en consultas complejas.
**Lecciones Aprendidas:** Necesidad de tutoriales más claros y optimización de consultas a la base de datos.

## 3. Codificación y Tecnologías Utilizadas
### 3.1. Codificación y Desarrollo
**Arquitectura:** Cliente-servidor (2 capas simplificada).
**Lenguaje/Paradigma:** Python 3.9, Programación Orientada a Objetos.
**Gestión de Base de Datos:** SQLite (para prototipo), con ORM SQLAlchemy.
**Prácticas de Trabajo:** Desarrollo ágil básico (iteraciones semanales).

### 3.2. Tecnologías Utilizadas
**Plataforma/IDE:** Visual Studio Code.
**Herramientas de Desarrollo:** Git para control de versiones, pytest para pruebas unitarias.
**Tecnologías de Interfaz de Usuario:** Tkinter para la GUI de escritorio.
**Medidas de Seguridad:** Hashing SHA-256 para contraseñas de usuario.

## 4. Resultados y Conclusiones
### 4.1. Resultados
**Desempeño:** Opiniones mixtas; buena respuesta en operaciones básicas, lenta en reportes.
**Usabilidad/Experiencia Usuario:** Interfaz intuitiva para la mayoría, pero algunos campos generaron confusión.
**Problemas Técnicos:** 3 errores críticos (cierre inesperado) reportados, 7 errores menores (validación de entrada).

### 4.2. Conclusiones
**Logros:** Creación exitosa de usuarios y registro de datos.
**Lecciones Aprendidas (FODA):**
*   **Fortalezas:** Facilidad de instalación, modularidad del código.
*   **Oportunidades:** Integración con sistemas existentes, mejora de reportes.
*   **Debilidades:** Rendimiento en grandes volúmenes de datos, falta de validación robusta.
*   **Amenazas:** Resistencia al cambio por parte de usuarios, requisitos cambiantes.
**Recomendaciones:** Priorizar optimización de base de datos y mejorar validación de entrada.

## 5. Análisis y Recomendaciones
### 5.1. Análisis de Resultados
**Evaluación:** Se observó una tendencia positiva en la adopción, pero con frustraciones puntuales por rendimiento.
**Comparación con Objetivos:** Se cumplió el objetivo de validar la funcionalidad básica, pero la usabilidad requiere ajustes.
**Feedback Usuarios:** Sugerencias para simplificar formularios y añadir filtros de búsqueda.

### 5.2. Recomendaciones
**Mejoras Funcionales (Backend):** Optimizar consultas SQL, considerar migración a PostgreSQL para escalabilidad.
**Optimización Usabilidad (Frontend):** Rediseñar formularios complejos, añadir mensajes de error más claros.
**Plan de Acción:**
1.  Sprint 1: Optimización de consultas y validación de entrada.
2.  Sprint 2: Rediseño de interfaz de usuario para formularios clave.
3.  Sprint 3: Implementación de tutoriales interactivos.
