def contar_primos(numero):

#el primer num de la lista arranca en 2 porque es el primer primo
    primos = [2]
#el segundo numero que se agregara a la lista pasando por el else del while
    iteracion = 3
# si es menor a 2 no hay ningun primo, por eso se retorna 0
    if numero < 2:
        return 0

#
    while iteracion <= numero:
# rango 3 (primer primo),iteracion (arramca en 3 pero luego va a ir aumentando de 2 en 2) y 2 porque cada 2 numeros tenemos un par, los pares por encima de 2 (el primero seria 4, no son primos.
        for n in range(3,iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(50))