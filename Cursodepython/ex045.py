import random
from time import sleep
print('-=- JOKENPO -=- \n'
      '[ 1 ] PEDRA \n'
      '[ 2 ] PAPEL \n'
      '[ 3 ] TESOURA')
player = int(input('Qual é a sua jogada? '))
pc = random.randrange(1,3)
if pc == 1:
    print('Computador escolheu PEDRA')
    if player == 1:
            print('Jogador escolheu PEDRA\n'
                  'PEDRA com PEDRA faísca\n'
                  'O JOGO EMPATOU!')
    elif player == 2:
            print('Jogador escolheu PAPEL\n'
                  'PAPEL embrulha PEDRA \n'
                  'JOGADOR VENCE!!!')
    elif player == 3:
            print('Jogador escolheu TESOURA\n'
                  'PEDRA destrói TESOURA\n'
                  'JOGADOR PERDE!')
    else:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
if pc == 2:
    print('Computador escolheu PAPEL')
    if player == 1:
        print('Jogador escolheu PEDRA\n'
              'PAPEL embrulha PEDRA \n'
              'JOGADOR PERDE!')
    elif player == 2:
        print('Jogador escolheu PAPEL\n'
              'PAPEL com PAPEL não risca\n'
              'O JOGO EMPATOU!')
    elif player == 3:
        print('Jogador escolheu TESOURA\n'
              'TESOURA corta PAPEL\n'
              'JOGADOR VENCE!!!')
    else:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
if pc == 3:
    print('Computador escolheu TESOURA')
    if player == 1:
        print('Jogador escolheu PEDRA\n'
              'PEDRA destrói TESOURA\n'
              'JOGADOR VENCE!!!')
    elif player == 2:
        print('Jogador escolheu PAPEL\n'
              'TESOURA corta PAPEL\n'
              'JOGADOR PERDE!')
    elif player == 3:
        print('Jogador escolheu TESOURA\n'
              'TESOURA com TESOURA faísca\n'
              'O JOGO EMPATOU!')
    else:
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')







