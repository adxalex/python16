# Elimina duplicados y el mas alto lista [1,2,15,7,2] debe devolver [1,2,7].

lista_numeros = [1,2,15,7,2,8]

def reducir_lista(lista):
    sindupli = []
    for n in lista:
        if n not in sindupli:
            sindupli.append(n)
    sindupli.remove((max(sindupli)))
    return sindupli


def promedio(lista):
    promedio = 0
    for n in lista:
        promedio += n
    promedio = promedio / len(lista)
    return promedio

print(reducir_lista(lista_numeros))
reducido = (reducir_lista(lista_numeros))
print(promedio(reducido))

# que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
