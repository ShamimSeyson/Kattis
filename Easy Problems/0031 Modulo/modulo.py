moduloSet = set()
for i in range(10):
    number = int(input())
    remainder = number % 42
    moduloSet.add(remainder)
print(len(moduloSet))
