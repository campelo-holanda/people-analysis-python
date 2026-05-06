from random import randint
def sorteia(lista):
    for c in range(5):
       lista.append(randint(1, 10)) 

def soma_par(lista):
    soma = 0
    for e in lista:
        if e % 2 == 0:
            soma = soma + e
    print(f'A soma dos números pares na lista {lista} = {soma}')
        


numeros = []
sorteia(numeros)
print(numeros)
soma_par(numeros)