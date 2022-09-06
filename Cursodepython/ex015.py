d = int(input('Quantos dias de aluguel?'))
km = float(input('Quantos KM foram percorridos durante o período?'))
va = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(va))
