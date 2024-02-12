a = int(input())
aa = input().split(' ')
cool = 0

for i in range(len(aa)):
    cool += int(aa[i])
cool /= a

for i in range(len(aa)):
    if int(aa[i]) > cool:
        print('higher')
    elif int(aa[i]) < cool:
        print('lower')
    elif int(aa[i]) == cool:
        print('equal')