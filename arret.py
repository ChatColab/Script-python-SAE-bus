import pandas as pd

# init
file = open("arret.txt","r")

# put every line in a list
list = file.readlines()
patterns = "Insert into Arret(nomArret) values "
print(list)

final_list = []
for line in list:
    final_list.append(patterns + " (" + line + ");")
print(final_list)
