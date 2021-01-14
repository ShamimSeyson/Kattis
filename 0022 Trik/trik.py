firstCup = True
secondCup = False
thirdCup = False

movesList = list(input())
for move in movesList:
    if move == "A":
        firstCup, secondCup = secondCup, firstCup

    if move == "B":
        secondCup, thirdCup = thirdCup, secondCup

    if move == "C":
        firstCup, thirdCup = thirdCup, firstCup

if firstCup == True:
    print(1)
elif secondCup == True:
    print(2)
elif thirdCup == True:
    print(3)
