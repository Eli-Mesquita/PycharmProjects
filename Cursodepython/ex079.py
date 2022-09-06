valor = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valor:
        valor.append(num)
        print('Valor adicionado com sucesso!')
        cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
        while cont not in 'SsNn':
            cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
        if cont == 'N':
            print(f'Você digitou os valores: {sorted(valor)}')
            break
    else:
        print('Números duplicados não serão adicionados.')
        cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
        while cont not in 'SsNn':
            cont = str(input('Continuar? [S/N] ')).upper().strip()[0]
        if cont == 'N':
            print(f'Você digitou os valores {sorted(valor)}')
            break



