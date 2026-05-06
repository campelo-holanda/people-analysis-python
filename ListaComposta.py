lista = []
principal = []
contador = 0
maior = menor = 0
while True:
    nome = str(input("Nome:  "))
    peso = int(input("Peso: "))
    lista.append(nome)
    lista.append(peso)
    contador += 1
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()

    r = input((f'Quer continuar? [S ou N]: ')).upper()
    if r == 'N':
        break
print(principal)
print(f'O maior peso é {maior}kg')
print(f'O menor é de {menor}kg')
