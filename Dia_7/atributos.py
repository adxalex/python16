class Pajaro:

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('negro', 'Tucan')

#print(f'Mi pajaro es de {mi_pajaro.color} y es un {mi_pajaro.especie}')

class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco', 4)

#print(f'Mi casa es de color {casa_blanca.color} y tiene {casa_blanca.cantidad_pisos}')

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

#print(f'{Cubo.caras} es {cubo_rojo.color}')

#--------Ejercio 3---------------

class Personaje:
    real = False
    def __init__(self, especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("humano", True, 17)

print(f'el personaje harry potter es un personaje {Personaje.real} porque es {harry_potter.magico} y eso no existe. Su especie es {harry_potter.especie} y tiene {harry_potter.edad}')