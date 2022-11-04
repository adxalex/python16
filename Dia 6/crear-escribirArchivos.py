# # modo solo lectura
#archivo = open('pruebas.txt', 'r')

# # modo escritura (va a sobreescribir everything lo que este en el archivo)
# archivo = open('pruebas.txt', 'w')

# # Este metodo es muy usado para logs ya que escribe la linea al final
# archivo = open('pruebas.txt', 'a')
#
# archivo.write('usado para logs')

# para poder escribir tiene que estar en modo escritura
# archivo.write('Soy el nuevo texto')

#escribe everything en una misma linea pegada (no es muy util).
# archivo.writelines(['hola', 'mundo','aqui','estoy'])

# Si quiero hacerlo por diferentes lineas puedo usar un for.

# lista = ['hola', 'mundo','aqui','estoy']
#
# for p in lista:
#     archivo.writelines(p + '\n')

# # El siguiente ejemplo requiere abrir y cerrar el archivo para poder leerlo despues de que lo editmos
# mi_archivo = open('mi_archivo.txt', 'w')
#
# mi_archivo.write('Nuevo texto')
#
# mi_archivo.close()
#
# mi_archivo = open('mi_archivo.txt')
#
# print(mi_archivo.read())

# mi_archivo = open('pruebas.txt', 'a')
#
# mi_archivo.write("Nuevo inicio de sesión")
#
# mi_archivo.close()
#
# mi_archivo = open('pruebas.txt')
#
# print(mi_archivo.read())
#-------------------------------------------------------------------
# mi_archivo = open('registro.txt', 'a')
#
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
#
# for ele in registro_ultima_sesion:
#     mi_archivo.writelines(ele + '\t')
#
# mi_archivo.close()
#
# mi_archivo = open('registro.txt')
#
# print(mi_archivo.read())