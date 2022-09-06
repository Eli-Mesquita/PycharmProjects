n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;33m', end=" ")
        cont += 1
    else:
        print('\033[1;31m', end=" ")
    print(f'{c}', end=" ")
print(f'\n\033[1;34mO numero {n} tem {cont} divisores')
if cont == 2:
    print(f'\033[1;32mPortanto, {n} é um número PRIMO.')
else:
    print(f'Portanto, {n} \033[1;31mNÃO é um número PRIMO.')



