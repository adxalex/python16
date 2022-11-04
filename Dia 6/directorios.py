import os
from pathlib import Path

# Directorio Actual
ruta = os.getcwd()

# Cambiar la ruta del directorio que queremos entrar
#ruta = os.chdir('C:\\adx\\programador\\python\\Curso\\Dia 6\\testdirectorio')

#Crear una carpeta desde Python
#ruta = os.makedirs('C:\\adx\\programador\\python\\Curso\\Dia 6\\testdirectorio\\otra')


#ruta = 'C:\\adx\\programador\\python\\Curso\\Dia 6\\testdirectorio\\otra\\'

# Me trae el nombre del archivo que hay dentro de la carpeta
elemento = os.path.basename(ruta)
print(elemento)

# Me trae el directorio
# elemento = os.path.dirname(ruta)

# Trae nombre del archivo + directorio pero como una tupla
#elemento = os.path.split(ruta)
# print(elemento)

# borrar un directorio con python (el directorio tiene que estar vacio)
# os.rmdir('C:\\adx\\programador\\python\\Curso\\Dia 6\\testdirectorio\\otra')

#print(elemento)

# Abre un archivo en un directorio distinto de donde estas parado.
# otro_archivo = open('C:\\adx\\programador\\python\\Curso\\Dia 6\\testdirectorio\\otro.txt')

# print(otro_archivo.read())

# Formateamos para que la ruta pueda ser leida por cualquier sistema operativo importando el modulo pathlib
#carpeta = Path('C:/adx/programador/python/Curso/Dia 6/testdirectorio')
#archivo = carpeta / 'otro.txt'

#mi_archivo = open(archivo)
#print(mi_archivo.read())