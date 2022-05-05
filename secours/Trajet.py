file = open("Trajet.txt", "a+")

patterns = "Insert into Trajet(nLigne,nArretA,nArretB) values "

for i in range(32):
    file.write(patterns + "(1,,);")
    file.write("\n")
for i in range(45):
    file.write(patterns + "(2,,);")
    file.write("\n")
for i in range(24):
    file.write(patterns + "(3,,);")
    file.write("\n")
for i in range(35):
    file.write(patterns + "(4,,);")
    file.write("\n")
