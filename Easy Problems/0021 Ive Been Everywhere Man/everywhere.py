testCasesTotal = int(input())
for testCaseNum in range(testCasesTotal):
    tripsTotal = int(input())
    citiesSet = set()
    for tripNum in range(tripsTotal):
        citiesSet.add(input())
    print(len(citiesSet))
