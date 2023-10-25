def sort(list):
    maksi = max(list)
    min=0
    all_bucket = []
    rang = maksi // len(list)
    if 0 in list:
        all_bucket.append(0)
    while len(list)!=len(all_bucket):
        bucket = [min,rang]
        for i in list:
            if i <= bucket[1] and i>bucket[0]:
                bucket.append(i)

        bucket.remove(min)
        bucket.remove(rang)

        if len(bucket)>=2:
            for j in range(len(bucket)):
                for x in range(1,len(bucket)):
                    if bucket[x]>bucket[x-1]:
                        pass
                    elif bucket[x]<bucket[x-1]:
                        remeber = bucket[x-1]
                        bucket[x-1] = bucket[x]
                        bucket[x] = remeber
                    else:
                        pass
            for z in bucket:
                all_bucket.append(z)


        elif len(bucket) == 0:
            pass
        else:
             all_bucket.append(bucket[0])


        min =rang
        rang+=rang
    return all_bucket


