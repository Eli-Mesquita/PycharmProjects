from datetime import datetime
from time import sleep
from random import randint
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
for i in range(5):
    sleep(randint(1, 60))
    right_this_minute = datetime.now().minute
    if right_this_minute in odds:
        print('This minute seems a little odd')
    else:
        print('Not and odd minute at all')



# to calculate sequence
'''for c in range(1, 60):   
    if c % 2 == 1:
        print(c, end= ", " )'''


