#lo hacemos como set dado que set no toma los valores repetidos.
def orden_alfa(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(orden_alfa("entretenido"))