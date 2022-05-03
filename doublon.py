import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
#get all columns with ArretA and ArretB as title from 12 to 15
df_arret = df[['ArretA12', 'ArretB12', 'ArretA13', 'ArretB13', 'ArretA14', 'ArretB14', 'ArretA15', 'ArretB15']]

# make a list of all the stops
df_arretA = df_arret.iloc[:,0]
df_arretA = df_arretA.append(df_arret.iloc[:,2])
df_arretA = df_arretA.append(df_arret.iloc[:,4])
df_arretA = df_arretA.append(df_arret.iloc[:,6])

df_arretB = df_arret.iloc[:,1]
df_arretB = df_arretB.append(df_arret.iloc[:,3])
df_arretB = df_arretB.append(df_arret.iloc[:,5])
df_arretB = df_arretB.append(df_arret.iloc[:,7])

df_arret = df_arretA.append(df_arretB)
# drop duplicates
df_arret = df_arret.drop_duplicates()
print(df_arret)


final_file = open('arret.txt','w')

for line in df_arret:
    final_file.write(str(line))
    final_file.write('\n')
########################################
final_file.close()
