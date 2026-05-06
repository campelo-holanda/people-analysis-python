def ajuda(k):
    return help(k)


while True:
    p = str(input("Biblioteca ou função[FIM para sair]: "))
    if p.upper() == "FIM":
        break
    else:
        ajuda(p)
