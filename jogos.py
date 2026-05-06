jogos = {}
lista = []
jogos['Nome'] = str(input("Qual o nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogos['Nome']} jogou: "))
for c in range(partidas):
    gols = int(input(f"Quantos gols na {c + 1}º partida: "))
    lista.append(gols)


soma = 0
for c in lista:
    soma = soma + c

jogos['gols'] = lista[:]
jogos['total'] = soma

print(jogos)

print('=-' * 30)

for k, v in jogos.items():
    print(f'O campo {k} tem o valor {v}')

print('=-' * 30 )

cursor = 0
for p in range(partidas):
    print(f'  => Na partida {p}, fez {jogos['gols'][cursor]}')
    cursor = cursor + 1
print(f'Foi um total de {soma}')



    
    

    





