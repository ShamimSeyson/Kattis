import sys

for inputLine in sys.stdin:
    pairList = inputLine.split()
    num1 = int(pairList[0])
    num2 = int(pairList[1])
    diff = abs(num1 - num2)
    print(diff)
