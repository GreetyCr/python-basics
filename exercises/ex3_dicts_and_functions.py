# 1. Define un dict con productos y precios, p.ej. {'manzana': 200, 'pan': 150}.
# 2. Escribe una función `calcular_total(compra: dict) -> int` que sume los valores.
# 3. Prueba la función con distintos dicts de ejemplo.
def calcular_total(compra: dict) -> int:
  return sum(compra.values())

def main():
  compra = {'manzana': 200, 'pan': 150, 'leche': 300, 'cereales': 100}
  compra2 = {'pera': 220, 'pancito': 100, 'avena': 200, 'cereales': 100}
  total = calcular_total(compra)
  total2 = calcular_total(compra2)
  print(f"El total de la compra es: {total}")
  print(f"El total de la compra es: {total2}")

if __name__ == "__main__":
  main()

