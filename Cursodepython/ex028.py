import random
from time import sleep
print('-=-'*30)
print('O computador pensará em um número entre 0 e 5. Você consegue descobrir que número é esse?')
print('-=-'*30)
guess = int(input('Que número o computador escolheu? ')) #O jogador tenta adivinhar
pick = random.randrange(0, 5) #faz o computador pensar
print('Processando...')
sleep(2) #faz o programa demorar um pouco
print(f'O computador escolheu o número: {pick}')
if guess == pick:
    print('Parabéns, você acertou!')
else:
    print('Desculpa, não foi dessa vez...')




