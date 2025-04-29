# 1. Crea clase Persona:
#      - __init__(self, nombre: str, edad: int)
#      - presentarse(self) -> str: devuelve "Hola, soy <nombre> y tengo <edad> años."
# 2. Instancia dos objetos y llama a presentarse().

class Persona:
  def __init__(self, nombre: str, edad: int):
    self.nombre = nombre
    self.edad = edad
    
  def presentarse(self):
    return f"Hola, soy {self.nombre} y tengo {self.edad} años."

def main():
  persona1 = Persona("Juan", 25)
  persona2 = Persona("Maria", 30)
  print(persona1.presentarse())
  print(persona2.presentarse())

if __name__ == "__main__":
  main()