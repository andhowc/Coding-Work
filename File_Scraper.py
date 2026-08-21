# Basic file/word sraper

# This project is an attempt to create a basic file scraping too,,
##and gain access to quick insights into the frequency of words use
##in an average exam script.

##the output will be useful in helping the student create meaningful
##typing exercises say. Eventually building speed in writing words
##that are commonplace in their field of expertise.

import os, sys, re, csv
import tkinter as tk
from tkinter import filedialog
import pathlib


root=tk.Tk()
root.withdraw()     #hides the tkinter window


    # this allows choosing of file, and handling of exception

try:
    filelink=filedialog.askopenfilename(title = 'Choose file', filetypes =
[('Word files', '*.txt'),('CSV files', '*.csv')]) # may also use ('PDF files','*.pdf')

except ImportError:
    print('Missing module')

if filelink: pass
else: print('No file selected')

os.chdir('C:\\Users\\Ndu\\Downloads\\Python_R_VBA\\Scripts')

    # spells out characters to leave out of the analysis

spec_chars  = r'[^a-zA-Z0-9\s]'   # apparently called the regex pattern to match the special characters
non_words   = r'[^\w\s]'          # gives all other non-word chars in the source file

    # working on the loaded file text, the data is turned to lower case
    # and the special characters are removed using real expressions

with open(filelink,'r') as file:
    f   =file.read()
    f   =f.lower()

    #  below we rid the text of non-alphanumeric characters
    
    text    = re.sub(spec_chars,' ',f)
    clr_txt = re.sub(non_words,' ',text)
    ftr     = clr_txt.replace('\n',' ').replace('\r','')

    #.replace('\t','').strip().replace('\r','')
    # may have been used but were yielding creepy results


    fstr    = str(ftr)
    str1    = fstr.lstrip().split(' ', len(fstr))
    set1    = set(str1)
    

# the list to hold the words and counts is created, and filled up

tofile = []
    
for i in set1:
    #print(i, '\t',str1.count(i))
    u   = [i, str1.count(i)]
    tofile.append(u)


#this section prints the outcome to screen and file

print(tofile)

# The hope is this adds to ore convenience to the user, and allows me to cook
# with other modules.


filename = filedialog.asksaveasfilename(title = 'Choose file name', filetypes =
[('Word files', '*.txt'),('CSV files', '*.csv')])

with open(filename,'w',newline='') as of:
    

# applies to csv
    writer = csv.writer(of)
    writer.writerow(['Source file:',filelink,'\n'])
    writer.writerow(['Word','Frequency'])
    writer.writerows(tofile)

os.startfile(filename)      # Opens the file written to recently

# Nest steps
        
# Possible output is the use of the same file name, only appended
# the version of the file being written to.
# giving the user the ability to choose the I/O file types eg
# PDF, txt, docx and xlxs
# Extend the model to work with the relevant modules eg b4s for PDFs

