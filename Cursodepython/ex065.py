s = c = n = maior = menor = 0
cont = 'S'
while cont != 'N':
    s += n
    c += 1
    n = int(input('Insira um número: '))
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('Deseja coninuar? [ S / N ] ')).upper().strip()[0]
m = s/c
print(f'Você inseriu {c} números e a média entre eles é: {m}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')