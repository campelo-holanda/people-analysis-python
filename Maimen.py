maior = 0
menor = 0
for c in range(10):
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print(maior)
print(menor)