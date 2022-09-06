s = float(input('Salário atual: R$'))
a = float(input('Quantos % de aumento?'))
ns = s + (s * a / 100)
print('Com um aumento de {:.0f}% seu novo salário será: R${:.2f}'.format(a, ns))

