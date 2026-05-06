def aumentar(n, t):
    porcentagem = (t/100) * n
    aum = n + porcentagem
    return f'Aumentando {t}% temos {aum}'

def diminuir(n, t):
    porcentagem = (t/100) * n
    dim = n - porcentagem
    return f'Diminuindo {t}% temos {dim}'

def dobro(n):
    return n * 2

def metade(n):
    return n / 2

