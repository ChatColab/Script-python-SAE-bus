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


final_file = open('intervalleTemps.txt', 'w')

#le truc ci-dessous marche
# for i in range(0, len(df_arret['ArretA12'])):
#     final_file.write(df_arret['ArretA12'][i] + ' ' + '\n')

with open('arret.txt') as arret_file:
    for num, line in enumerate(arret_file, 1):
        for i in range(0, len(df_arret['ArretA12'])):
            if str(df_arret['ArretA12'][i]) in line:
                final_file.write(df_arret['ArretA12'][i] + ' ' + str(num) + '\n')
        for i in range(0, len(df_arret['ArretB12'])):
            if str(df_arret['ArretB12'][i]) in line:
                final_file.write(df_arret['ArretB12'][i] + ' ' + str(num) + '\n')
        for i in range(0, len(df_arret['ArretA13'])):
            if str(df_arret['ArretA13'][i]) in line:
                final_file.write(df_arret['ArretA13'][i] + ' ' + str(num) + '\n')
        for i in range(0, len(df_arret['ArretB13'])):
            if str(df_arret['ArretB13'][i]) in line:
                final_file.write(df_arret['ArretB13'][i] + ' ' + str(num) + '\n')
        for i in range(0, len(df_arret['ArretA14'])):
            if str(df_arret['ArretA14'][i]) in line:
                final_file.write(df_arret['ArretA14'][i] + ' ' + str(num) + '\n')
        for i in range(0, len(df_arret['ArretB14'])):
            if str(df_arret['ArretB14'][i]) in line:
                final_file.write(df_arret['ArretB14'][i] + ' ' + str(num) + '\n')
        for i in range(0, len(df_arret['ArretA15'])):
            if str(df_arret['ArretA15'][i]) in line:
                final_file.write(df_arret['ArretA15'][i] + ' ' + str(num) + '\n')
        for i in range(0, len(df_arret['ArretB15'])):
            if str(df_arret['ArretB15'][i]) in line:
                final_file.write(df_arret['ArretB15'][i] + ' ' + str(num) + '\n')
                
        # final_file.write(line)
        # final_file.write(str(num))
        # final_file.write('\n')


# for index, row in df_arret.iterrows():
#     final_file.write(row['ArretA12'])


final_file.write("eyow")
arret_file.close()
final_file.close()

# #remove the (arreta, arretb, temps) lines where there is a dublon of arreta and arretb combination
# df_arret = df_arret.drop_duplicates(subset=['ArretA12', 'ArretB12'])


#final_file = open('intervalleTemps.txt','w')

#write df arret in intervalleTemps.txt
# for index, row in df_arret.iterrows():
#     final_file.write(patterns + '(' + str(row['ArretA12']) + ',' + str(row['ArretB12']) + ',' + str(int(row['Temps12'])) + ');' + "\n")
#     final_file.write(patterns + '(' + str(row['ArretA13']) + ',' + str(row['ArretB13']) + ',' + str(int(row['Temps13'])) + ');' + "\n")
#     final_file.write(patterns + '(' + str(row['ArretA14']) + ',' + str(row['ArretB14']) + ',' + str(int(row['Temps14'])) + ');' + "\n")
#     final_file.write(patterns + '(' + str(row['ArretA15']) + ',' + str(row['ArretB15']) + ',' + str(int(row['Temps15'])) + ');' + "\n")

# final_file.close()