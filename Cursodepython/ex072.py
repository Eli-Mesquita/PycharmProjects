num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', \
      'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20: '))

    while n not in range(0, 21):
        print('\033[1;33mNúmero inválido! Tente novamente.\033[m')
        n = int(input('Digite um número entre 0 e 20: '))
    print(f'\033[1;32mVocê digitou o número \033[1;31m{num[n]}\033[m')
    cont = str(input('Deseja continuar? [S / N] ')).upper().strip()[0]
    if cont in 'N':
        print('\033[1;34mPROGRAMA FINALIZADO!')
        break
