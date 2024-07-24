import math

stlfile = open("E:\Python\Inputs\\Unbend_Model.stl", "r")

unit = ''
onearea = 0.0; area = 0.0; volume = 0.0
count = 0; s = 0; b = 0
vertices = [[0,0,0],[0,0,0],[0,0,0]]
sidelengths = [0,0,0]; normal = [0,0,0]; centroid = [0,0,0]; ds = [0,0,0]

data = stlfile.readlines()

for line in data:
    word = line.split()

    #unit
    if s == 0:
        for i in word:
            if i == 'Unit':
                unit = word[s+2]
            s += 1

    #normal
    if word[0] == 'facet':
        if word[1] == 'normal':
            for i in range(0,3):
                normal[i] = float(word[i+2])
    
    #getting the vertices of the one element
    if word[0] == 'vertex':
        for i in range(0,3):
            vertices[b][i] = float(word[i+1])
        b += 1

    if word[0] != 'endfacet':
        continue

    b = 0
    
    #area calculation using each face using its side lengths
    for side in range(0,3):
        sidelengths[side] = math.sqrt((vertices[(side+1)%3][0] - vertices[side][0])**2 + (vertices[(side+1)%3][1] - vertices[side][1])**2 + (vertices[(side+1)%3][2] - vertices[side][2])**2)
    s = (sidelengths[0] + sidelengths[1] + sidelengths[2])/2
    onearea = math.sqrt(s*(s-sidelengths[0])*(s-sidelengths[1])*(s-sidelengths[2]))
    area += onearea

    #volume calculation using gauss divergence
    for i in range(0,3):
        centroid[i] = (vertices[0][i] + vertices[1][i] + vertices[2][i])/3

    for i in range(0,3):
        ds[i] = onearea * normal[i]

    for i in range(0,3):
        volume += centroid[i] * ds[i]

volume /= 3

print('\nArea =', round(area, 10), 'sq.',unit)
print('Volume =', round(volume, 10), 'cu.',unit)
