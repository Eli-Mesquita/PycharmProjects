maisdmil = total = menor = c = 0
barato = ' '
while True:
    product = str(input('Insira o nome do produto: '))
    price = float(input(' Insira o valor do produto: R$'))
    c += 1
    total += price
    if price > 1000:
        maisdmil += 1
    if c == 1 or price < menor:
        menor = price
        barato = product
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S / N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'O valor total da compra foi de R${total:.2f}\n'
      f'O número de produtos acima de R$1000 é: {maisdmil}\n'
      f'O/A {barato} foi produto de menor valor e custou R$ {menor}')



