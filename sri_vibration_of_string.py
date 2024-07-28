Noofdivisions = 100  #no of elements in string = for smooth curve
Time = 100  # how long to run
delx = 0.1
delt = 0.1  # no of intervals to find = for smooth animation
c = 0   # damping
m = 1   # mass
k = 1   # stiffness

mmcdt = m - (c * delt)
mpcdt = m + (c * delt)
kdtsmtm = (k * (delt ** 2)) - (2 * m)

y = [0 for i in range(0, Time)]
for j in range(0, Time):
    y[j] = [0 for i in range(0, Noofdivisions+1)]

#input disp
inidisploc = 25  # < Noofdivisions
inidispval = 1
for i in range(0, -2, -1):
    for j in range(0, inidisploc + 1):
        y[i][j] = (j / inidisploc) * inidispval
    for j in range(inidisploc + 1, Noofdivisions+1):
        y[i][j] = ((Noofdivisions - j) / (Noofdivisions - inidisploc)) * inidispval

print(y[0])

import time

for t in range(0, Time-1):
    for x in range(1, Noofdivisions):
        y[t+1][x] = (((delt **2) / (delx ** 2)) * (y[t][x+1] - (2 * y[t][x]) + y[t][x-1])) + (2 * y[t][x]) - y[t-1][x]
        #y[t][x] = -(((y[t-2][x] * mmcdt) + (y[t-1][x] * kdtsmtm)) / mpcdt)
    #time.sleep(0.1)
    #print(y[t])

import csv

with open('E:\\Python\\Outputs\\vos_new_100.csv', 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(y)

print('Done')
