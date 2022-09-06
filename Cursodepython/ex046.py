from time import sleep
from playsound import playsound
for c in range(10, 0, -1):
    print(c), sleep(1),
print('Ignition\n', sleep(1),
      'LIFT OFF!')
playsound('ex046.mp3')

