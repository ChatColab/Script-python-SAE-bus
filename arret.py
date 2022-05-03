import pandas as pd

# init
col_list = []
df = pd.csv("raw.csv", usecol=col_list)
pattern = "Insert into Arret(nomArret) values "

# ecriture des lignes finale dans une liste
final_list = []
col = df["arret"]
i = 0
for line in col:
    final_list[i] = pattern + "({df["arret"][i]})"
    i++

# ecriture dans un nouveau fichier texte
f = open("data.txt",a+)
for line in final_list:
    f.write(line)
