#!/usr/bin/python3

import re

def getNum(arr, string):
    result = []
    for val in arr:
        val = val.replace(string, "")
        result.append(int(val))
    return result


file = open("day2-input")
data = []
for line in file:
    data.append(line.rstrip("\n"))
file.close()

total = 0
for game in data:
    reds = re.findall(r"\d+ red", game)
    greens = re.findall(r"\d+ green", game)
    blues = re.findall(r"\d+ blue", game)

    reds = getNum(reds, "red")
    greens = getNum(greens, "green")
    blues = getNum(blues, "blue")

    highestRed = max(reds)
    highestGreen = max(greens)
    highestBlue = max(blues)

    if highestRed<=12 and highestGreen<=13 and highestBlue<=14:
        gameID = re.findall(r"Game \d+", game)
        gameID = getNum(gameID, "Game")
        total += gameID[0]

print(total)
