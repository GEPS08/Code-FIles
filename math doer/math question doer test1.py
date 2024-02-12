import math,os,time

question = input('please put the context of the question here:\n')

ints = 1
questionarr = []

for int in question:
    print ('there are', ints, 'numbers in the inputed text')
    questionarr.append(int)
    ints += 1
print (questionarr)