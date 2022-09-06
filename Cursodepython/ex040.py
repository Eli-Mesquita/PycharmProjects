n1 = float(input('Digite a nota da N1: '))
n2 = float(input('Digite a nota da N2: '))
mp = ((n1*2) + (n2*3))/5
af = 10 - mp
print('A sua média Parcial é: {:.1f}'.format(mp))
if 10 >= mp >= 7:
    print('Situação: \033[1;32mAprovado\033[m')
elif 7 > mp >= 3:
    print('Situação: \033[1;33mAvaliação Final')
    print(f'Você precisa de nota {af:.1f} na AF.\033[m')
elif mp < 3:
    print('Situação: \033[1;31mReprovado')
elif mp > 10:
    print('\033[1;31mVerifique a sua nota e tente novamente.')
else:
    print('\033[1;31mVerifique a sua nota e tente novamente.')