print('\033[1;33m-=-'*10)
print('\033[1;34m   ANALISADOR DE TRIÂNGULOS')
print('\033[1;33m-=-'*10)
a = float(input('\033[mInsira o valor do primeiro segmento: '))
b = float(input('Insira o valor do segundo segmento: '))
c = float(input('Insira o valor do terceiro segmento: '))
if (a-b) < c < (a+b) and (a-c) < b < (a+c) and (c-b) < a < (c+b):
    print('\033[1;32mOs segmentos dados PODEM FORMAR um triângulo.')
else:
    print('\033[1;31mOs segmentos dados NÃO PODEM FORMAR um triângulo.')



