from datetime import datetime
def voto(ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return f"Você tem {idade} e Voto negado"
    elif 16 <= idade < 18 or idade > 65:
        return f"Você tem {idade} e Voto opcional"
    else:
        return f"Você tem {idade} e Voto obrigatorio"

ano = int(input("Em que ano você nasceu? "))
resp = voto(ano)
print(resp)


