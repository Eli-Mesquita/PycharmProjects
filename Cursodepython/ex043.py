peso = float(input('Informe o seu peso (kg):'))
altura = float(input('Informe a sua altura (cm)'))
imc = peso/((altura**2)/100**2)
print(f'O seu IMC é de {imc:.1f} kg/m2')
if imc < 18.5:
    print('Categoria: Abaixo do peso \n'
          'De acordo com a Organização Mundial da Saúde, seu IMC está abaixo do recomendado para a sua altura.')
elif imc <= 24.9:
    print('Categoria: Peso normal \n'
          'De acordo com a Organização Mundial da Saúde, seu IMC é considerado normal para a sua altura.')
elif imc <= 29.9:
    print('Categoria: Sobrepeso \n'
          'De acordo com a Organização Mundial da Saúde, seu IMC está acima do recomendado para a sua altura.')
elif imc <= 34.9:
    print('Categoria: Obesidade grau 1 \n'
          'De acordo com a Organização Mundial da Saúde, seu IMC está acima do recomendado para a sua altura.')
elif imc <= 39.9:
    print('Categoria: Obesidade grau 2 \n'
          'De acordo com a Organização Mundial da Saúde, seu IMC está acima do recomendado para a sua altura.')
elif imc <= 40:
    print('Categoria: Obesidade grau 3 \n'
          'De acordo com a Organização Mundial da Saúde, seu IMC está acima do recomendado para a sua altura.')
