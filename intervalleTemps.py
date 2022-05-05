from wsgiref.util import shift_path_info
import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
patterns = "Insert into TempsTrajet (nArretA,nArretB,intervalleTemps) values"

df_arret = df [['ArretA12', 'ArretB12', 'Temps12', 'ArretA13', 'ArretB13', 'Temps13', 'ArretA14', 'ArretB14', 'Temps14', 'ArretA15', 'ArretB15', 'Temps15']]

#remove all nan values
df_arret = df_arret.dropna()


arreta12 = df_arret.astype(str)['ArretA12']
arretb12 = df_arret.astype(str)['ArretB12']
arreta13 = df_arret.astype(str)['ArretA13']
arretb13 = df_arret.astype(str)['ArretB13']
arreta14 = df_arret.astype(str)['ArretA14']
arretb14 = df_arret.astype(str)['ArretB14']
arreta15 = df_arret.astype(str)['ArretA15']
arretb15 = df_arret.astype(str)['ArretB15']

print(arreta12)

inter_file = open("arret.txt","r")
final_file = open("interFinal.txt", "w")

#split inter_file into 3 columns separated by ,
for line1 in inter_file:
    line1 = line1.split(",")
    for i in range(len(line1)):
        line1[i] = line1[i].replace("\n","")
    for i in range(0, 2):
        cpt=1
        arret_file = open("doublon.txt", "r")
        for line in arret_file:
            if str(line1[i]) in line:
                line1[i] = str(cpt)
            cpt+=1
        arret_file.close()

final_file.close()
inter_file.close()
