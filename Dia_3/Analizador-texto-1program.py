
#texto = "En la casa de mi perro, los huesos son color azul, porque el los busca mientras mastica chicle, por eso aprendo python"
#letra1 = "a"
#letra2 = "B"
#letra3 = "c"

textomayu = input("introduce un texto: ")
texto = textomayu.lower()
letra1low = input("introduce una letra: ")
letra2low = input("introduce otra letra: ")
letra3low = input("introduce una última letra: ")

separador = texto.split(" ")
mi_list = list(separador)


#Cuantas veces aparece cada Letra que escribio

cuenta_1 = texto.count(letra1low)
cuenta_2 = texto.count(letra2low)
cuenta_3 = texto.count(letra3low)

print(f"La primera letra que colocaste está '{cuenta_1}' veces en el texto")
print("    ")
print("    ")
print(f"La segunda letra que colocaste está '{cuenta_2}' veces en el texto")
print("    ")
print("    ")
print(f"La tercera letra que colocaste está '{cuenta_3}' veces en el texto")

# Cantidad de Palabras que hay en el texto

print("    ")
print("    ")

total_palabras = len(mi_list)
print("La cantidad total de palabras es: ",total_palabras)

print("    ")
print("    ")

#Cual es la primera letra del texto y la última
primera = texto[0]
print("La primera letra del texto es: ", primera)

print("    ")
print("    ")

ultima = texto[-1]
print("La última letra del texto es: ", ultima)

print("    ")
print("    ")

#Invierte todas las palabras
mi_list.reverse()
texto_invertido = ' '.join(mi_list)
print(f"El texto invertido es: {texto_invertido}")

print("    ")
print("    ")

# Aparece la palabra Python?
pythontext = 'python' in texto
dicpy = {True:'Si', False:'No'}
print(f"la palabra 'Python' {dicpy[pythontext]} se encuentra en el texto")
#pythontext = str(pythontext)
#print(dicpy[pythontext])
