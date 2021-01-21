number = int(input())
finalNum = 0
for i in range(number):
    unformatted = input()
    unformattedList = list(unformatted)
    exponent = unformattedList.pop()
    number = "".join(unformattedList)
    finalNum = finalNum + (int(number) ** int(exponent))
print(finalNum)
