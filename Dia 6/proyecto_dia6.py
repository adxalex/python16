# dar la bienvenida al usuario

#informar la ruta de acceso del directorio donde se encuentra nuestra carpeta de recetas

# Informa cuantas recetas totales hay

# NOTAS:
#
# - Hacer un loop while para que el usuario presiona una letra y se reinici el menu de opciones y el loop termina cuando elija opcion 6 (finalizar)
# - EL menu debe estar dentro de ese loop while
# - Cada vez que se termina una ejecucion que se limpie la pantalla con system('cls')
# - Tendras que buscar nuevos metodos no vistos en las clases, hay que buscar documentacion.
# - Crea todas las funciones que sean necesarias. ejemplo: "elegir categoria"
# - Realizar un diagrama de flujo.
#
# # elegir opciones
# [1] Leer receta
#
# - Pregunta que categoria elige
# - Que receta quiere leer y le muestra el contenido
#
# [2] Crear receta
#
# - Pregunta que categoria elige
# - escribe el nombre
# - Escribe el contenido de la nueva receta
# - El programa crea el archivo de la nueva receta
#
# [3] crear categoria
#
# - Pregunta que categoria quieres crear.
# - Se crea la carpeta con la nueva categoria
#
# [4] eliminar receta
# - Pregunta que categoria elige (ubicacion de la receta que quiere eliminar)
# - Pregunta que receta quiere
# - Elimina la receta
#
# [5] eliminar categoria
# - Pregunta que categoria elige
# - Elimina la categoria elegida
#
# [6] finalizar programa
# - Finaliza la ejecuccion del codigo.
# -------------------------------------------------------------Fin de comentarios-----------------------------------------
import glob
import os
import pathlib
from os import system
from os import remove
from os import rmdir
from pathlib import Path, PureWindowsPath

dir_base = os.getcwd()
ruta = Path('Recetas')
#ruta = 'Recetas'

directorio_recetas = dir_base / ruta

# Muestra el listado de carpetas disponibles (subcarpetas) = categorias
def categorias(ruta):
    lista_categoria = []
    for cate in ruta.glob("*"):
        lista_categoria.append(os.path.basename(cate))
    return (lista_categoria)

# Cuenta por categoria la cantidad de archivos dentro de ellas mismas
def cantidad_recetas(ruta, lista_categoria):
    cuenta_recetas = 0
    for categoria in lista_categoria:
        for path in pathlib.Path(ruta / categoria).iterdir():
            if path.is_file():
                cuenta_recetas +=1
    return cuenta_recetas

# entra en una categoria y lista los archivos .txt que hay dentro = recetas
def listar_receta(ruta, categoria):
    listar_recetas = []
    #archivos = glob.glob(ruta + categoria + '/*/*')
    for receta in os.listdir(Path(ruta)/(categoria)):
        if '.txt' in receta:
            listar_recetas.append(receta)
    return listar_recetas



cantidad_recetas = (cantidad_recetas(ruta,(categorias(ruta))))
opcion_seleccionada = 0
#######################################------------------EMPIEZA EL PROGRAMNA-----------##################################
#nombre = input('Hola, por favor introduce tu nombre: ')
nombre = 'Adixon'
#print(f'Hola {nombre}. Bienvenido a nuestro recetario, ubicado en {directorio_recetas}, el cual cuenta con {cantidad_recetas} recetas.')

def menu():

    lista_opciones = [1,2,3,4,5,6]
    opcion = int(input(f'\n\n¿Que quieres hacer? \n(1) Leer una receta. \n(2) Crear una receta. \n(3) Crear una categoria. \n(4) Eliminar una receta. \n(5) Eliminar una categoría. \n(6) Salir del programa.\n\nEscribe el numero de la opción que quieres: '))


    while opcion not in lista_opciones:

        print(f'{nombre} por favor ingresa una opción válida \n')
        opcion = int(input(f'\n\n¿Que quieres hacer? \n(1) Leer una receta. \n(2) Crear una receta. \n(3) Crear una categoria. \n(4) Eliminar una receta. \n(5) Eliminar una categoría. \n(6) Salir del programa. \n\nEscribe el numero de la opción que quieres: '))
    else:
        return int(opcion)

# opcion_seleccionada = menu()
#print(opcion_seleccionada)

while opcion_seleccionada != 6:
    opcion_seleccionada = menu()
    opcion = opcion_seleccionada
    categoria_seleccionada = ''
    receta_seleccionada = ''
    mi_receta = ''
    nuevo_archivo = ''
    nueva_receta= ''
    lista_categorias = categorias(directorio_recetas)

#Opcion 1: leer receta.
    if opcion == 1:

        categoria_seleccionada = input(f'\nMuy bien, vamos a leer la receta. Por favor escribe el nombre de la categoria que quieres ver\n\n {lista_categorias}: ')
        os.chdir(Path(ruta) / (categoria_seleccionada))
        receta_seleccionada = input(f'\nPor favor escribe el nombre de la receta que quieres ver\n\n {listar_receta(ruta, categoria_seleccionada)}: ')
        mi_receta = open(receta_seleccionada)
        mi_receta = mi_receta.read()
        print(f'{mi_receta} \n')
        os.system("cls")

#Opcion 2: Crear Receta
    elif opcion == 2:

        categoria_seleccionada = input(f'\nMuy bien, vamos a crear una nueva receta. Por favor escribe el nombre de la categoria donde vas a guardar tu receta\n\n {lista_categorias}')
        os.chdir(Path(ruta) / (categoria_seleccionada))
        nuevo_archivo = input('\ningresa el nombre de la receta que quieres crear: ')
        nueva_receta = open(nuevo_archivo, "w")
        nueva_receta.write(input('\nEscribe el contenido de tu receta: '))
        os.system("cls")

#Opcion 3: Crear categproa
    elif opcion == 3:
        categoria_seleccionada = input(f'\nMuy bien, vamos a crear una nueva Categoria. Por favor escribe el nombre de la nueva categoria\n\n')
        os.makedirs(Path(ruta) / (categoria_seleccionada))
        os.system("cls")
#Opcion 4: ELiminar receta
    elif opcion == 4:
        categoria_seleccionada = input(f'\nMuy bien, vamos a eliminar una receta. Primero, elijamos la categoria de la receta que quieres eliminar\n\n {lista_categorias}: ')
        os.chdir(Path(ruta) / (categoria_seleccionada))
        receta_seleccionada = input(f'\nPor favor escribe el nombre de la receta que quieres eliminar\n\n {listar_receta(ruta, categoria_seleccionada)}: ')
        remove(receta_seleccionada)
        os.system("cls")
#Opcion 5: Eliminar Categoria
    elif opcion == 5:

        categoria_seleccionada = input(f'\nMuy bien, vamos a eliminar una receta. Primero, elijamos la categoria de la receta que quieres eliminar\n\n {lista_categorias}: ')
        os.chdir(Path(ruta) / (categoria_seleccionada))
        rmdir(categoria_seleccionada)
        os.system("cls")
else:
# Opcion 6
    print(f'Hasta pronto')

