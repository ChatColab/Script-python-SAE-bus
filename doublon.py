import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
#get all columns with ArretA and ArretB as title
df_arret = df.ArretA12
df_arret = df_arret.append(df.ArretB12)
df_arret = df_arret.append(df.ArretA13)
df_arret = df_arret.append(df.ArretB13)
df_arret = df_arret.append(df.ArretA14)
df_arret = df_arret.append(df.ArretB14)
df_arret = df_arret.append(df.ArretA15)
df_arret = df_arret.append(df.ArretB15)


#remove doublon
df_arret = df_arret.drop_duplicates()

#print all arret one by one in lines
for i in range(0,len(df_arret)):
    print(df_arret.iloc[i])

final_file = open('arret.txt','w')

for line in df_arret:
    final_file.write(line)
    final_file.write('\n')
########################################
final_file.close()
