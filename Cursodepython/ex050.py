s = 0
cont = 0
soma = 0
conta = 0
for c in range(1, 7):
    n = int(input(f'digite o {c}º número: '))
    if n % 2 == 0:
        s += n
        cont += 1
    elif n % 2 == 1:
        soma += n
        conta += 1
print(f'A soma dos {cont} números PARES informados é igual a {s} ')
print(f'A soma dos {conta} números ÍMPARES informados é igual a {soma} ')