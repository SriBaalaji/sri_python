import random
import csv

noofpoints = 100000

def getabg():
    alpha = random.random()
    beta = random.random()
    gamma = 1 - (alpha + beta)
    return(alpha,beta,gamma)

def trigen(*args):
    largs = list(args)
    num = len(largs)
    
    if num == 3:
        a,b,c = largs
    elif num == 4:
        a,b,c,d = largs

    ba = a.copy()
    bb = b.copy()
    bc = c.copy()
    
    for i in range(noofpoints):
        alpha,beta,gamma = getabg()

        while(gamma < 0):
            alpha,beta,gamma = getabg()

        sumall = alpha+beta+gamma
        while(sumall != 1):
            alpha,beta,gamma = getabg()
            sumall = alpha+beta+gamma
        
        rp = [0,0,0]
        for k in range(3):
            rp[k] = (alpha * a[k]) + (beta * b[k]) + (gamma * c[k])

        yield rp

        if num == 4:    
            if i%2 == 0:
                a = a.copy()
                b = d.copy()
                c = c.copy()
            else:
                a = ba.copy()
                b = bb.copy()
                c = bc.copy()  

a = [0,0,0]
b = [0,1,0]
c = [1,0,0]
d = [0,-1,0]

pt = [[0,0,0] for i in range(noofpoints)]

randpt = trigen(a,b,c,d)

for j in range(noofpoints):
    pt[j] = next(randpt)
    #print(pt[j])

with open('E:\\Python\\Outputs\\tri.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(pt)

print('Done')
