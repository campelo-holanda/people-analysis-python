ficha = []
while True:
    aluno = str(input('Nome: '))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([aluno, [nota1, nota2], media])
    resposta = str(input("Quer continuar [S/N]: "))
    if resposta in 'Nn':
        break
print(ficha)
