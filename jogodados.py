from random import randint
from operator import itemgetter
ranking = {}
dic = {'jogador 1': randint(1, 6),
       'jogador 2': randint(1, 6),
       'jogador 3': randint(1, 6),
       'jogador 4': randint(1, 6)}
for k, v in dic.items():
    print(f'{k}: tirou {v}')
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
print('=-'*20)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    



