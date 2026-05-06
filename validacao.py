def LeiaInt(c):
    ok = False
    valor = 0
    while True:
        n = str(input(c))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Valor incorreto!')
        if ok:
            break
    return valor
# Programa principal
p = LeiaInt('Digite um número: ')

