def choice_sorting(list):
    for x in range(len(list)):
        min_number = list[x]
        number = list[x]
        index = 0
        for i in range(x+1,len(list)):
            if min_number>list[i]:
                index = i
                min_number = list[i]
        if index != 0:
            list[x] = min_number
            list[index] = number
    return list



# Sortownie przez wybór
# wybierz 1 liczba z listy
# porównaj z kadą inną i znajdź najmniejszą
# zastąp najmniejszą z liczba wybraną
# przejdź do koljenej liczby i zrób to samo
# [5,2,1,6,3]
