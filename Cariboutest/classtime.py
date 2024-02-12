start = input().split(':')
end = input().split(':')
takenh = 0
takenm = 0

takenh = int(end[0]) - int(start[0])

if takenh < 0:
    takenh *= -1

if end < start:
    takenh = 24 - takenh

takenh *= 60


takenm = int(end[1]) - int(start[1])

taken = takenh + takenm

if taken == 0:
    taken = 24

print(taken)