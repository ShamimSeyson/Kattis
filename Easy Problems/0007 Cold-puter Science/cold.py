totalNum = int(input())
temperatures = input().split()
lessThanZero = 0
for temperature in temperatures:
  if int(temperature) < 0:
    lessThanZero = lessThanZero + 1
print(lessThanZero)