nameList = list(input())
i = 0
while i <= (len(nameList) - 1):
    if i != len(nameList) - 1:
        if nameList[i] == nameList[i + 1]:
            nameList.pop(i + 1)
            i -= 1
    i += 1
nameString = "".join(nameList)
print(nameString)
