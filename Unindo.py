pessoas = {}
ListaPessoas = []
Mulheres = []
Acima = []
resposta = ''
soma = 0
while resposta != 'N':
    pessoas['nome'] = input("Nome: ")
    sexo = str(input("Sexo: ")).upper()
    if sexo in 'MmFf':
        pessoas['sexo'] = sexo
    else:
        while True:
            print("Erro! Somente M ou F")
            sexo = str(input("Qual seu sexo: "))
            if sexo in 'MmFf':
                break
        pessoas['sexo'] = sexo
    pessoas['idade'] = int(input("Idade: "))
    ListaPessoas.append(pessoas.copy())
    pessoas.clear()
    resposta = input("Quer continuar S ou N: ").upper()
    if resposta not in "SN":
        while True:
            print("Resposta inválida. Somente S ou N.")
            resposta = input("Quer continuar S ou N: ").upper()
            if resposta in 'SN':
                break
    
print('=-'*30)
print(f"A) Foram cadastradas {len(ListaPessoas)} pessoas.")   
for pessoa in ListaPessoas:
    soma = soma + pessoa['idade']
media = soma/ len(ListaPessoas)
print(f"B) Média das idades: {media:.2f}")


for m in ListaPessoas:
    if m['sexo'] == 'F':
        Mulheres.append(m['nome'])
if len(Mulheres) > 0:
    print(f'C) Mulheres cadastradas foram {Mulheres}')
else:
    print(f'Não teve mulheres')

for p in ListaPessoas:
    if p['idade'] > media:
        Acima.append(p['nome'])
print(f'C) Pessoas com idade acima da média: {Acima}')





