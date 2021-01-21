inputList = input().split()
fizzNum = int(inputList[0])
buzzNum = int(inputList[1])
lengthNum = int(inputList[2])
for i in range(1, lengthNum + 1):
    if i % fizzNum == 0 and i % buzzNum == 0:
        print("FizzBuzz")
    elif i % fizzNum == 0:
        print("Fizz")
    elif i % buzzNum == 0:
        print("Buzz")
    else:
        print(i)
    
