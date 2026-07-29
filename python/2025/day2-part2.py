#!/usr/bin/python3

def isInvalid(n):
    stringN = str(n)
    length = len(stringN)
    for i in range(int(length/2),0,-1):
        matches = [index for index, char in enumerate(stringN) if char == stringN[0:i]]



file = open("day2-input")
data = ""
data = file.read()
data = data.rstrip('\n')
file.close()

idRanges = data.split(',')
tally = []
for ranges in idRanges:
    values = ranges.split('-')
    print(values)
    for numb in range(int(values[0]),int(values[1])+1):
        if isInvalid(numb):
            tally.append(numb)

print(sum(tally))
