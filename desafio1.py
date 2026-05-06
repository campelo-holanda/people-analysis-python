minimo = 400
estoque = int(input("Qual o estoque? "))
if estoque < minimo:
    print("Temos que comprar urgente!")
elif minimo <= estoque <= 480:
    print("Está na hora de comprar")
else:
    print('Nada a informar')
    