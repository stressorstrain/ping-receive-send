#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter as Tk
from pingin import jstping
from ftping import login, download, upload

class Window(Tk.Tk):
    def __init__(self, parent):
        Tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
       
        self.v1 = Tk.IntVar(value=1)
        self.v2 = Tk.StringVar(value=1)
        self.l0 = Tk.Label(self, text= "Server Status", fg='white', bg='black')
        self.l0.grid(column=0, row=0, sticky='EW')
        self.l1 = Tk.Label(self, text= "Host Status", fg='white', bg='black')
        self.l1.grid(column=0, row=2, sticky='EW')

        self.rd0 = Tk.Radiobutton(self, text = None, value=self.v1, bg='black', selectcolor='red')
        self.rd0.grid(column=1,row=0,sticky='EW')
        #self.rd0.deselect()
        self.rd1 = Tk.Radiobutton(self,text = None, value=self.v1, bg='black', selectcolor = 'red')
        self.rd1.grid(column=1,row=2,sticky='EW')
        #self.rd1.deselect()
        #ping_select(self)
        
        #button1 = Tk.Button(self,  text = "Click here", command=select)
        #button1.grid(column=3,row=0)

        #label = Tkinter.Label(self, anchor="w", fg="white", bg="black")
        #label.grid(column=0,row=1,columnspan=2,sticky="EW")

        self.grid_columnconfigure(0, weight=1)

        self.select()

    def select(self):
            
        #self.rd1.configure(selectcolor='red')
        server_stats = jstping()
        if server_stats == True:
            self.rd0.configure(selectcolor='green')
            self.rd0.select()
        else:
            self.rd0.select()    

if __name__ == "__main__":
    #var = IntVar()
    root = Window(None)
    root.title('Music Box')
    root.configure(bg='black')
    root.mainloop()
    

    
