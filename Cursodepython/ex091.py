from time import sleep
from random import randint
from operator import itemgetter
player = {"Jogador 1": randint(1, 6),
          "Jogador 2": randint(1, 6),
          "Jogador 3": randint(1, 6),
          "Jogador 4": randint(1, 6), }
ranking = list()
print('Rolando os dados...')
for k, v in player.items():
    sleep(1)
    print(f'O {k} tirou o número {v}')
ranking = sorted(player.items(), key=itemgetter(1), reverse=True)
sleep(1)
print('    Criando ranking de jogadores...')
for c, p in enumerate(ranking):
    sleep(1)
    print(f'    {c+1}° lugar {p[0]} com {p[1]}')
