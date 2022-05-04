from wsgiref.util import shift_path_info
import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
patterns = "Insert into TempsTrajet (nArretA,nArretB,intervalleTemps) values"

df_arret = df [['ArretA12', 'ArretB12', 'Temps12', 'ArretA13', 'ArretB13', 'Temps13', 'ArretA14', 'ArretB14', 'Temps14', 'ArretA15', 'ArretB15', 'Temps15']]

#remove all nan values
df_arret = df_arret.dropna()

#convert all df_arret values into string
df_arret = df_arret.astype(str)

arreta12 = df_arret.astype(str)['ArretA12']
arretb12 = df_arret.astype(str)['ArretB12']
arreta13 = df_arret.astype(str)['ArretA13']
arretb13 = df_arret.astype(str)['ArretB13']
arreta14 = df_arret.astype(str)['ArretA14']
arretb14 = df_arret.astype(str)['ArretB14']
arreta15 = df_arret.astype(str)['ArretA15']
arretb15 = df_arret.astype(str)['ArretB15']


final_file = open('intervalleTemps.txt', 'w')

with open('doublon.txt') as arret_file:
    for num, line in enumerate(arret_file, 1):
        for i in range(0, len(df_arret['ArretA12'])):
            if str(df_arret['ArretA12'][i]) in line:
                arreta12[i]=str(num)
        for i in range(0, len(df_arret['ArretB12'])):
            if str(df_arret['ArretB12'][i]) in line:
                arretb12[i]=str(num)
        for i in range(0, len(df_arret['ArretA13'])):
            if str(df_arret['ArretA13'][i]) in line:
                arreta13[i]=str(num)
        for i in range(0, len(df_arret['ArretB13'])):
            if str(df_arret['ArretB13'][i]) in line:
                arretb13[i]=str(num)
        for i in range(0, len(df_arret['ArretA14'])):
            if str(df_arret['ArretA14'][i]) in line:
                arreta14[i]=str(num)
        for i in range(0, len(df_arret['ArretB14'])):
            if str(df_arret['ArretB14'][i]) in line:
                arretb14[i]=str(num)
        for i in range(0, len(df_arret['ArretA15'])):
            if str(df_arret['ArretA15'][i]) in line:
                arreta15[i]=str(num)
        for i in range(0, len(df_arret['ArretB15'])):
            if str(df_arret['ArretB15'][i]) in line:
                arretb15[i]=str(num)
                
        # final_file.write(line)
        # final_file.write(str(num))
        # final_file.write('\n')


# for index, row in df_arret.iterrows():
#     final_file.write(row['ArretA12'])

arret_file.close()
final_file.close()

final_file = open('intervalleTemps.txt','w')

for index, row in df_arret.iterrows():
    final_file.write(patterns + '(' + arreta12[index] + ',' + arretb12[index] + ',' + str(row['Temps12']) + ');' + "\n")
    final_file.write(patterns + '(' + arreta13[index] + ',' + arretb13[index] + ',' + str(row['Temps13']) + ');' + "\n")
    final_file.write(patterns + '(' + arreta14[index] + ',' + arretb14[index] + ',' + str(row['Temps14']) + ');' + "\n")
    final_file.write(patterns + '(' + arreta15[index] + ',' + arretb15[index] + ',' + str(row['Temps15']) + ');' + "\n")



final_file.close()

# #remove the (arreta, arretb, temps) lines where there is a dublon of arreta and arretb combination
# df_arret = df_arret.drop_duplicates(subset=['ArretA12', 'ArretB12'])


#final_file = open('intervalleTemps.txt','w')
