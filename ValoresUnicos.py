lista = []
n = ''
while n != 999:
    n = int(input("Digite um valor[999 para sair]: "))
    if n in lista:
        lista.remove(n)
    if n == 999:
        break
    lista.append(n)
print(sorted(lista))


