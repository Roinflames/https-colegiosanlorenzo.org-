<!-- 3 horas pedagògicas -->
# Clase 7: Introducción a la Línea de Comandos (CMD)
[GAMMA](https://gamma.app/docs/Introduccion-a-la-Linea-de-Comandos-CMD-vr1j4lxkqf8andu?mode=doc)

## Objetivo de la Clase
Familiarizar a los estudiantes con los comandos básicos e intermedios de la línea de comandos de Windows (CMD), entendiendo su utilidad para la navegación de archivos, gestión de directorios y ejecución de programas.

## ¿Qué es la Línea de Comandos (CMD)?
La línea de comandos es una interfaz basada en texto que permite a los usuarios interactuar directamente con el sistema operativo mediante comandos escritos. Es una herramienta poderosa para automatizar tareas, diagnosticar problemas y gestionar el sistema de manera eficiente.

## Comandos Básicos

### 1. `cd` (Change Directory)
Permite cambiar el directorio actual.
- **`cd <nombre_directorio>`**: Entra a un directorio específico.
- **`cd ..`**: Sube un nivel en la jerarquía de directorios.
- **`cd \`**: Va a la raíz de la unidad actual.
- **`cd /d <letra_unidad>:`**: Cambia a otra unidad (ej. `cd /d D:`).

**Ejemplos:**
```cmd
cd Documentos
cd ..
cd \
cd /d D:
```

### 2. `dir` (Directory)
Muestra una lista de archivos y subdirectorios dentro de un directorio.
- **`dir`**: Muestra el contenido del directorio actual.
- **`dir /p`**: Muestra el contenido página por página.
- **`dir /w`**: Muestra el contenido en formato ancho (varias columnas).
- **`dir /s`**: Muestra el contenido del directorio actual y todos sus subdirectorios.
- **`dir *.txt`**: Muestra solo archivos con extensión `.txt`.

**Ejemplos:**
```cmd
dir
dir /p
dir /s *.log
```

### 3. `mkdir` (Make Directory) / `md`
Crea un nuevo directorio.
- **`mkdir <nombre_directorio>`**: Crea un directorio con el nombre especificado.

**Ejemplos:**
```cmd
mkdir NuevaCarpeta
md Proyectos\MiProyecto
```

### 4. `rmdir` (Remove Directory) / `rd`
Elimina un directorio. El directorio debe estar vacío para ser eliminado con `rmdir` sin opciones.
- **`rmdir <nombre_directorio>`**: Elimina un directorio vacío.
- **`rmdir /s <nombre_directorio>`**: Elimina un directorio y todos sus subdirectorios y archivos (solicita confirmación).
- **`rmdir /s /q <nombre_directorio>`**: Elimina un directorio y todos sus subdirectorios y archivos sin pedir confirmación (¡usar con precaución!).

**Ejemplos:**
```cmd
rmdir CarpetaVacia
rmdir /s CarpetaConContenido
```

### 5. `del` (Delete)
Elimina uno o más archivos.
- **`del <nombre_archivo>`**: Elimina un archivo específico.
- **`del *.txt`**: Elimina todos los archivos `.txt` en el directorio actual.
- **`del /p <nombre_archivo>`**: Solicita confirmación antes de eliminar cada archivo.

**Ejemplos:**
```cmd
del mi_documento.txt
del *.bak
```

### 6. `copy`
Copia uno o más archivos de una ubicación a otra.
- **`copy <origen> <destino>`**: Copia archivos.

**Ejemplos:**
```cmd
copy archivo.txt C:\NuevaCarpeta
copy *.jpg D:\FotosBackup
```

### 7. `move`
Mueve archivos y directorios de una ubicación a otra.
- **`move <origen> <destino>`**: Mueve archivos o directorios.

**Ejemplos:**
```cmd
move documento.docx C:\Documentos\Reportes
move C:\Temp\MiCarpeta C:\Archivos
```

### 8. `ren` (Rename) / `rename`
Cambia el nombre de un archivo o directorio.
- **`ren <nombre_antiguo> <nombre_nuevo>`**: Renombra.

**Ejemplos:**
```cmd
ren archivo_viejo.txt archivo_nuevo.txt
ren CarpetaAntigua CarpetaNueva
```

### 9. `cls` (Clear Screen)
Limpia la pantalla de la consola.

**Ejemplo:**
```cmd
cls
```

### 10. `exit`
Cierra la ventana de la línea de comandos.

**Ejemplo:**
```cmd
exit
```

## Comandos Intermedios

### 1. `ipconfig`
Muestra la configuración de red de Windows.
- **`ipconfig`**: Muestra la configuración básica.
- **`ipconfig /all`**: Muestra la configuración completa, incluyendo adaptadores físicos y lógicos.

**Ejemplos:**
```cmd
ipconfig
ipconfig /all
```

### 2. `ping`
Envía paquetes de datos a una dirección IP o nombre de host para verificar la conectividad de red.
- **`ping <dirección_ip_o_host>`**: Envía 4 paquetes.
- **`ping -t <dirección_ip_o_host>`**: Envía paquetes continuamente hasta que se detenga manualmente (Ctrl+C).

**Ejemplos:**
```cmd
ping google.com
ping 192.168.1.1
```

### 3. `tracert` (Trace Route)
Muestra la ruta que toman los paquetes de datos para llegar a un destino. Útil para diagnosticar problemas de red.

**Ejemplos:**
```cmd
tracert google.com
```

### 4. `tasklist`
Muestra una lista de todos los procesos que se están ejecutando en el sistema.

**Ejemplo:**
```cmd
tasklist
```

### 5. `taskkill`
Termina uno o más procesos en ejecución.
- **`taskkill /im <nombre_imagen_proceso>`**: Termina un proceso por su nombre de imagen (ej. `notepad.exe`).
- **`taskkill /pid <id_proceso>`**: Termina un proceso por su ID de proceso.
- **`taskkill /f /im <nombre_imagen_proceso>`**: Fuerza la terminación de un proceso.

**Ejemplos:**
```cmd
taskkill /im notepad.exe
taskkill /pid 1234
taskkill /f /im chrome.exe
```

### 6. `systeminfo`
Muestra información detallada sobre la configuración del sistema operativo y el hardware.

**Ejemplo:**
```cmd
systeminfo
```

### 7. `findstr`
Busca cadenas de texto en archivos. Es una versión más potente de `find`.
- **`findstr "texto a buscar" <nombre_archivo>`**: Busca el texto en el archivo.
- **`findstr /i "warning" *.txt`**: Busca el texto (ignorando mayúsculas/minúsculas) en todos los archivos `.txt`.
- **`findstr /r "expresión regular" <nombre_archivo>`**: Busca usando expresiones regulares.

**Ejemplos:**
```cmd
findstr "error" log.txt
findstr /i "warning" *.log
```

### 8. `echo`
Muestra mensajes en la consola o se utiliza para escribir texto en archivos.
- **`echo Hola Mundo`**: Muestra "Hola Mundo".
- **`echo Texto > archivo.txt`**: Escribe "Texto" en `archivo.txt` (sobrescribe).
- **`echo Más Texto >> archivo.txt`**: Añade "Más Texto" a `archivo.txt`.

**Ejemplos:**
```cmd
echo Iniciando script...
echo Este es un nuevo log > nuevo_log.txt
echo Otra línea >> nuevo_log.txt
```

### 9. `assoc` y `ftype`
- **`assoc`**: Muestra o modifica las asociaciones de extensiones de archivo.
- **`ftype`**: Muestra o modifica los tipos de archivo que se utilizan en las asociaciones de extensiones de archivo.

**Ejemplos:**
```cmd
assoc .txt
ftype txtfile
```

### 10. `help`
Proporciona ayuda sobre los comandos de CMD.
- **`help`**: Muestra una lista de comandos disponibles.
- **`help <nombre_comando>`**: Muestra información detallada sobre un comando específico.

**Ejemplos:**
```cmd
help
help dir
```

## Ejercicios Prácticos
1.  Crea una estructura de directorios: `Proyecto\` dentro de ella `Documentos\` y `Imagenes\`.
2.  Navega a la carpeta `Documentos`.
3.  Crea un archivo de texto llamado `notas.txt` dentro de `Documentos` usando `echo`.
4.  Copia `notas.txt` a la carpeta `Imagenes`.
5.  Renombra `notas.txt` en `Imagenes` a `fotos_info.txt`.
6.  Elimina el archivo `notas.txt` original en `Documentos`.
7.  Vuelve a la raíz de tu unidad y elimina la carpeta `Proyecto` con todo su contenido.

## Recursos Adicionales
-   [Documentación oficial de comandos de Windows](https://docs.microsoft.com/es-es/windows-server/administration/windows-commands/windows-commands)
-   [Tutoriales de CMD en YouTube](https://www.youtube.com/results?search_query=comandos+cmd+basicos)
