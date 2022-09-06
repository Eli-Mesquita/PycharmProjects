from random import randint
num = randint(1,99), randint(1,99), randint(1,99), \
      randint(1,99), randint(1,99)
print('O números sorteados foram:', end=' ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)} \n'
      f'O menor valor sorteado foi {min(num)}')
