def sorting_linear(list):
    for x in range(0,len(list)):
        i = 1
        while list[i-1]<list[i] and i < len(list)-1:
            i+=1

        while list[i-1]>list[i]:
            number_poprzedzajacy = list[i-1]
            number=list[i]
            list[i] = number_poprzedzajacy
            list[i-1] = number
            i +=1
            if i > len(list)-1:
                break
    return list

#Rozpocznij od drugiego elementu zbioru
#porównaj go z poprzednim elementem
#jeśli ten element jest większy przesun go o jedno w prawo
#przesuwa się dopóki nie napotka liczby mniejszej lub gdy skończy się lista
#następnie wstaw wyznaczoną liczbę w wyznaczoną pozycje
# [6,5,4,3,2,1]
#jeżeli 5 jest mniejsze od 6 | 6 przesuń w prawo
