def avg(*args):
    avgvalue = 0
    argslist = list(args)
    count = len(argslist)
    
    for i in range(0, count):
        avgvalue += (argslist[i]/count)

    return(avgvalue)

a = avg(1,5,9,8,15)

print('Average =', a)

