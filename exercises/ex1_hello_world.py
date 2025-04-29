# 1. Imprime "Hello, World!"
# 2. Pide al usuario su nombre y salúdalo: "¡Hola, <nombre>!"

def main():
  name = input("¿Cuál es su nombre? ")
  print("Hello, World!" + name)
  #Haciendo uso de format
  print("Hello, World! {}".format(name))
  #Haciendo uso de f-string
  print(f"Hello, World! {name}")

if __name__ == "__main__":
  main()