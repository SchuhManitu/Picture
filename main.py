import requests
import time
import random
import sys

f = open(file='1.txt', mode='w')
sys.stdout = f

#############################


url1 = 'https://fotoshare.co/i/' + '3rhwxb1'
print(url1)
x1 = requests.get(url1)
print(x1)

#############################

i = 1
while i < 10:

    randstr = ""
    source = 'abcdefghijklmnopqrstuvwxyz1234567890' + '1234567890'
    for i in range(7):
        randstr += random.choice(source)

    url = 'https://fotoshare.co/i/' + randstr
    print(url)
    time.sleep(0.75)
    response = requests.get(url)
    print(response)
    print(response.ok)


f.close()

# Zufall
# import random
#
# randstr = ""
# source = 'abcdefghijklmnopqrstuvwxyz1234567890' + '1234567890'
# for i in range(7):
#     randstr += random.choice(source)
#
# url = 'https://fotoshare.co/i/' + randstr
#
# x = requests.get(url)
# print(x)
