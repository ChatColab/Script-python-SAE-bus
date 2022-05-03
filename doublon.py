import pandas as pd

#init
df = pd.read_csv('Lignes.csv')
#get all columns with ArretA and ArretB as title from 12 to 15
df_arret = df[['ArretA12', 'ArretB12', 'ArretA13', 'ArretB13', 'ArretA14', 'ArretB14', 'ArretA15', 'ArretB15']]

#convert df_arret to string list
df_arret = df_arret.applymap(str)

#convert df_arret to one list
df_arret = df_arret.stack().to_list()

#remove dublon
df_arret = list(set(df_arret))

#remove nan values
df_arret = [x for x in df_arret if str(x) != 'nan']

print(df_arret)


final_file = open('arret.txt','w')

for line in df_arret:
    final_file.write(str(line))
    final_file.write('\n')
########################################
final_file.close()
