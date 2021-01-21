sidePoints = 2
iterations = int(input())
for i in range(iterations):
    sidePoints = sidePoints + (sidePoints - 1)
totalPoints = sidePoints * sidePoints
print(totalPoints)
