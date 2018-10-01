#firstarts
# by default pandas assumes reading excel as a number
for i, row in df.iterrows() # every dataframe (nice to have for iterating over rows) has this function to iteratie

a = str(row['a'])
b = str(row['b'])

concat = a + b

df.set_value(i,'c', concat)# i represents the row number, at row i at column C, set that value to concat

# now we are going to count all of the duplicates of C, and stored in D

seen={} # create empty dict
for i , row in df.itterows(): # itterate over the rows again 

# if we have not seen lettter in dict, we count as zero because now it has something too look up against while looping through, to ensure step bellow
#dictionaries cant have the same keys
#


