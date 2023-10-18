def Max(list):
    max_number=list[0]
    min_number=list[0]
    for x in range(len(list)):
        if list[x]>max_number:
            max_number = list[x]
        elif min_number>list[x]:
            min_number = list[x]
        else:
            pass
    return max_number,min_number


print(Max([12,2,12,30,60]))

