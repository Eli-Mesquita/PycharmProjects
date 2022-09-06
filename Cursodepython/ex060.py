from math import factorial
n = int(input('Digite um numero para calcular o seu fatorial: '))
fac = factorial(n)
c = n + 1
print(f'{n}! = ', end='')
while c > 1:
    c -= 1
    if c > 1:
        print(c, end=' x ')
    else:
        print(c, end=' = ')
print(f'{fac}')

