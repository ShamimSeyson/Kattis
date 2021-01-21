import math
firstLine = input().split()
matchNum = int(firstLine[0])
w = int(firstLine[1])
h = int(firstLine[2])

for match in range(matchNum):
    matchLength = int(input())
    diagBoxLength = math.sqrt((w * w) + (h * h))
    if matchLength <= diagBoxLength:
        print("DA")
    else:
        print("NE")
