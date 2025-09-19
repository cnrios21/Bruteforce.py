# BruteforceDemo

Demo simple de fuerza bruta en Python. Sirve para entender cómo escala el número de combinaciones al crecer la longitud y el tamaño del alfabeto.

## Archivos
- `bruteforce.py` : script principal.

## Requisitos
- Python 3.8+
- Opcional: entorno virtual (recomendado).

  
## Ejemplo de salidas

<img width="542" height="528" alt="image" src="https://github.com/user-attachments/assets/b4aaefd6-8322-4ca9-9484-951ccd2c4b31" />


## Reflexion

¿qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?

Lo que sucede es que el programa se demora mas tiempo en decifrar la contraseña porque tiene mas digitos.


## Ejecución (PowerShell / Terminal)
```powershell
python bruteforce.py -p abc -A lower -m 3
python bruteforce.py -p 123 -A digits -m 3
python bruteforce.py -p ABC1 -A alnum -m 4

