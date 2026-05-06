def LeiaInt(c):
    while True:
        try:
            n = int(input(c))
        except (ValueError, TypeError):
            print("Digite apenas número inteiro")
            continue
        except KeyboardInterrupt:
            print("O usuário preferiu não continuar.")
            return 0
        else:
            return n
        


def LeiaFloat(c):
    while True:
        try:
            n = float(input(c))
        except (ValueError, TypeError):
            print('Digite apenas número real.')
            continue
        except KeyboardInterrupt:
            print("O usuário preferiu não continuar.")
            return 0
        else:    
            return n
        
n1 = LeiaInt("Digite um inteiro: ")
n2 = LeiaFloat("Digite um real: ")
print(f'Número inteiro é {n1} e número real é {n2}')

