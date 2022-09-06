from datetime import date
nome = str(input('Nome completo: '))
sexo = str(input('Informe o sexo ( M / F): ')).upper()
ano = int(input('Ano de nascimento:'))
data = date.today().year
idade = data - ano
print(f'O/A atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JÚNIOR')
elif 19 < idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')