#!/usr/bin/python3

def largest(string):
    largestNum = 0
    for char in string:
        if int(char)>largestNum:
            largestNum = int(char)
    return str(largestNum)

def largestJoltage(n):
    digit = [0]*12
    pos = [0]*12
    digit[0] = largest(n[:-11])
    pos[0] = n.index(digit[0])
    #???
    digit[1] = largest(n[pos[0]+1:-10])
    pos[1] = pos[0]+n[pos[0]+1:-10].index(digit[1])

    digit[2] = largest(n[pos[1]+1:-9])
    pos[2] = pos[1]+n[pos[1]+1:-9].index(digit[2])
    #Is this actually correct??



    result = ""
    for d in digit:
        result += str(d)
    return int(result)


file = open("day3-input")
batteries = []
for line in file:
    batteries.append(line)
file.close()

total = 0
for batStrip in batteries:
    batStrip = batStrip.rstrip('\n')
    total += largestJoltage(batStrip)
print(total)

