file = open('doublon.txt', 'r')

Line = file.readlines()

# delete dublon in Line list
Line = list(dict.fromkeys(Line))


print(Line)
