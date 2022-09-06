dist = int(input('Qual é a distância da viagem em Km? '))
preço = dist*0.50 if dist <= 200 else dist*0.45
print(f'Para uma viagem de {dist:.0f}Km o valor da passagem será: R${preço:.2f}')
    