def sorting(list):
    if len(list) > 1:

        mid = len(list) // 2
        list_L = list[:mid]
        list_R = list[mid:]
        sorting(list_L)
        sorting(list_R)

        i = j = k = 0

        while i < len(list_L) and j < len(list_R):
            if list_L[i] < list_R[j]:
                list[k] = list_L[i]
                i += 1
            else:
                list[k] = list_R[j]
                j += 1
            k+=1
        while j < len(list_R):
            list[k] = list_R[j]
            j+=1
            k+=1

        while i < len(list_L):
            list[k] = list_L[i]
            i+=1
            k+=1


def next_sorting(list):
    mniejsze = []
    rowne = []
    wieksze = []
    if len(list) > 1:
        piwot = list[len(list)//2]
        for x in list:
            if x > piwot:
                wieksze.append(x)
            elif x == piwot:
                rowne.append(x)
            else:
                mniejsze.append(x)
        return next_sorting(mniejsze) + rowne + next_sorting(wieksze)
    else:
        return list
print(next_sorting([5,6,4,2,1]))



# 5,6,4,2,1
# 5,6,4 | 2,1
# 2,1,4 | 5,6
# 1,2,4 | 5,6
