monthlyMegabytes = int(input())
pastMonthsNum = int(input())
usedMegabytes = 0
for i in range(1, pastMonthsNum + 1):
    usedMegabytes = usedMegabytes + int(input())

availableMegabytes = monthlyMegabytes + ((pastMonthsNum * monthlyMegabytes) - usedMegabytes)
print(availableMegabytes)
