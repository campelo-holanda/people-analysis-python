Lista = []
maior = 0
menor = 0
for c in range(1, 6):
    n = int(input(f"Digite o [{c}/5]: "))
    Lista.append(n)
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f"O maior valor é {maior} nas posições ", end='')
for i, v in enumerate(Lista):
    if v == maior:
        print(i,'...') 
print(f"O menor valor é {menor}, nas posições ", end='')
for i, n in enumerate(Lista):
    if n == menor:
        print(f'{i}...')
        
