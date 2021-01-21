entry = input()
while entry != "-1":
    firstPair = True
    distance = 0
    for i in range(int(entry)):
        pair = input().split()
        miles = int(pair[0])
        hours = int(pair[1])
        if firstPair == True:
            distance += (miles * hours)
        else:
            distance += (miles * (hours - previousHours))
        previousHours = hours
        firstPair = False
    print(distance, "miles")
    entry = input()
