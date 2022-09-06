casa = float(input('Qual o valor do imóvel que deseja financiar? R$'))
s = float(input('informe o valor do seu salário atual: R$'))
anos = int(input('Em quantos anos quer pagar o financiamento? '))
num_de_parc = anos*12
valor_da_parcela = casa/num_de_parc
if valor_da_parcela > (s*30/100):
    print(f'Financiado em {num_de_parc} meses, o valor da parcela seria de {valor_da_parcela:.2f}.\n'
          '\033[1;33mEsse valor excede a cota máxima de 30% do seu salário.\033[m')
    print('\033[01;31mInfelizmente você não pode financiar o imóvel nessas condições.\033[m')
else:
    print(f'O imovel será financiado em {num_de_parc} meses, com parcela mensal de R${valor_da_parcela:.2f} \n'
          '\033[01;32mO financiamento pode ser concedido.')


