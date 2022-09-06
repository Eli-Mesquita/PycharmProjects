n1 = float(input('insira o primeiro número: '))
n2 = float(input('Insira o segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
elif n1 == n2:
    print('O primeiro valor é igual ao segundo.')
else:
    print('Valores inválidos! Por favor tente novamente!')
