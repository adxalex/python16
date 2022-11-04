#AHORCADO

'''
1- Elegir palabra secreta (random).
2- Mostrar la cantidad de los guiones bajos = a la cantidad de letras (puede ser con len())
3- El jugador entra en un turno pone una letra y si la letra está
el programa le devuelve las letras en la ubicacion de los guiones algo asi: _d__o_ = dijo D y O de Adixon
sino esta, pierde un turno y le diremos la cantidad de vidas que le quedan (maximo 6)
4.- Si lo lgora "gana" si se acaban las vidas pierde.

Tips:
- Import Choice (elegir palabra)
- Funciones: Pedir letra - Validar letra - chequear letra - ver si gano.
- Primero escribe las funciones y luego el codigo que las implementa ordenadamente

'''

from random import choice

vidas = 6
lista_palabra = ['manzana','cabeza','plata','tanedora']
#lista_palabra = ['carteluo','computador','plato','cabezon']
palabra = list(choice(lista_palabra))

def valida_letra(letra_valida):
    lista_letra = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

    while letra_valida not in lista_letra:
        print(f'{nombre} debes ingresar una letra: ')
        letra_valida = input()
    else:
        pass
    return letra_valida

def valida_letra_en_palabra(letra_valida,palabra):
    estado = ''
    if letra_valida in palabra:
        estado = True
    else:
        estado = False
    return estado

def palabra_a_guion(palabra):
    espacio_palabra = []
    for letra in palabra:
        letra = '_'
        espacio_palabra.append(letra)
        con_guion = "".join(espacio_palabra)
    return con_guion


contruccion_palabra = list(palabra_a_guion(palabra))
nombre = input(f'Por favor dime tu nombre: ')
print(f' Hola {nombre}, juguemos al ahorcado, tu palabra es: {palabra_a_guion(palabra)}')

while vidas > 0:

    letra = valida_letra(input(f'Por favor ingresa una letra: '))

    if valida_letra_en_palabra(valida_letra(letra), palabra) == True:
#MANZANA
        for iteracion in palabra:
            if iteracion == letra:
                letra = iteracion
                #contruccion_palabra
            contruccion_palabra[palabra.index(iteracion)] = iteracion
        print(contruccion_palabra)

        if contruccion_palabra == palabra:
            print(f'Ganaste {nombre}, ¡buen trabajo!')

        else:
            #letra = valida_letra(input(f'Por favor ingresa una letra: '))
            pass

    else:
        vidas -= 1
        print(f'te quedan {vidas} vidas')

        if vidas < 1:
            print(f'Lo siento {nombre} has perdido :(, tu palabra era {palabra}')
            break

        else:
            #letra = valida_letra(input(f'Por favor ingresa una letra: '))
            pass