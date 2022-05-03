import pandas as pd

df = pd.read_csv('Lignes.csv')

df_arretA = df.ArretA12
df_arretA = df_arretA.append(df.ArretA13)
df_arretA = df_arretA.append(df.ArretA14)
df_arretA = df_arretA.append(df.ArretA15)

df_arretB = df.ArretB12
df_arretB = df_arretB.append(df.ArretB13)
df_arretB = df_arretB.append(df.ArretB14)
df_arretB = df_arretB.append(df.ArretB15)

df_arretA += "   " + df_arretB

#drop duplicate
df_arretA = df_arretA.drop_duplicates()

#print all this shit in intervalleTemps.txt with mode a+
with open('intervalleTemps.txt', 'a+') as f:
    for i in df_arretA:
        f.write(i)
        f.write("\n")