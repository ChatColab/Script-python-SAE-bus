#read a csv file
#find the doublon

import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
#get all columns with ArretA and ArretB as title
df_arret = df['ArretA12','ArretB12','ArretA13','ArretB13','ArretA14','ArretB14','ArretA15','ArretB15']

#remove doublon
df_arret = df_arret.drop_duplicates()

#print all arret one by one in lines
for i in range(0,len(df_arret)):
    print(df_arret.iloc[i])

final_file = open ('arret.txt','w')

for i in range(0,len(df_arret)):
    final_file.write(df_arret.iloc[i])

########################################

