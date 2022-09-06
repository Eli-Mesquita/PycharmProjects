from random import randint
from time import sleep
print('-=- JOKENPO -=- \n'
      '[ 0 ] PEDRA \n'
      '[ 1 ] PAPEL \n'
      '[ 2 ] TESOURA')
player = int(input('Qual é a sua jogada? '))
jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-'*10)
print(f'O computador escolheu {jogadas[pc]}')
print(f'O jogador escolheu {jogadas[player]}')
print('-=-'*10)
if pc == 0: #PEDRA
      if player == 0: #PEDRA
            print('EMPATE')
      elif player == 1: #PAPEL
            print('JOGADOR VENCE!!!')
      elif player == 2: #TESOURA
            print('COMPUTADOR VENCE!')
      else:             #ERRO
            print('JOGADA INVÁLIDA!')
elif pc == 1: #PAPEL
      if player == 0:  # PEDRA
            print('COMPUTADOR VENCE!')
      elif player == 1:  # PAPEL
            print('EMPATE')
      elif player == 2:  # TESOURA
            print('JOGADOR VENCE!!!')
      else:  # ERRO
            print('JOGADA INVÁLIDA!')

elif pc == 2: #TESOURA
      if player == 0:  # PEDRA
            print('JOGADOR VENCE!!!')
      elif player == 1:  # PAPEL
            print('COMPUTADOR VENCE!')
      elif player == 2:  # TESOURA
            print('EMPATE')
      else:  # ERRO
            print('JOGADA INVÁLIDA!')
