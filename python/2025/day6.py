#!/usr/bin/python3

import re

file = open("day6-input")
rows = []
for line in file:
    line = re.sub('\s+', ' ', line)
    temp = line.split(" ")
    temp = temp[:-1]
    rows.append(temp)
file.close()

print(rows[0])

result = 0
for column in range(len(rows[0])):
    if rows[len(rows)-1][column]=="*":
        runningTotal = 1
    else:
        runningTotal = 0 
    for line in range(len(rows)-1):
        if rows[len(rows)-1][column]=="*":
            runningTotal *= int(rows[line][column])
        else:
            runningTotal += int(rows[line][column])
    result += runningTotal

print(result)



