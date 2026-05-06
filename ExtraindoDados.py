lista = []
contador = 0
while True:
    n = int(input("Digite um número: "))
    contador += 1
    lista.append(n)
    r = input(('Quer continuar [S ou N]? ')).lower()
    if r == 'n':
        break
print('=-' * 20)
if 5 in lista:
    print('5 está na lista')
else:
    print('5 não está na lista')
print(f'Foram digitados {contador} números')
inverso = reversed(sorted(lista))
print(list(inverso))

