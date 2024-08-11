def centroid(*args):
    largs = list(args)
    maxc = 0
    count = 0
    for one in largs:
        count += 1
        if len(one) > maxc:
            maxc = len(one)

    rcen = [0 for i in range(maxc)]
    dum = [0 for i in range(maxc)]
    i = 0
    for j in range(maxc):
        for one in largs:
            if len(one) < maxc:
                for k in range(maxc):
                    if k > (len(one) - 1):
                        one.append(0)
            rcen[i] += one[j] / count
        i += 1

    print(rcen)
    
centroid([2],[2,3,4])
