print('{:=^50}'.format(' CASA POTIGUAR '))
valor = float(input('Informe o valor da compra: R$'))
print('FORMA DE PAGAMENTO\n'
      '[ 1 ] à vista - Dinheiro / PIX\n'
      '[ 2 ] à vista - Cartão\n'
      '[ 3 ] 2x - Cartão\n'
      '[ 4 ] 3x ou mais - Cartão')
fp = int(input('Escolha a forma de pagamento: '))

if fp == 1:
    print('Desconto de 10% para compras à vista nessa modalidade de pagamento\n'
          f'O valor final da sua compra foi de {valor - (valor*10/100):.2f}')
elif fp == 2:
    print('Desconto de 5% para compras à vista nessa modalidade de pagamento\n'
          f'O valor final da sua compra foi de {valor - (valor * 5 / 100):.2f}')
elif fp == 3:
    parc = int(input('Informe o número de parcelas:'))
    print('É possível parcelar sua compra sem juros.\n'
          f'O valor final da sua compra foi de {valor}')
elif fp == 4:
    parc = int(input('Informe o número de parcelas:'))
    print('É possível parcelar sua compra com um acréscimo de 20% de juros.\n'
          f'O valor final da sua compra foi de {valor + (valor * 20/100)}')
else:
    print('\033[1;31mEscolha uma forma de pagamento válida.')
