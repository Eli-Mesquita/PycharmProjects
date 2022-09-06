saque = int(input('Informe o valor que deseja sacar: R$'))
total = saque
nota = 50
c = 0
while True:
    if total >= nota:
        total -= nota
        c += 1
    else:
        if c > 0:
            print(f'O total de {c} cédulas de {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        c = 0
        if total == 0:
            break












