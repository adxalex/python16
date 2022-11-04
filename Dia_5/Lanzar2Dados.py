import random


'''Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados (la función debe retornar dos valores resultado, que se encuentren entre 1 y 6).'''
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)

#print(lanzar_dados())

'''Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:'''

def evaluar_jugada(dado1,dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif suma_dados > 6 and suma_dados < 10:
        return f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    else:
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'

dados = lanzar_dados()
print(dados)
resultado = evaluar_jugada(dados[0], dados[1])
print(resultado)
