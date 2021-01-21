numbersList = input().split()
numbersList[0] = int(numbersList[0][::-1])
numbersList[1] = int(numbersList[1][::-1])
print(max(numbersList))
