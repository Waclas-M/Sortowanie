def quicksorting(list):
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
        return quicksorting(mniejsze) + rowne + quicksorting(wieksze)
    else:
        return list
