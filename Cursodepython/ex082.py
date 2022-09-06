lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SsNn':
        cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-=-'*20)
print(f'A lista completa é {sorted(lista)}')
print(f'A lista de números pares digitados é {sorted(par)}')
print(f'A lista de números ímpares digitados é {sorted(impar)}')
