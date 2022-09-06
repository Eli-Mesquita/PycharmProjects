'''import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hip = (math.sqrt(co ** 2 + ca ** 2))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa do triângulo retângulo é {}'.format(hip))'''
import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hip = math.hypot(co, ca)
print('A hipotenusa do triângulo retângulo é {}'.format(hip))




