import glob
import pandas as pd
import os
import numpy as np
import time

print(os.getcwd())
df=pd.read_csv(f"{os.getcwd()}/data/BL-Flickr-Images-Book.csv")
print(df)
df.head()

to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

df.drop(to_drop, inplace = True, axis = 1)
df.head()

df.set_index('Identifier', inplace = True)
df.head()

df['Date of Publication'].head(25)

unwanted_characters = ['[', ',', '-',']','?']

def clean_dates(row):
    dop= str(row['Date of Publication']).strip()
    
    if dop == 'nan' or dop[0] == '[':
        return np.nan
    
    for character in unwanted_characters:
        if character in dop:
            print(f"{dop} before")
            character_index = dop.find(character)
            dop = dop[:character_index]
            print(f"{dop} after")
    
    return dop

df['Date of Publication'] = df.apply(clean_dates, axis = 1)



