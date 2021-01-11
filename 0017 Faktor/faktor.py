inputList = input().split()
articleNum = int(inputList[0])
impactFac = int(inputList[1])

bribeNum = articleNum * (impactFac - 1)
bribeNum += 1
print(bribeNum)
