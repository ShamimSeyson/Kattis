from math import sin
from math import radians
from math import ceil
inputLine = input().split()
result = int(inputLine[0]) / sin(radians(int(inputLine[1])))
print(ceil(result))
