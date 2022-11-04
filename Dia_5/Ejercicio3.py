def validacion(*args):
    num_antes = 1
    estado = ''
    for num in args:
        if num == 0:
            if num == num_antes:
                estado = True
                break
            else:
                num_antes = num
        else:
            num_antes = num
        estado = False
    return estado

print(validacion(1,0,5,5,7,9,0))


def ceros_vecinos(*args):

    contador = 0

    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(1,2,8,7,8,9,0,0,7,1,5,0,3,0,4,0))