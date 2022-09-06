def lin():
    print('-' * 30)


name = 'Eli Mesquita'
lin()
print(f'{name:^30}')
lin()


def message(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


message('         Eli Mesquita')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A + B = {s}')
    print('-' * 15)


soma(a=8, b=9)
soma(2, 2)


def contador(*num):
    print(num)
    size = len(num)
    print(f'Recebi os valores {sorted(num, reverse=True)} que são ao todo {size} números.')
    print(f'A soma dos valores informados é igual a {sum(num)}')
    for v in num:
        print(v, end=' - ')
    print('')


contador(3, 4, 6, 8, 9)


def doble(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 4, 6, 8, 20, 27]
doble(valores)
print(valores)