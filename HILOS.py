import threading
import time
import random

# Variable compartida
total_descargas = 0

# Lock para evitar condiciones de carrera
lock = threading.Lock()


def descargar_archivo(nombre, tiempo):
    """
    Simula la descarga de un archivo con tamaño aleatorio
    y muestra el progreso
    """
    global total_descargas

    # Tamaño ficticio del archivo
    tamaño = random.randint(5, 10)
    descargado = 0

    inicio = time.time()

    print(f"Iniciando descarga de {nombre} (tamaño: {tamaño} MB)...")

    # Simulación de descarga por partes
    while descargado < tamaño:
        time.sleep(tiempo / tamaño)
        descargado += 1
        progreso = int((descargado / tamaño) * 100)

        # Evita que los prints se mezclen
        with lock:
            print(f"Descargando {nombre} [{progreso}%]...")
    
    fin = time.time()
    tiempo_real = round(fin - inicio, 2)

    # Sección crítica protegida
    with lock:
        total_descargas += 1
        print(f"Descarga de {nombre} completada en {tiempo_real} segundos.")


def main():
    # Lista de archivos a descargar (nombre, tiempo total)
    archivos = [
        ("Archivo1.zip", 3),
        ("Archivo2.zip", 2),
        ("Archivo3.zip", 4),
        ("Archivo4.zip", 1)
    ]

    hilos = []

    # Crear e iniciar los hilos
    for archivo, tiempo in archivos:
        hilo = threading.Thread(
            target=descargar_archivo,
            args=(archivo, tiempo)
        )
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("\nTodas las descargas han finalizado.")
    print(f"Total de archivos descargados: {total_descargas}")


if __name__ == "__main__":
    main()

