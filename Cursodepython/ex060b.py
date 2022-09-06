n = int(input('Insira um número para calcular o seu fatorial: '))
fat = 1
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    fat *= c
    if c > 1:
        print(c, end=' x ')
    else:
        print(c, end=' = ')
print(fat, end='')


