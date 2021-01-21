iteration = int(input())
sidePoints = 2
for i in range(iteration):
    sidePoints = sidePoints + (sidePoints - 1)
    totalPoints = sidePoints * sidePoints
print(totalPoints)
