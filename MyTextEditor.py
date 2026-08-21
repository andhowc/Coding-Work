'''An attempt to make a simple text editor'''

# p14-3 program in the Jap text I like using

import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog

'''This is how tkinter allows widgets and callback functions be initiated'''

class MyFrame(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('The Editor')

        '''for the menu bar with \
        menubar >> file menu >> Open, Save as , Exit'''
        
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = 'Open', command = self.openfile)
        filemenu.add_command(label = 'Save as', command = self.saveas)
        filemenu.add_command(label = 'Exit', command = self.master.destroy)
        menubar.add_cascade(label = 'File', menu = filemenu)
        self.master.config(menu = menubar)

        '''text widgetfor editing a class using editbox'''
        self.editbox = tk.Text(self)
        self.editbox.pack()


        '''Method to open a file, using own 'self' parameter'''
        
    def openfile(self):
        '''Obtain the file name via the filedialog box'''
        filename = tk.filedialog.askopenfilename()
        
        if filename:
            tk.messagebox.showinfo("Filename", "Open: "+filename)

            '''Open a file with variable named file using with statement'''
            with open (filename,'r') as file:
                text = file.read()

            '''set the file contents in the editboc Text widget'''

            self.editbox.delete('1.0', tk.END)
            self.editbox.insert('1.0', text)

        else:
            tk.messagebox.showinfo("Filename", "Cancelled")


    '''Methods for saving the files so created'''
    
    def saveas(self):
        
        '''Open a file with a variable named file using with statement'''
        filename = tk.filedialog.asksaveasfilename()
        
        if filename:
            
            with open (filename,'w') as file:
                file.write(self.editbox.get('1.0',tk.END))
                
            tk.messagebox.showinfo("Filename", "Save as: "+filename)

        else:
            tk.messagebox.showinfo("Filename", "Cancelled")

'''Main program from here'''
root    = tk.Tk()
f       = MyFrame(root)
f.pack()
f.mainloop()
