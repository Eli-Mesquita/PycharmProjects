from random import randint
c = 0
while True:
    cpu = randint(0, 11)
    player = int(input('Insert a number: '))
    choice = str(input('Odds or even? [O / E] ')).upper().strip()[0]
    total = cpu + player
    check = total % 2
    even = check == 0
    odd = check == 1
    if choice == 'O':
        if odd:
            c += 1
            print(f'You threw {player} and the computer threw {cpu}. \n'
                  f' The amount {total} is an ODD number.\n'
                  f'\033[01;32mPlayer won!\033[m')
        else:
            print(f'You threw {player} and the computer threw {cpu}. \n'
                  f' The amount {total} is an EVEN number. \n'
                  f'Player lost! Your final score was {c}\n'
                  f'\033[01;31mGame OVER\033[m')
            break
    if choice == 'E':
        if even:
            c += 1
            print(f'You threw {player} and the computer threw {cpu}. \n'
                  f' The amount {total} is an even number.\n'
                  f'\033[01;32mPlayer won\033[m')
        else:
            print(f'You threw {player} and the computer threw {cpu}. \n'
                  f' The amount {total} is an odd number. \n'
                  f'Player lost! Your final score was {c} \n'
                  f'\033[01;31mGame OVER\033[m')
            break
