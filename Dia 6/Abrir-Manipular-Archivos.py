#Abro el archivo y lo meto en una variable
mi_archivo = open('Prueba.txt')

# #leo un archivo
# print(mi_archivo.read())

#Cada vez que lea una linea python se queda en el punto leido
una_linea = mi_archivo.readline()
una_linea = mi_archivo.readline()
print(una_linea)

# #el rstrip omite el salto de linea
# una_linea = mi_archivo.read()
# print(una_linea.rstrip())
#
# # Puedes usar metodos de sprint como "upper" para pasar a mayuscula
# una_linea = mi_archivo.read()
# print(una_linea.upper())
#
# #Podemos hacer un for con cada linea del archivo
#
# for l in mi_archivo:
#     print("Aqui dice: " + l)
#
# # Las lineas se imprimen como una lista
# todas = mi_archivo.readlines()
# print(todas)

#Siempre el close al final para que no quede en memoria
mi_archivo.close()