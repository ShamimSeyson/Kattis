inputLine = input().split()
hours = int(inputLine[0])
minutes = int(inputLine[1])

earlyHours = hours - 1
earlyMinutes = minutes + 15
if earlyHours == -1:
    earlyHours = 23
    if earlyMinutes > 59:
        earlyMinutes = earlyMinutes - 60

elif earlyMinutes > 59:
    earlyMinutes = earlyMinutes - 60
    earlyHours = hours
print(earlyHours, earlyMinutes)
