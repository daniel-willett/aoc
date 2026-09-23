#!/usr/bin/python3

file = open("day1-input")
data = []
for line in file:
    data.append(line.rstrip("\n"))
file.close()

numbers = ["0","1","2","3","4","5","6","7","8","9"]
counter = []
for line in data:
    Lpointer = 0
    Rpointer = len(line)-1
    found = False
    while found==False:
        if line[Lpointer] in numbers:
            found = True
        else:
            Lpointer += 1

    found = False

    while found==False:
        if line[Rpointer] in numbers:
            found = True
        else:
            Rpointer -= 1
    
    val = int(line[Lpointer] + line[Rpointer])
    counter.append(val)

total = 0
for num in counter:
    total += num

print(total)
