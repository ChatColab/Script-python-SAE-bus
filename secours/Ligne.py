file = open("Ligne.txt","w")

patterns = "Insert into Ligne(nomLigne,nArretDepart) values()"

for i in range(5):
    file.write(patterns)
    file.write("\n")



