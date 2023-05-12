import resp as resp


def potencia(base, expoente):
    resp = 1
    for i in range(expoente):
        resp *= base
    #return resp
        print(resp)
base = int(input('digite um valor'))
expoente = int(input('digite um valor'))
potencia(base, expoente)
