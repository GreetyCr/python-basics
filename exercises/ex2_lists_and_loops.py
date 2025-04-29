# 1. Define una lista de números (hardcodeada o ingresada por consola).
# 2. Recorre la lista con un loop y calcula el promedio.
# 3. Imprime el resultado.

def calcular_promedio(nums: list[int]) -> float:
    return sum(nums) / len(nums) if nums else 0


def main():
  numbers = [1, 2, 3, 4, 5]
  average = calcular_promedio(numbers)
  print(f"El promedio de la lista es: {average}")

  #Otra forma de hacerlo con input y map
  numbers = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
  average = calcular_promedio(numbers)
  print(f"El promedio de la lista es: {average}")


if __name__ == "__main__":
  main()