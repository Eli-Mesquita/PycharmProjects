import random
from time import sleep
speed = random.randrange(20, 180)
print('Analisando a velocidade...')
sleep(2)
print(f'A velocidade do veículo é {speed}Km/h')
if speed > 80:
    print('O veículo ultrapassou o limite de velocidade e foi multado.')
    multa = (speed - 80)*7
    print(f'O valor da multa é: R${multa:.2f}')
else:
    print('O veículo está dentro do limite de velocidade.')