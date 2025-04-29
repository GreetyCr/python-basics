# 1. Imprime "Hello, World!"
# 2. Pide al usuario su nombre y salúdalo: "¡Hola, <nombre>!"

def main():
  name = input("¿Cuál es su nombre? ")
  print("Hola " + name)
  #Haciendo uso de format
  print("Hola {}".format(name))
  #Haciendo uso de f-string
  print(f"Hola {name}")

if __name__ == "__main__":
  main()