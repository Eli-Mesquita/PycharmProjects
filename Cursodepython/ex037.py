print('-=-'*15)
print('Calculadora de Conversão de Bases Numéricas')
print('-=-'*15)
n = int(input('Inisra o número inteiro que deseja converter: '))
print('[ 1 ] para BINÁRIO')
print('[ 2 ] para OCTAL')
print('[ 3 ] para HEXADECIMAL')
b = int(input(('Para que base deseja converter esse número? ')))
if b == 1:
    bin = bin(n)
    print(f'{n} convertido para BINÁRIO é igual a {bin[2:]}')
elif b == 2:
    oct = oct(n)
    print(f'{n} convertido para OCTAL é igual a {oct[2:]}')
elif b == 3:
    hex = hex(n)
    print(f'{n} convertido para HEXADECIMAL é igual a {hex[2:]}')
else:
    print('\033[1;31mOpção inválida! Por favor tente novamente.')
