lista = []

for c in range(0, 10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

maior = None
segundo = None

for n in lista:
    if maior is None or n > maior:
        segundo = maior
        maior = n
    elif n != maior and(segundo is None or n > segundo):
        segundo = n

print(f"Segundo maior é {segundo}")
