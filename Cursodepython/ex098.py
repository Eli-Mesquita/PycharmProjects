from time import sleep
def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1:')
    for cont in range(1, 11):
        sleep(0.5)
        print(cont, end=' ')
    print('FIM!')
    print('-=' * 20)
    sleep(1)
    print('Contagem de 10 até 0 de 2 em 2:')
    for cont in range(10, -1, -2):
        sleep(0.5)
        print(cont, end=' ')
    print('FIM!')
    print('-=' * 20)
    sleep(1)
    print('Agora é a sa vez de personalizar a contagem!')
    a = int(input('Início: '))
    b = int(input('Fim:    '))
    c = int(input('Passo:  '))
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a > b:
        c = -c
        b = b - 1
    if c == 0:
        c = -1
    for cont in range(a, b, c):
        sleep(0.5)
        print(cont, end=' ')
    print('FIM!')


contador()
