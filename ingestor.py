# Librerias a Usar 
from pathlib import Path
import logging
import shutil
import sys


# Creamos las rutas necesarios para el reto
LANDING_PATH = Path("./landing")
BRONZE_PATH = Path("./bronze") # cARPETA BRONCE 
BAD_DATA_PATH = Path("./bad_data") # CARPETA DE DATAS DEFECTUOSAS

# Primero diseñaremos el logging para tener un buen seguimiento del proceso
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    handlers=[
        logging.FileHandler("ingestor.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("Iniciando el proceso de ingesta de datos")
# Conteo
bronze_conteo = 0
bad_data_conteo = 0

# Creacion de la for de ingesta
for archivo in LANDING_PATH.glob("*"):
    if not archivo.is_file(): continue

    try:
        logging.info(f"Procesando el archivo: {archivo.name}")
        # Validacion simple: Verificar si el archivo no esta vacio
        if archivo.stat().st_size == 0:
            raise ValueError("El archivo esta vacio")
        
        # Mover el archivo a la carpeta bronze
        destino = BRONZE_PATH / archivo.name
        shutil.move(str(archivo), str(destino))
        bronze_conteo += 1
        logging.info(f"Archivo movido a la carpeta bronze: {destino}")

    except Exception as e:
        logging.error(f"Error al procesar el archivo {archivo.name}: {e}")
        # Mover el archivo a la carpeta bad_data
        destino_bad = BAD_DATA_PATH / archivo.name
        shutil.move(str(archivo), str(destino_bad))
        bad_data_conteo += 1
        logging.info(f"Archivo movido a la carpeta bad_data: {destino_bad}")

# Informacion final
logging.info("Resumen final del proceso")
logging.info(f"Archivos enviados a Bronze: {bronze_conteo}")
logging.info(f"Archivos enviados a Bad Data: {bad_data_conteo}")

logging.info("Proceso de ingesta finalizado")