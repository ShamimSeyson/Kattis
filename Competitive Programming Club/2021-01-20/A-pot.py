num = int(input())
result = 0
for i in range(num):
    raw = input()
    power = int(raw[int(len(raw)-1)])
    number = int(raw[:-1])
    result += number ** power
print(result)
