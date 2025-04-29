# Escribir un script que:
#   a) Lea `data.txt` y cuente cuántas líneas tiene.
#   b) Genere (o sobrescriba) un archivo `output.txt` con el texto:
#      "El archivo tiene X líneas."
#   c) Imprima en consola un mensaje confirmando la escritura.
import os

def contar_lineas_archivo(archivo: str) -> int:
    with open(archivo, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file) #sum(1 for _ in file) es una expresión que cuenta el número de líneas en el archivo.
    
def escribir_output(archivo: str, num_lineas: int):
    with open(archivo, 'w', encoding='utf-8') as file: #'w' es para escribir en el archivo, si no existe, lo crea. Si existe, lo sobreescribe.
        file.write(f"El archivo tiene {num_lineas} líneas.\n")

def main():
    base = os.path.dirname(__file__)           # ruta de exercises/
    input_file = os.path.join(base, 'data.txt')
    output_file = os.path.join(base, 'output.txt')

    # 1) Contar líneas
    num_lineas = contar_lineas_archivo(input_file)

    # 2) Escribir resultado
    escribir_output(output_file, num_lineas)

    # 3) Confirmación en consola
    print(f"[OK] '{output_file}' creado: El archivo tenía {num_lineas} líneas.")

if __name__ == "__main__":
    main()