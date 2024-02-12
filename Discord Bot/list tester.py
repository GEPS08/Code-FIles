list1 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]
list10 = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9']

print (list1)
print(list10)


def ShortenList(list, type):

    if type == 'str':
        list2 = ''
    elif type == 'int':
        list2 = 0

    list3 = []

    ii = len(list) - 1
    for i in reversed(list):
        if list[ii] == list2:
            list3.append(ii)
        ii -= 1
        list2 = i

    for i in list3:
        del(list[(i - 1)])

    return list

list1 = ShortenList(list1, 'int')
list10 = ShortenList(list10, 'str')

print(list10)
print(list1)