#ASCII Characters programm
import random
import time

# --Code below--
for key in range(5):
    randomN = random.randint(34, 111)
    key = chr(randomN)
    print('this random number is ' + str(randomN))
    print('this nunber is the code for ' + key + '\n')
    time.sleep(1)

for value in range(10):
    print('Enter a character (a number, letter or symbol)')
    Tiped = input()
    value = ord(Tiped)
    print('The code for that character is ' + str(value))

print('GoodBye')