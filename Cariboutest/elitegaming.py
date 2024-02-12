i = input()
integ = 1
bad = 0

for ii in range(len(i)):
    if not ii-1 < 0:
        if i[ii] == i[ii-1]:
            print('BAD')
            bad = 1
            break
if not bad == 1:
    print('GOOD')