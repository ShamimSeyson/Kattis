binary = bin(int(input()))
binaryNoPrefix = binary[2:]
reverseBinary = binaryNoPrefix[::-1]
base10 = int(reverseBinary, 2)
print(base10)
