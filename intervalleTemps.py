import pandas as pd

df = pd.read_csv('Lignes.csv')
patterns = "Insert into TempsTrajet (nArretA,nArretB,intervalleTemps) values"
