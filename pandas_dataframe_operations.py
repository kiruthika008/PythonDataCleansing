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

unwanted_characters = ['[', ',', '-',']','?',' ']


def clean_dates_other(row):
    dop= str(row['Date of Publication']).strip()
    print(dop)
    if dop == 'nan' or dop[0] == '[':
        return np.nan
    else:
        split_list = [i for i in dop]
        print(split_list)
        for i in split_list:
            if i in unwanted_characters:
                character_index = split_list.index(i)  # to find index of value i for list if strings use find(i)
                print(character_index)
                dop = dop[:character_index]
                break
        print(f"{dop} after")
        return dop

df['Date of Publication'] = df.apply(clean_dates_other, axis = 1)
df['Date of Publication'].to_csv(f"{os.getcwd()}/data/output.csv")







