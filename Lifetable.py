''' This file tries to create a life table i.e. dx, tpx, ux and tqx.
This without using dataframes from NumPy'''


import os, sys, re, csv
import tkinter as tk
from tkinter import filedialog as fd


root=tk.Tk()
root.withdraw() #hides the tkinter window


#this allows choosing of file, and handling of exception

try:
    filelink=fd.askopenfilename(title = 'Choose file', filetypes =
[('CSV files', '*.csv'),('Text files', '*.txt')]) #may also use ('PDF files','*.pdf')

except ImportError:
    print('Missing module')

if filelink: pass
else: print('No file selected')

os.chdir('C:\\Users\\Ndu\\Downloads\\Python_R_VBA\\')

spec_chars =r'[^a-zA-Z0-9\s]'  
non_words = r'[^\w\s]'   

tofile=[]
row=0

with open(filelink,'r') as file:
    f=[line.strip().split(',')[:2] for line in file]
'''the iterable is allowing the file to be read and stripped of any excess non-numeric types'''

b = float(f[5][1])

for row in f[5::]:
    print('check: iter', row[0], 'row[1] =',row[1])
    
    lx = row[1]
    dx = float(lx) - b
    
    try:
        row=[(row[0]),lx, dx, dx/float(lx)]

    except type(row[1]):
        row = ''   
    
    tofile.append(row)
    b = float(row[1])
    next

    '''Need to find a way of calcing and adding more columns to/
    complete the program'''
 
filename=fd.asksaveasfilename(title = 'Choose file name', filetypes =
[('CSV files', '*.csv'),('Word files', '*.txt')])

with open(filename,'a', newline='') as of:
    
    '''# applies to csv'''
    writer=csv.writer(of)
    writer.writerow(f[0])
    writer.writerow(['Age','lx','dx','qx'])
    writer.writerows(tofile)
    of.close()
    
os.startfile(filename)

# Nest steps
        
'# Possible output is the use of the same file name, only appended'
'# the version of the file being written to.'
'# giving the user the ability to choose the I/O file types eg'
'# PDF, txt, docx and xlxs'
'# Extend the model to work with the relevant modules eg b4s for PDFs'

