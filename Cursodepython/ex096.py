def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}m de largura x {c}m de comprimento é de {a:.1f}m²')


print('-' * 20)
print('Controle de terrenos')
print('-' * 20)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
