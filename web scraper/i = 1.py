import time

i = 1
ii = 1
iii = ii/100
ii = 0

while True:
    print (ii)
    ii += iii


while True:
    print (i)
    i = i*0.9
    time.sleep(0.1)

