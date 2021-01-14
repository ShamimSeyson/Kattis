inputNum = int(input())
for i in range(inputNum):
    inputsList = input().split()
    withoutAds = int(inputsList[0])
    withAds = int(inputsList[1])
    adCost = int(inputsList[2])
    adsMinusCost = withAds - adCost
    if adsMinusCost > withoutAds:
        print("advertise")
    elif adsMinusCost == withoutAds:
        print("does not matter")
    else:
        print("do not advertise")
