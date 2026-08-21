# This module attempts to derive a saw wave by using a sum of sines

from math import *
import tkinter as tk
import tkinter.filedialog
import os

# declaring the variables

n=0
terms=4
wchart=[]

for n in range(0,400):
    saw = 0
    waved=[]
    sum=0
    
    for i in range(1,terms+1):
        y=sin(i*n*pi/180)
        if i==0: saw=y/1
        else: saw = y/i
        waved.append(saw)
        sum+=saw
        next
    waved.append(sum)
    wchart.append(waved)
    next

print(wchart)

# This section aims to wtite to file
wchart

with open('Wavechart2.txt','w') as f:
    for row in wchart:
        row_str=''.join(map(str,row))
        f.write(row_str +'\n')
