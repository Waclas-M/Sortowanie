def merge(list):
    if len(list) > 1:

        mid = len(list) // 2
        list_L = list[:mid]
        list_R = list[mid:]
        merge(list_L)
        merge(list_R)

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
    return list

