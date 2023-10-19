def sorting_from_smallest_to_largest(list):
    for i in range(len(list)):
        for x in range(1,len(list)):
            if list[x]>list[x-1]:
                pass
            elif list[x]<list[x-1]:
                remeber = list[x-1]
                list[x-1] = list[x]
                list[x] = remeber
            else:
                pass

    return list






# 2 4 50 4
