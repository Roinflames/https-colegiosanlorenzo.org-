# Informe de Eventos de Implementación Piloto: Aplicación de Gestión de Tareas (Tkinter Python)

## 1. Introducción
Este informe documenta la implementación piloto de una aplicación de escritorio para la gestión de tareas, desarrollada con Python y Tkinter. El propósito fue evaluar la funcionalidad básica, la experiencia de usuario y la estabilidad de la aplicación en un entorno de prueba, con el fin de identificar mejoras antes de su distribución.

## 2. Descripción y Alcance de la Aplicación
### 2.1. Descripción de la App
**Nombre:** TaskMaster v1.0
**Propósito:** Permitir a los usuarios crear, organizar y dar seguimiento a sus tareas diarias.
**Funcionalidades:** Añadir/eliminar tareas, marcar tareas como completadas, establecer prioridades (baja, media, alta), filtrar tareas por estado.
**Público Objetivo:** Usuarios individuales que buscan una herramienta sencilla para la organización personal.

### 2.2. Alcance de la Implementación Piloto
**Objetivos:** Validar la interacción del usuario con la GUI de Tkinter, probar la persistencia de datos local y recoger feedback sobre la usabilidad.
**Ubicación y Duración:** Entorno de desarrollo local en 3 equipos, durante 1 semana (Noviembre 2025).
**Usuarios Involucrados:** 3 desarrolladores internos y 2 usuarios beta.
**Nivel de Satisfacción:** Bueno, destacando la simplicidad, pero con sugerencias de mejora en la interfaz.

### 2.3. Consideraciones Adicionales
**Desafíos:** Adaptación de la interfaz a diferentes resoluciones de pantalla, manejo de errores de entrada de usuario.
**Lecciones Aprendidas:** La importancia de un diseño responsivo y una validación de datos robusta en aplicaciones de escritorio.

## 3. Codificación y Tecnologías Utilizadas
### 3.1. Codificación y Desarrollo
**Arquitectura:** Monolítica (aplicación de escritorio standalone).
**Lenguaje/Paradigma:** Python 3.10, Programación Orientada a Objetos.
**Gestión de Base de Datos:** Archivo JSON para almacenamiento local de tareas.
**Prácticas de Trabajo:** Desarrollo iterativo con enfoque en la funcionalidad principal.

### 3.2. Tecnologías Utilizadas
**Plataforma/IDE:** PyCharm Community Edition.
**Herramientas de Desarrollo:** Git para control de versiones, unittest para pruebas unitarias.
**Tecnologías de Interfaz de Usuario:** Tkinter para la construcción de la interfaz gráfica de usuario.
**Medidas de Seguridad:** No aplica directamente para esta versión local, pero se consideró la sanitización de entradas para prevenir inyección de código.

## 4. Resultados y Conclusiones
### 4.1. Resultados
**Desempeño:** La aplicación funcionó de manera fluida en todas las operaciones, sin retrasos perceptibles.
**Usabilidad/Experiencia Usuario:** Los usuarios encontraron la aplicación fácil de usar para las funciones básicas. Se sugirió una mejora visual para la diferenciación de prioridades.
**Problemas Técnicos:** 1 error menor (no se guardaban las tareas al cerrar la aplicación si no se hacía clic en 'guardar'), resuelto rápidamente.

### 4.2. Conclusiones
**Logros:** Implementación exitosa de las funcionalidades básicas de gestión de tareas y persistencia de datos local.
**Lecciones Aprendidas (FODA):**
*   **Fortalezas:** Interfaz intuitiva, bajo consumo de recursos, fácil de instalar.
*   **Oportunidades:** Añadir funcionalidades de sincronización en la nube, personalización de la interfaz.
*   **Debilidades:** Diseño visual básico, falta de funciones avanzadas (recordatorios, subtareas).
*   **Amenazas:** Competencia de aplicaciones de gestión de tareas más robustas.
**Recomendaciones:** Mejorar el diseño visual y añadir una función de guardado automático.

## 5. Análisis y Recomendaciones
### 5.1. Análisis de Resultados
**Evaluación:** La aplicación cumple con su propósito principal, pero el feedback sugiere que las mejoras en la UI/UX son cruciales para la adopción.
**Comparación con Objetivos:** Los objetivos de funcionalidad y usabilidad básica se lograron, superando las expectativas en estabilidad.
**Feedback Usuarios:** Los usuarios valoraron la simplicidad, pero pidieron más opciones de personalización y una estética más moderna.

### 5.2. Recomendaciones
**Mejoras Funcionales (Backend):** Implementar guardado automático, explorar opciones de base de datos más escalables para futuras versiones.
**Optimización Usabilidad (Frontend):** Refactorizar la interfaz de usuario con un enfoque en la estética moderna de Tkinter (ttk), añadir iconos.
**Plan de Acción:**
1.  Sprint 1: Implementar guardado automático y mejorar la validación de entrada.
2.  Sprint 2: Rediseño visual de la interfaz de usuario utilizando `ttk` y estilos personalizados.
3.  Sprint 3: Añadir funcionalidad de recordatorios y exportación de tareas.
