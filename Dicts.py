Ficha = {}
Nome = str(input("Nome: "))
Media = float(input("Média: "))
Ficha['Nome'] = Nome
Ficha['Media'] = Media
print('=-'*10)
print(f'O  nome é igual a {Ficha['Nome']}')
print(f'A média é igual a {Ficha['Media']} ')
if Ficha['Media'] >= 7:
    print("Aprovado")
else:
    print("Reprovado")
print(Ficha)
