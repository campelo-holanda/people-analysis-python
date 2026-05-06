from random import randint
jogo = []
jogos = []
quantidade = int(input("Quantos jogos você vai querer? "))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            contador += 1
        if contador == 6:
            break    
    jogos.append(jogo[:])
    jogo.clear()
    total += 1
for n in jogos:
    print(n)
    






