#print("El nombre de tu cerveza\nes '" + input("Que ciudad te gustaria visitar de nuevo?: ") + " " + input("Cual es tu color favorito?: ") + "'\nFelicitaciones!")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)