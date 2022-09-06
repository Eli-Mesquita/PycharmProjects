from datetime import datetime
ficha = dict()
ficha["Nome"] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ficha["Idade"] = datetime.now().year - nascimento
ficha["CTPS"] = int(input('Carteira de trabalho: (0 - não tem) '))
if ficha["CTPS"] > 0:
    ficha["Ano de contratação"] = int(input('Ano de contratação: '))
    ficha["Salário"] = float(input('Salário: '))
    ficha["Idade de aposentadoria"] = ficha["Ano de contratação"] + 35 - nascimento
print('=== Dados do colaborador ===')
for k, v in ficha.items():
    print(f'   - {k}: {v}')

