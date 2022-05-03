import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
patterns = "Insert into TempsTrajet (nArretA,nArretB,intervalleTemps) values"

df_arret = df [['ArretA12', 'ArretB12', 'Temps12', 'ArretA13', 'ArretB13', 'Temps13', 'ArretA14', 'ArretB14', 'Temps14', 'ArretA15', 'ArretB15', 'Temps15']]

#remove all nan values
df_arret = df_arret.dropna()

#remove lines where 

# #remove the (arreta, arretb, temps) lines where there is a dublon of arreta and arretb combination
# df_arret = df_arret.drop_duplicates(subset=['ArretA12', 'ArretB12'])

#write all df-arret in intervalleTemps.txt
final_file = open('intervalleTemps.txt','w')

#write df arret in intervalleTemps.txt
for index, row in df_arret.iterrows():
    final_file.write(patterns + '(' + str(row['ArretA12']) + ',' + str(row['ArretB12']) + ',' + str(int(row['Temps12'])) + ');' + "\n")
    final_file.write(patterns + '(' + str(row['ArretA13']) + ',' + str(row['ArretB13']) + ',' + str(int(row['Temps13'])) + ');' + "\n")
    final_file.write(patterns + '(' + str(row['ArretA14']) + ',' + str(row['ArretB14']) + ',' + str(int(row['Temps14'])) + ');' + "\n")
    final_file.write(patterns + '(' + str(row['ArretA15']) + ',' + str(row['ArretB15']) + ',' + str(int(row['Temps15'])) + ');' + "\n")

final_file.close()