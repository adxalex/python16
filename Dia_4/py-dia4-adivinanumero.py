from random import *

# Pregunta su nombre
secreto = choice(range(1,100))
#secreto = 60
nombre = input(f'¿cuál es tu nombre? ')
#nombre = "Adixon"

print(f'Hola {nombre} Bienvenid@ a mi primer juego, es sencillo, pero se que te va a gustar \n \nTe cuento que he estado pensando en un número entre 1 y 100 y creo que tu seras capaz de adivinarlo. \n \nTienes 8 intentos' )

#numero = int(input(f'introduce el numero: '))
#numero = 60

intento = 0

#for i in intentos:
while intento < 8:
    numero = int(input(f'introduce el numero: '))
    if numero < 1 or numero > 100:
        print(f'{nombre} te dije que entre 1 y 100. Te quedan {7 - intento} intentos' )
        intento += 1

    elif numero < secreto and numero > 0:
        print(f'{nombre} el número que pensé es mayor. Te quedan {7 - intento} intentos')
        intento += 1

    elif numero > secreto and numero <= 100:
        print(f'{nombre} el número que pensé es menor. Te quedan {7 - intento} intentos')
        intento += 1

    elif numero == secreto:
        print(f'Felicidades {nombre} no creí que pudieras hacerlo tan solo en {intento} intentos')
        break
else:
    print(f'se acabaron los intentos')

print(f'El número que pensé era {secreto}')



# Dice: Juan he penasdo un numero entre 1 y 100 y tiene 8 intentos para adivinar
# Cuando coloque el numero va a responder, de acuerdo con las siguientes condiciones
    # si es menor a 1 o superior a 100 = no esta permitido
    # si es menor al que penso el programa = incorrecto, pensaste uno menor al que yo tengo
    # si es menor al que penso el programa = incorrecto, pensaste uno mayor al que yo tengo
    # Ganaste= te tomo x cantidad de intentos.
    # finaliza cuando gane o se le acaben los 8 intentos