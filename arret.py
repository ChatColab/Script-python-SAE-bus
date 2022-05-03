import pandas as pd

# init
file = open("arret.txt","r")

# put every line in a list
list = file.readlines()
patterns = "Insert into Arret(nomArret) values "
print(list)

final_list = []
for line in list:
    # append patterns + line and splice the 2 last char of the line
    final_list.append(patterns + '("' + line[:-1] + '");' + "\n")

print(final_list)

final_file = open("arretFinal.txt","w")

for line in final_list:
    final_file.write(line)

file.close()
final_file.close()
