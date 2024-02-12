start = input().split(':')
end = input().split(':')

startm = int(start[0])*60 + int(start[1])
endm = int(end[0])*60 + int(end[1])

if startm > endm:
    taken = endm + (1440 - startm)
else:
    taken = endm - startm

print (taken)