file = open("TempsTrajet.txt", "a+")

for i in range(136):
    file.write("Insert into TempsTrajet(nArretA,nArretB,intervalleTemps) values(,,);")
    file.write("\n")
