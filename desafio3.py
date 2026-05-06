# Mínimo

MinimoMaterial = 400
MinimoImportado = 80
MinimoOutros = 400
MinimoMedicamentos = 400
# Margem

MargemMaterial = MinimoMaterial + ((30 / 100) * MinimoMaterial ) 
MargemImportado = MinimoImportado + ((50 / 100) * MinimoImportado ) 
MargemOutros = MinimoOutros + ((15 / 100) * MinimoOutros ) 
MargemMedicamentos = MinimoMedicamentos + ((40 / 100) * MinimoMedicamentos ) 
 # Estrutura do codigo

while True:
    print('''
          [1] Material
          [2] Importado
          [3] Outros
          [4] Medicamentos
          [5] Sair ''')
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        quantidade = int(input("Digite a quantidade de Material: "))
        if quantidade < MinimoMaterial:
            print("Temos que comprar urgente")
        elif quantidade >= MinimoMaterial and quantidade <= MargemMaterial:
            print("Temos que comprar")
        print('nada a informar')
    elif opcao == 2:
        quantidade =  int(input("Digite a quantidade de importado: "))
        if quantidade < MinimoImportado:
            print("Temos que comprar urgente")
        elif quantidade >= MinimoImportado and quantidade <= MargemImportado:
            print('Temos que comprar')
        print("Nada a informar")
    elif opcao == 3:
        quantidade =  int(input("Digite a quantidade de outros: "))
        if quantidade < MinimoOutros:
            print("Temos que comprar urgente")
        elif quantidade >=MinimoOutros and quantidade <= MinimoOutros:
            print("Temos que comprar")
        print("Nada a informar")
    elif opcao == 4:
        quantidade = int(input("Digite a quantidade de Medicamentos: "))
        if quantidade < MargemMedicamentos:
            print("Temos que comprar urgente")
        elif quantidade >= MinimoMedicamentos and quantidade <= MargemMedicamentos:
            print("Temos que comprar")
        print("Nada a informar")
    elif opcao == 5:
        break
    