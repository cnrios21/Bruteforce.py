import time
import itertools
import matplotlib.pyplot as plt

ALFABETO = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]}{;:',.<>/?\\|`~\""

CONTRASENA = "aaaa"  
longitudes = []
tiempos = []

def generar_combinaciones(longitud):
    return itertools.product(ALFABETO, repeat=longitud)

def fuerza_bruta(contraseña_objetivo, max_longitud=None, verbose=True):

    intentos = 0
    if max_longitud is None:
        max_longitud = len(contraseña_objetivo)

    for longitud in range(1, max_longitud + 1):
        t_inicio_long = time.time()
        encontrado = False

        for combinacion in generar_combinaciones(longitud):
            intentos += 1
            intento = "".join(combinacion)
            if intento == contraseña_objetivo:
                t_fin_long = time.time()
                tiempo_long = t_fin_long - t_inicio_long
                longitudes.append(longitud)
                tiempos.append(tiempo_long)
                if verbose:
                    print(f"[+] Encontrada en longitud {longitud} tras {intentos} intentos (tiempo: {tiempo_long:.4f}s)")
                encontrado = True
                break

        if not encontrado:
            t_fin_long = time.time()
            tiempo_long = t_fin_long - t_inicio_long
            longitudes.append(longitud)
            tiempos.append(tiempo_long)
            if verbose:
                print(f"[i] Probadas todas las combinaciones de longitud {longitud} (intentps acumulados: {intentos}) - tiempo: {tiempo_long:.4f}s")

        if encontrado:
            break

    return encontrado, intentos

if __name__ == "__main__":
    encontrado, intentos = fuerza_bruta(CONTRASENA)

    if encontrado:
        print("CONTRASEÑA ENCONTRADA")
    else:
        print("NO ENCONTRADA con las longitudes probadas")
    print("Intentos totales:", intentos)

    if len(longitudes) > 0 and len(tiempos) > 0:
        plt.plot(longitudes, tiempos, marker='o')
        plt.xlabel("Longitud de intento")
        plt.ylabel("Tiempo (segundos)")
        plt.title("Tiempo de fuerza bruta por longitud de contraseña")
        plt.grid(True)
        plt.show()
    else:
        print("No hay datos para graficar.")
