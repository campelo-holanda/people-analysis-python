matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
maior = 0
scol = 0
# matriz

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}/{c}: '))
print('=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:5^}]',end='')
    print() 
      
# soma dos pares
for l in matriz:
    for valor in l:
        if valor % 2 == 0:
            somapares += valor
print('=-' * 10)
print(f'A soma dos números pares é {somapares}')

# soma da coluna

for l in range(0, 3):
    scol += matriz[l][2]
 
print(f'A soma da terceira coluna é {scol}')

# maior valor da segunda linha
for c in range(0, 3):
    if c == 0:
       maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')



      

      



