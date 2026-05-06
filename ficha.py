def ficha(n=0, g=0):
    print("FICHA DO JOGADOR")
    return f'O jogador {n} fez {g} gols no campeonato'

nome = str(input("Nome do jogador: "))
if nome.strip() == "":
    nome = "<desconhecido>"
gols = (input("Quantos gols: "))
if gols.isdigit():
    gols = int(gols)
else:
    gols = 0
res = ficha(nome, gols)
print(res)

