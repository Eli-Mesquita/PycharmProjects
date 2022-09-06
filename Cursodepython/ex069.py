f = m = ida = 0
while True:
    print('-' * 20)
    print('CADASTRO DE CLIENTE')
    print('-' * 20)
    age = int(input('Insira a idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Informe o gênero [F / M: ')).upper().strip()[0]
    if age >= 18:
        ida += 1
    if sex == 'M':
        m += 1
    if age < 20 and sex == 'F':
        f += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [ S / N]')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com a mais de 18 anos é: {ida} \n'
      f'O número de homens cadastrados é: {m} \n'
      f'O número de mulheres com menos de 20 anos é: {f}')
