#!/usr/bin/python3
import os
import shutil

# vars
number_of_lines_per_file = 500000
filename = os.listdir('input')[0]
filename = f"./input/{filename}"
header = "MMS Id\n" # don't forget the newline \n

# clean-up
folder = './output/'
shutil.rmtree(folder)
os.mkdir(folder)

# open source file and split by number of lines
with open(filename,'r') as file:
    l = file.readlines()
    n = number_of_lines_per_file

# using list comprehension, split into seperate files
x = [l[i:i + n] for i in range(0, len(l), n)]

int = 0
chunk_totals = 0

for chunk in x:
    # add chunk total
    chunk_total = len(chunk)

    # insert header at beginning of list
    if chunk[0] != header:
        chunk.insert(0, header)
        chunk_totals += chunk_total # add list len to chunk totals running count
    else:
        chunk_totals += chunk_total - 1 # remove 1 from total if already has header

    # write to files    
    int += 1
    with open(f".\output\{int}_SPLIT.txt",'w', newline=None) as out:
        out.write(''.join(chunk))

# final
print()
print("----------------------------------------------------------------")
print("Done.")
print("----------------------------------------------------------------")
print(f"Total members: {chunk_totals:,}")
print()