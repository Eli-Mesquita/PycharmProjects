import random
soma = 0
cpu = random.randint(0, 15)
n = int(input('Digite um número entre 0 e 15:'))
while n != cpu:
    soma += 1
    if n < cpu:
        n = int(input('Um pouco mais... Tente outra vez:'))
    elif n > cpu:
        n = int(input('Um pouco menos... Tente outra vez:'))
print(f'Você é um gênio! Acertou em apenas {soma+1} tentativas')
