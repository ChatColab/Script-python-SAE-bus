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

final_file = open('trajet.txt','w')

for index, row in df_arret.iterrows():
    final_file.write(patterns + '(' + arreta12[index] + ',' + arretb12[index] + ',' + "\n")
    final_file.write(patterns + '(' + arreta13[index] + ',' + arretb13[index] + ',' + "\n")
    final_file.write(patterns + '(' + arreta14[index] + ',' + arretb14[index] + ',' + "\n")
    final_file.write(patterns + '(' + arreta15[index] + ',' + arretb15[index] + ',' + "\n")

final_file.close()