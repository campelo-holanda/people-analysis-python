from time import sleep
def linha():
    print('-' * 20)

def perso(i, f, p):
    if p > 0:
        for a in range(i, f+1, p):
            print(a, end=' ', flush=True)
        print('FIM!')
        sleep(0.5)
    elif p == 0:
        print("Passo não pode ser 0!")
    else:
        for a in range(i, f-1, p):
            print(a, end=' ', flush=True)
        print('FIM!')
        sleep(0.5)

linha()
print('De 1 até 10 de 1 em 1: ')
perso(1, 10, 1)
sleep(0.5)
linha()
print("De 10 até 1 de 2 em 2: ")
perso(10, 0, -2)
linha()
print("Uma contagem personalizada: ")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
print("Iniciando contagem: ")
perso(i, f, p)
linha()