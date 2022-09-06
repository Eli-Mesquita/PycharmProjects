'''ano = int(input('Qual o ano de fabricação do seu carro?'))
tempo = 2022 - ano
if tempo <= 3:
    print('Seu carro ainda tá novão, brother!')
else:
    print('Ish, tá precisando trocar o carango, chapa!')'''

'''ano = int(input('Qual o ano de fabricação do seu carro? '))
tempo = 2022 - ano
print('Seu carro ainda está novo' if tempo <= 3 else 'Talvez seja melhor trocar de carro!')
print('Para mais informações acesse: www.meucarrinho.com.br')'''

'''sig = str(input('Qual o seu signo?')).strip()
if sig.title() == 'Sagitário':
    print('Wow! você tem o melhor signo do zodíaco, com toda certeza!')
else:
    print('Meh, que signo chato! Como você se suporta?!')'''

n1 = float(input('Digite a nota da N1: '))
n2 = float(input('Digite a nota da N2: '))
mp = ((n1*2) + (n2*3))/5
af = 10 - mp
print('A sua média Parcial é: {:.1f}'.format(mp))
if mp >= 7:
    print('Situação: Aprovado')
elif 7 > mp >= 3:
    print('Situação: Avaliação Final')
    print(f'Você precisa de nota {af:.1f} na AF.')
elif mp < 3:
    print('Situação: Reprovado')
else:
    print('Verifique a sua nota e tente novamente.')






