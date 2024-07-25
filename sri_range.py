def srirange(*args):
    argslist = list(args)
    if len(argslist) > 3:
        print('srirange expected at most 3 arguments, got ', len(argslist))
        return -1
    elif len(argslist) == 3:
        start, stop, step = argslist
    elif len(argslist) == 2:
        start, stop = argslist
        step = 1
    elif len(argslist) == 1:
        stop = argslist[0]
        start, step = 0, 1
    
    while (start < stop and step > 0) or (start > stop and step < 0):
        yield start
        start += step


for i in srirange(12):
    print (i)
