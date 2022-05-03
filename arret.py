import pandas as pd

file = open("arret.txt","r")

list = file.readlines()
patterns = "Insert into Arret(nomArret) values "
print(list)

final_list = []
for line in list:
    final_list.append(patterns + '("' + line[:-1] + '");' + "\n")

print(final_list)

final_file = open("arretFinal.txt","w")

for line in final_list:
    final_file.write(line)

file.close()
final_file.close()
