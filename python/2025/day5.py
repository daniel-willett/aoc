#!/usr/bin/python3

file = open("day5-input")
data = []
for line in file:
    data.append(line.rstrip("\n"))
file.close()

separator = data.index("")
intervals = data[:separator]
ingredients = data[separator+1:]
isFresh = False
counter = 0

for ing in ingredients:
    isFresh = False
    for intvl in intervals:
        [first,last] = intvl.split("-")
        if int(ing)>=int(first) and int(ing)<=int(last):
            isFresh = True
    if isFresh==True:
        counter += 1

print(counter)
