from pprint import pprint

import pandas as pd
from numpy import NaN

df = pd.read_excel('cool.xlsx')

print(df)

df['c'] = df['c'].astype('str')  # Allow putting strings in `c` column.

print("1.  Combine `A` and `B` into `C` by concatenation.")
for i, row in df.iterrows():
    # print("Row is:")
    # print(row)

    a = str(row['a'])
    b = str(row['b'])

    concat = a + b

    df.set_value(i, 'c', concat)
print(df)

print("2.  Count all the duplicates of `C` and store them in `D`.")
seen = {}
for i, row in df.iterrows():  # Count 'em up
    c = row['c']

    if c not in seen: # Haven't seen letter before
        seen[c] = 0

    seen[c] += 1 # Seen letter `c` once, add one.

for i, row in df.iterrows(): # Put the recorded numbers in, not we looping through each row, to get the value of c to call it as a key in the dict
    c = row['c']

    times_seen = seen[c]

    df.set_value(i, 'd', times_seen)
pprint(seen)
print(df)

print("3.  Remove all rows where `D` is `1`.") # go thorugh df, and have index's, if column d is 1, put into list called should drop, build it while iterating and drop at end
should_drop = []
for i, row in df.iterrows():
    d = row['d']

    if (d == 1.0):
        should_drop.append(i)

print("Dropping the following rows:")
print(should_drop)
df.drop(df.loc
        [should_drop], inplace=True)
print(df)

print("4.  Remove all rows where `F` is `CANCELLED`.")
should_drop = []

for i, row in df.iterrows():
    f = row['f']

    if str(f) == 'CANCELLED':
        should_drop.append(i)

print("Dropping the following rows:")
print(should_drop)
df.drop(df.index[should_drop], inplace=True)
print(df)
