from time import sleep
from random import sample
n = int(input('Quantos jogos você quer sortear? '))
jogo = [sample(range(1, 61),6) for c in range(0, n)]
for c in range(n):
    sleep(1)
    print(f'Jogo {c+1}: {sorted(jogo[c])}')
