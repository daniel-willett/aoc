#!/usr/bin/python3

def northEast(i,j):
    if i==xLength-1:
        return ""
    if j==0:
        return rows[i+1][j]
    return rows[i+1][j] + rows[i+1][j-1]

def southEast(i,j):
    if j==yLength-1:
        return ""
    if i==xLength-1:
        return rows[i][j+1]
    return rows[i][j+1] + rows[i+1][j+1]

def southWest(i,j):
    if i==0:
        return ""
    if j==yLength-1:
        return rows[i-1][j]
    return rows[i-1][j] + rows[i-1][j+1]

def northWest(i,j):
    if j==0:
        return ""
    if i==0:
        return rows[i][j-1]
    return rows[i][j-1] + rows[i-1][j-1]

def around(i,j):
    #so normally it would be arr[i+k][j+l] for k,l in {-1,0,1}^2\{(0,0)}
    #but we also need to consider edge cases
    """
    123
    4X5
    678

    northeast is (3,5)
    southeast is (7,8)
    southwest is (6,4)
    northwest is (1,2)
    """
    result = ""
    result += northEast(i,j)
    result += southEast(i,j)
    result += southWest(i,j)
    result += northWest(i,j)
    return result

file = open("day4-input")
rows = []
for line in file:
    rows.append(line.rstrip('\n'))
file.close()

xLength = len(rows[0])
yLength = len(rows)
surroundingRolls = ""
counter = 0
madeChanges = True
while madeChanges==True:
    madeChanges=False
    for i in range(xLength):
        for j in range(yLength):
            surroundingRolls = around(i,j)
            if surroundingRolls.count("@")<4 and rows[i][j]=='@':
                counter += 1
                madeChanges = True
                rows[i] = rows[i][:j] + '.' + rows[i][j+1:]


print(counter)
