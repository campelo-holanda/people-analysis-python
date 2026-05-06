from datetime import datetime
dados = {}
dados['nome'] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
dados['idade']= datetime.now().year - nascimento
dados['CTPS'] = int(input("Seu CTPS (0 não tem): "))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input("Ano de contratação: "))
    dados['Salário'] = int(input("Seu salário: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('=-'*30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
