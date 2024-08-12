import random
import csv
import math

noofpoints = 100000

def getabg():
    alpha = random.random()
    beta = random.random()
    gamma = 1 - (alpha + beta)
    return(alpha,beta,gamma)

def findarea(a,b,c):
    sidelengths = [0,0,0]
    
    sidelengths[0] = math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)
    sidelengths[1] = math.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2 + (c[2]-b[2])**2)
    sidelengths[2] = math.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2 + (a[2]-c[2])**2)
        
    s = (sidelengths[0] + sidelengths[1] + sidelengths[2])/2
    area = math.sqrt(s*(s-sidelengths[0])*(s-sidelengths[1])*(s-sidelengths[2]))
    
    return area

def ptinsidetri(pt,t1,t2,t3):
    triarea = findarea(t1,t2,t3)
    triarea = round(triarea, 6)
    
    checkarea = findarea(pt,t2,t3)
    checkarea += findarea(t1,pt,t3)
    checkarea += findarea(t1,t2,pt)
    checkarea = round(checkarea, 6)
    
    if triarea == checkarea:
        return True
    else:
        return False
    
def trigen(*args):
    largs = list(args)
    num = len(largs)
    
    if num == 3:
        a,b,c = largs
    elif num == 4:
        a,b,c,d = largs

        checkb = ptinsidetri(b,a,c,d)
        checkd = ptinsidetri(d,a,b,c)

        if(checkb):
            temp = a
            a = d
            d = c
            c = b
            b = temp
        elif(checkd):
            temp = a
            a = b
            b = c
            c = d
            d = temp            

    ba = a.copy()
    bb = b.copy()
    bc = c.copy()

    i = 0
    while True:
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
        i += 1

a = [-1,0,0]
b = [0,1,0]
c = [1,0,0]
d = [0,0.25,0]

pt = [[0,0,0] for i in range(noofpoints)]

randpt = trigen(a,b,c,d)

for j in range(noofpoints):
    pt[j] = next(randpt)
    #print(pt[j])

with open('D:\\Training\\Python\\tri.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(pt)

print('Done')
