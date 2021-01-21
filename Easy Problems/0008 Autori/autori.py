names = input().split("-")
initials = ""
for name in names:
  initials = initials + name[0]
print(initials)