v = float(input('Qual é o valor do produto? R$'))
d = float(input('Quantos % de desconto?'))
pf = v - (v * d / 100)
print('Com um desconto de {:.0f}% o produto vai custar: R${:.2f}'.format(d, pf))