# 1. Crea clase Persona:
#      - __init__(self, nombre: str, edad: int)
#      - presentarse(self) -> str: devuelve "Hola, soy <nombre> y tengo <edad> años."
# 2. Instancia dos objetos y llama a presentarse().

#En Python, cada objeto tiene dos métodos especiales para representar su contenido como cadena:

#__repr__: está pensado para una representación “oficial” del objeto, útil para depuración. Si no existe __str__, print(objeto) caerá de vuelta a __repr__.

#__str__: da la representación “amigable” que verá el usuario cuando hagas print(objeto) o str(objeto).

class Persona:
  def __init__(self, nombre: str, edad: int):
    self.nombre = nombre
    self.edad = edad
    
  def presentarse(self):
    return f"Hola, soy {self.nombre} y tengo {self.edad} años."

  def __str__(self) -> str:
      # Aquí usas tu método presentarse para la cadena de salida
      return self.presentarse()
    
def main():
  persona1 = Persona("Juan", 25)
  persona2 = Persona("María", 30)
  print(persona1.presentarse())
  print(persona2.presentarse())

if __name__ == "__main__":
  main()