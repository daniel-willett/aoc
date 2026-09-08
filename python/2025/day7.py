#!/usr/bin/python3

file = open("day7-input")
rows = []
for line in file:
    rows.append(line.rstrip('\n'))
file.close()

columnOfS = rows[0].index("S")
#rows[1][columnOfS] = "|"
rows[1] = rows[1][:columnOfS] + "|" + rows[1][columnOfS+1:]

numberOfSplits = 0
for line in range(len(rows)):
    for column in range(len(rows[0])):
        if rows[line-1][column]=="|":
            if rows[line][column]=="^":
                numberOfSplits += 1
                #rows[line][column-1] = "|"
                #rows[line][column+1] = "|"
                rows[line] = rows[line][:column-1] + "|^|" + rows[line][column+2:]
            else:
                #rows[line][column]="|"
                rows[line] = rows[line][:column] + "|" + rows[line][column+1:]

print(numberOfSplits)



