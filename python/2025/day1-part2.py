#!/usr/bin/python3

file = open("day1-input")
actions = []
for line in file:
    actions.append(line)
file.close()

counter = 0
position = 50
parity = 1
for action in actions:
    action = action.rstrip('\n')
    if action[0] == "L":
        parity = -1
    if action[0] == "R":
        parity = 1
    
    for i in range(1,int(action[1:])+1):
        position += parity
        position = position % 100
        if position == 0:
            counter += 1

print(counter)
