# Proceso de Ingesta de Archivos (Landing → Bronze / Bad Data)

## Descripción

Este script realiza un proceso básico de **ingesta de archivos** siguiendo una arquitectura reproducible en cualquier momento con poco costo computacional, clasificando los archivos ubicados en la carpeta `landing` y moviéndolos a:

- **bronze**: archivos válidos  
- **bad_data**: archivos defectuosos (por ejemplo, archivos vacíos)

Durante toda la ejecución se genera un archivo **`ingestor.log`**, el cual registra el movimiento **archivo por archivo** y un **resumen final del proceso**.

---

## Estructura del proyecto


---

## Funcionamiento del script

1. El script recorre todos los archivos ubicados en la carpeta `landing`.
2. Para cada archivo:
   - Se valida que sea un archivo válido.
   - Se verifica que **no esté vacío**.
3. Si el archivo es válido:
   - Se mueve a la carpeta `bronze`.
   - Se registra el movimiento en el log.
4. Si ocurre un error (por ejemplo, archivo vacío):
   - El archivo se mueve a `bad_data`.
   - Se registra el error y el movimiento en el log.
5. Al finalizar el proceso:
   - Se registra un **resumen final** con el total de archivos enviados a `bronze` y `bad_data`.

---

## Archivo de log (`ingestor.log`)

El archivo de log contiene:
- El inicio y fin del proceso de ingesta.
- El procesamiento **uno a uno** de cada archivo.
- Los errores encontrados.
- El resumen final de la ejecución.

Ejemplo:


---

## Resultado

El proceso garantiza:
- Clasificación automática de archivos.
- Trazabilidad completa mediante logs.
- Separación clara entre datos válidos y defectuosos.
