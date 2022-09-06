import datetime
ano = int(input('Digite o ano que quer analisar ou digite O para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
r1 = ano % 4
r2 = ano % 100
r3 = ano % 400
if r1 == 0 and r2 > 0:
    print(f'O ano de {ano} é bissexto.')
elif r1 == 0 and r2 == 0 and r3 == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')

