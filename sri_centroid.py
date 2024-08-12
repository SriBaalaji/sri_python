def centroid(*args):
    if len(args) == 0:
        return ValueError

    from itertools import zip_longest

    rcen = []
    for i in zip_longest(*args, fillvalue = 0):
        rcen.append(sum(i)/len(args))
    
    return (rcen)
    
    
print(centroid([2],[2,3,4]))
