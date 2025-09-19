import time
import itertools

alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]}{;:',.<>/?\\|`~\""
contraseña  = "ABC1"

def generar_combinaciones(longitud):
    return itertools.product(alfabeto, repeat=longitud)

def fuerza_bruta(contraseña_objetivo):
    intentos = 0
    tiempo_inicio = time.time()
    
    for longitud in range(1, len(contraseña_objetivo)+1):
        for combinacion in generar_combinaciones(longitud):
            intentos += 1
            intento = "".join(combinacion)
            if intento == contraseña_objetivo:
                tiempo_fin = time.time()
                print("Contraseña encontrada: ", intento)
                print("Intentos realizados: ", intentos)
                print("Tiempo de ejecucion: ", tiempo_fin - tiempo_inicio, " segundos")
                return
if __name__ == "__main__":
    fuerza_bruta(contraseña)
    
