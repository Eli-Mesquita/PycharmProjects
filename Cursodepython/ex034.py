s = float(input('Qual o valor do seu salário atual? R$'))
if s >= 1250:
    print(f'Você receberá um aumento de 10% e seu salário passará a se de: R${s+(s*10/100):.2f}')
else:
    print(f'Você receberá um aumento de 15% e seu salário passará a ser de: R${s+(s*15/100):.2f}')
