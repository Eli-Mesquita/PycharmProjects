from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
option = 0
print('[ 1 ] somar \n'
      '[ 2 ] multiplicar\n'
      '[ 3 ] maior\n'
      '[ 4 ] novos números\n'
      '[ 5 ] sair do programa')
option = int(input('\033[1;34m>>>>>>O que deseja fazer?\033[m '))
while option != 5:
    if option == 1:
        print(f'\033[1;32mA soma entre {v1} e {v2} é {v1+v2}\033[m')
    elif option == 2:
        print(f'\033[1;32mO resultado de {v1} x {v2} é {v1*v2}\033[m')
    elif option == 3:
        if v1 > v2:
            print(f'\033[1;32mEntre {v1} e {v2}  o  maior é {v1}\033[m')
        else:
            print(f'\033[1;32mEntre {v1} e {v2} o maior valor é {v2}\033[m')
    elif option == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    else:
        print('\033[1;31mOpção inválida!\033[m')
    sleep(2)
    print('=-='*10)
    print('[ 1 ] somar \n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')
    option = int(input('\033[1;34m>>>>>> O que deseja fazer?\033[m '))
print('\033[1;31mFinalizando...\033[m')
sleep(2)
print('\033[1;31mFim\033[m')