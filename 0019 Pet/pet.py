contestant1 = input().split()
contestant2 = input().split()
contestant3 = input().split()
contestant4 = input().split()
contestant5 = input().split()

score1 = 0
for score in contestant1:
    score1 += int(score)

score2 = 0
for score in contestant2:
    score2 += int(score)

score3 = 0
for score in contestant3:
    score3 += int(score)

score4 = 0
for score in contestant4:
    score4 += int(score)

score5 = 0
for score in contestant5:
    score5 += int(score)
    
scoreList = [score1, score2, score3, score4, score5]

winningIndex = scoreList.index(max((score1, score2, score3, score4, score5))) + 1
winningScore = max(scoreList)

print(winningIndex, winningScore)
