def maior(*valores):
    if valores:
        maior = valores[0]
        for v in valores:
            if v > maior:
                maior = v
        print(maior)
    else:
        print("Está vazio!")

maior()

