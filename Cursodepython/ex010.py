real = float(input('Insira o valor em Real brasileiro:'))
dolar = real / 5.18
euro = real / 5.42
print('>>>  R$ {:.2f} Real brasileiro \n>>> US$ {:.2f} Dólar americano'.format(real, dolar))
print('>>>   € {:.2f} Euro'.format(euro))
