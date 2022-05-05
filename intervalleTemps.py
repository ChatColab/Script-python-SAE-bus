#init
patterns = "Insert into TempsTrajet (nArretA,nArretB,intervalleTemps) values"

inter_file = open("arret.txt","r")
final_file = open("interFinal.txt", "w")



#split inter_file into 3 columns separated by ,
for line1 in inter_file:
    line1 = line1.split(",")
    for i in range(len(line1)):
        line1[i] = line1[i].replace("\n","")
    for i in range(0, 2):
        cpt=1
        arret_file = open("doublon.txt", "r")
        for line in arret_file:
            if str(line1[i]) in line:
                line1[i] = str(cpt)
            cpt+=1
        arret_file.close()
    final_file.write(patterns + '(' + str(line1[0]) + ',' + str(line1[1]) + ',' + str(line1[2]) + ');' + "\n")
    
        
                    



# for index, row in df_arret.iterrows():
#     final_file.write(patterns + '(' + arreta12[index] + ',' + arretb12[index] + ',' + str(int(row['Temps12'])) + ');' + "\n")
#     final_file.write(patterns + '(' + arreta13[index] + ',' + arretb13[index] + ',' + str(int(row['Temps13'])) + ');' + "\n")
#     final_file.write(patterns + '(' + arreta14[index] + ',' + arretb14[index] + ',' + str(int(row['Temps14'])) + ');' + "\n")
#     final_file.write(patterns + '(' + arreta15[index] + ',' + arretb15[index] + ',' + str(int(row['Temps15'])) + ');' + "\n")

# #close all files

final_file.close()
inter_file.close()
