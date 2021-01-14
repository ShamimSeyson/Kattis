QALY_periods = int(input())
accumQALY = 0
for period in range(QALY_periods):
    dataPair = input().split()
    product = float(dataPair[0]) * float(dataPair[1])
    accumQALY += product
print(round(accumQALY, 3))
