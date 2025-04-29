# 1. Define una lista de números (hardcodeada o ingresada por consola).
# 2. Recorre la lista con un loop y calcula el promedio.
# 3. Imprime el resultado.

def main():
  numbers = [1, 2, 3, 4, 5]
  total = 0
  for number in numbers:
    total += number
  average = total / len(numbers)
  print(f"El promedio de la lista es: {average}")

  #Otra forma de hacerlo  
  numbers = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
  total = 0
  for number in numbers:
    total += number
  average = total / len(numbers)
  print(f"El promedio de la lista es: {average}")

  
if __name__ == "__main__":
  main()