Informe Técnico: Gestor de Tareas del Estudiante

  Versión: 1.0
  Fecha: 28/10/2025
  Autor: Gemini CLI

  ---

  1. Resumen Ejecutivo

  El "Gestor de Tareas del Estudiante" es una aplicación de escritorio diseñada para ayudar a los estudiantes a organizar sus tareas y trabajos académicos. La aplicación permite a los usuarios
  añadir, ver, marcar como completadas y eliminar tareas. Este documento detalla los requisitos, diseño, implementación y pruebas de la aplicación.

  ---

  2. Introducción

   * 2.1 Propósito del Informe: Este informe documenta el diseño, la implementación y las pruebas de la aplicación de escritorio "Gestor de Tareas del Estudiante".
   * 2.2 Descripción General de la Aplicación: Es una herramienta simple que permite a los estudiantes llevar un registro de sus responsabilidades académicas.
   * 23 Alcance del Informe: Este informe cubre los requisitos funcionales y no funcionales, la arquitectura y el diseño, los detalles de implementación y las pruebas de la aplicación.
   * 2.4 Público Objetivo: Este informe está destinado a desarrolladores, testers y gestores de proyectos.

  ---

  3. Descripción General del Sistema

   * 3.1 Visión del Producto: Proporcionar a los estudiantes una herramienta sencilla y eficaz para gestionar sus tareas académicas.
   * 3.2 Características Principales:
       * Añadir nuevas tareas con título, descripción y fecha de vencimiento.
       * Ver todas las tareas en una lista.
       * Marcar las tareas como completadas.
       * Eliminar tareas.
   * 3.3 Roles de Usuario e Interacciones: Solo hay un tipo de usuario: el estudiante. El estudiante puede añadir, ver, completar y eliminar tareas.
   * 3.4 Entorno Operativo: La aplicación está diseñada para ejecutarse en Windows 10 y versiones posteriores. Requiere la instalación de .NET 5.0 o superior.

  ---

  4. Requisitos

   * 4.1 Requisitos Funcionales:
       * El usuario podrá añadir una nueva tarea con un título, una descripción y una fecha de vencimiento.
       * El usuario podrá ver una lista de todas las tareas.
       * El usuario podrá marcar una tarea como completada.
       * El usuario podrá eliminar una tarea.
   * 42 Requisitos No Funcionales:
       * Rendimiento: La aplicación debe iniciarse en menos de 3 segundos.
       * Usabilidad: La interfaz de usuario debe ser sencilla e intuitiva.
       * Fiabilidad: La aplicación no debe bloquearse ni perder datos.

  ---

  5. Arquitectura y Diseño

   * 5.1 Arquitectura de Alto Nivel: La aplicación sigue una arquitectura de 3 capas:
       1. Capa de Presentación (GUI): Construida con WPF (Windows Presentation Foundation).
       2. Capa de Lógica de Negocio: Gestiona las operaciones de las tareas (añadir, eliminar, etc.).
       3. Capa de Acceso a Datos: Almacena las tareas en un archivo local (JSON).
   * 5.2 Pila Tecnológica:
       * Lenguaje: C#
       * Framework: .NET 5.0
       * Interfaz de Usuario: WPF

  ---

  6. Manual de Usuario

   * 6.1 Instalación:
       1. Asegúrate de tener .NET 5.0 instalado.
       2. Ejecuta StudentTaskManager.exe.
   * 6.2 Guía de Inicio Rápido:
       * Para añadir una tarea, rellena los campos de texto y haz clic en "Añadir Tarea".
       * Para marcar una tarea como completada, selecciónala en la lista y haz clic en "Marcar como Completada".

  ---