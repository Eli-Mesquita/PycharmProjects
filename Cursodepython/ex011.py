larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
ar = larg*alt
tinta = ar/2
print('Sua parede tem uma dimensão de {} x {} e sua área é de {:.2f'
      '}m²'.format(larg, alt, ar))
print('Você vai precisar de {:.2f}l de tinta para pinta-la'.format(tinta))