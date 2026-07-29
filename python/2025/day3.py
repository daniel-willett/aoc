#!/usr/bin/python3

def largest(string):
    largestNum = 0
    for char in string:
        if int(char)>largestNum:
            largestNum = int(char)
    return str(largestNum)

def largestJoltage(n):
    firstDigit = largest(n[:-1])
    pos = n.index(firstDigit)
    secondDigit = largest(n[pos+1:])
    result = ""
    result = firstDigit + secondDigit
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
