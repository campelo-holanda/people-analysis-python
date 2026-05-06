def notas(*notas, sit=False):
    dic = {}
    maior = notas[0]
    menor = notas[0]
    dic['Quantidade'] = len(notas)
    for p in notas:
        if p > maior :
            maior = p
        if p < menor:
            menor = p
    dic['maior'] = maior
    dic['menor'] = menor
    media = sum(notas) / len(notas)
    dic['média'] = media
    if sit:
        if media <= 5:
            dic['situação'] = 'Ruim'
        elif media > 5 and media <=6.9:
            dic['situação'] = 'Razoável'
        else:
            dic['situação'] = 'Boa'
    return dic
        
resp = notas(5.5, 9.5, 10, 6.5, sit=False)
print(resp)

        
    

