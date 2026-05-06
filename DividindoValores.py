lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = input("Quer continuar [S ou N]? ").upper()
    if r == 'N':
        break
print('=-' * 20)
print(f'lista normal: {lista}')
print(f'pares: {pares}')
print(f'Ímpares: {impares}')

