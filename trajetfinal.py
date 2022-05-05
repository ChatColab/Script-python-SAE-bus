from wsgiref.util import shift_path_info
import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
patterns = "Insert into TempsTrajet (nLigne,nArretA,nArretB) values"

df_arret = df [['ArretA12', 'ArretB12', 'ArretA13', 'ArretB13', 'ArretA14', 'ArretB14', 'ArretA15', 'ArretB15']]

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


for i in range(0, len(df_arret['ArretA12'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretA12'][i]) in line:
            arreta12[i] = str(cpt)
        cpt+=1
    arret_file.close()
for i in range(0, len(df_arret['ArretB12'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretB12'][i]) in line:
            arretb12[i] = str(cpt)
        cpt+=1
    arret_file.close()
for i in range(0, len(df_arret['ArretA13'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretA13'][i]) in line:
            arreta13[i] = str(cpt)
        cpt+=1
    arret_file.close()
for i in range(0, len(df_arret['ArretB13'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretB13'][i]) in line:
            arretb13[i] = str(cpt)
        cpt+=1
    arret_file.close()
for i in range(0, len(df_arret['ArretA14'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretA14'][i]) in line:
            arreta14[i] = str(cpt)
        cpt+=1
    arret_file.close()
for i in range(0, len(df_arret['ArretB14'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretB14'][i]) in line:
            arretb14[i] = str(cpt)
        cpt+=1
    arret_file.close()
for i in range(0, len(df_arret['ArretA15'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretA15'][i]) in line:
            arreta15[i] = str(cpt)
        cpt+=1
    arret_file.close()
for i in range(0, len(df_arret['ArretB15'])):
    cpt=1
    arret_file = open("doublon.txt", "r")
    for line in arret_file:
        if str(df_arret['ArretB15'][i]) in line:
            arretb15[i] = str(cpt)
        cpt+=1
    arret_file.close()

final_file = open('trajet.txt','w')

for index, row in df_arret.iterrows():
    final_file.write(patterns + '(1,' + arreta12[index] + ',' + arretb12[index] + ');' + "\n")
    final_file.write(patterns + '(2,' + arreta13[index] + ',' + arretb13[index] + ');' + "\n")
    final_file.write(patterns + '(3,' + arreta14[index] + ',' + arretb14[index] + ');' + "\n")
    final_file.write(patterns + '(4,' + arreta15[index] + ',' + arretb15[index] + ');' + "\n")

    

final_file.close()



# inter_file = open("arret.txt","r")
# final_file = open("interFinal.txt", "w")

# #split inter_file into 3 columns separated by ,
# for line1 in inter_file:
#     line1 = line1.split(",")
#     for i in range(len(line1)):
#         line1[i] = line1[i].replace("\n","")
#     for i in range(0, 2):
#         cpt=1
#         arret_file = open("doublon.txt", "r")
#         for line in arret_file:
#             if str(line1[i]) in line:
#                 line1[i] = str(cpt)
#             cpt+=1
#         arret_file.close()
#     final_file.write(patterns + '(' + str(line1[0]) + ',' + str(line1[1]) + ',' + str(line1[2]) + ');' + "\n")

# final_file.close()
# inter_file.close()



# final_file = open('trajet.txt','w')

# for index, row in df_arret.iterrows():
#     final_file.write(patterns + '(' + str(row['ArretA12']) + ',' + str(row['ArretB12']) + ',' + str(int(row['Temps12'])) + ');' + "\n")
#     final_file.write(patterns + '(' + str(row['ArretA13']) + ',' + str(row['ArretB13']) + ',' + str(int(row['Temps13'])) + ');' + "\n")
#     final_file.write(patterns + '(' + str(row['ArretA14']) + ',' + str(row['ArretB14']) + ',' + str(int(row['Temps14'])) + ');' + "\n")
#     final_file.write(patterns + '(' + str(row['ArretA15']) + ',' + str(row['ArretB15']) + ',' + str(int(row['Temps15'])) + ');' + "\n")
    

# final_file.close()