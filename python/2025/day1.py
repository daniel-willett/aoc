#!/usr/bin/python3

file = open("day1-input")
actions = []
for line in file:
    actions.append(line)
file.close()

#We can use actions[i][0] for L/R
#And use actions[i][1:] for the value that comes after
counter = 0
position = 50
for action in actions:
    action = action.rstrip('\n')
    if action[0] == "L":
        position -= int(action[1:])
    if action[0] == "R":
        position += int(action[1:])
    position = position % 100
    if position == 0:
        counter += 1

print(counter)
