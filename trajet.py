import pandas as pd

#init
df = pd.read_csv('Lignes.csv')

#get all columns with ArretA as title from 12
df_arretA12 = df.ArretA12
print(df_arretA12)

#get all columns with ArretB as title from 12
df_arretB12 = df.ArretB12
print(df_arretB12)

#get all columns with ArretA as title from 13
df_arretA13 = df.ArretA13
print(df_arretA13)

#get all columns with ArretB as title from 13
df_arretB13 = df.ArretB13
print(df_arretB13)

#get all columns with ArretA as title from 14
df_arretA14 = df.ArretA14
print(df_arretA14)

#get all columns with ArretB as title from 14
df_arretB14 = df.ArretB14
print(df_arretB14)

#get all columns with ArretA as title from 15
df_arretA15 = df.ArretA15
print(df_arretA15)

#get all columns with ArretB as title from 15
df_arretB15 = df.ArretB15
print(df_arretB15)

#convert df_arretA12 to string
df_arretA12 = df_arretA12.astype(str)

#convert df_arretB12 to string
df_arretB12 = df_arretB12.astype(str)

#convert df_arretA13 to string
df_arretA13 = df_arretA13.astype(str)

#convert df_arretB13 to string
df_arretB13 = df_arretB13.astype(str)

#convert df_arretA14 to string
df_arretA14 = df_arretA14.astype(str)

#convert df_arretB14 to string
df_arretB14 = df_arretB14.astype(str)

#convert df_arretA15 to string
df_arretA15 = df_arretA15.astype(str)

#convert df_arretB15 to string
df_arretB15 = df_arretB15.astype(str)

#removeA12 nan values
df_arretA12 = [x for x in df_arretA12 if str(x) != 'nan']

#removeB12 nan values
df_arretB12 = [x for x in df_arretB12 if str(x) != 'nan']

#removeA13 nan values
df_arretA13 = [x for x in df_arretA13 if str(x) != 'nan']

#removeB13 nan values
df_arretB13 = [x for x in df_arretB13 if str(x) != 'nan']

#removeA14 nan values
df_arretA14 = [x for x in df_arretA14 if str(x) != 'nan']

#removeB14 nan values
df_arretB14 = [x for x in df_arretB14 if str(x) != 'nan']

#removeA15 nan values
df_arretA15 = [x for x in df_arretA15 if str(x) != 'nan']

#removeB15 nan values
df_arretB15 = [x for x in df_arretB15 if str(x) != 'nan']

print(df_arretA12)
print(df_arretB12)
print(df_arretA13)
print(df_arretB13)
print(df_arretA14)
print(df_arretB14)
print(df_arretA15)
print(df_arretB15)

final_file = open('arretraw.txt','a+')

#write df_arretA12 in arret.txt
final_file.write(str(df_arretA12))

#write last index of df_arretB12 in arret.txt
final_file.write(df_arretB12[len(df_arretB12)-1])

#write df_arretA13 in arret.txt
final_file.write(str(df_arretA13))

#write last index of df_arretB13 in arret.txt
final_file.write(df_arretB13[len(df_arretB13)-1])

#write df_arretA14 in arret.txt
final_file.write(str(df_arretA14))

#write last index of df_arretB14 in arret.txt
final_file.write(df_arretB14[len(df_arretB14)-1])

#write df_arretA15 in arret.txt
final_file.write(str(df_arretA15))

#write last index of df_arretB15 in arret.txt
final_file.write(df_arretB15[len(df_arretB15)-1])
