#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter

class Window(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entry =  Tkinter.Entry(self, text= "typer here")
        self.entry.grid(column=0, row=0, sticky='EW')

        button1 = Tkinter.Button(self,  text = "Click here")
        button1.grid(column=1,row=0)

        label = Tkinter.Label(self, anchor="w", fg="white", bg="black")
        label.grid(column=0,row=1,columnspan=2,sticky="EW")

        self.grid_columnconfigure(0, weight=1)



if __name__ == "__main__":
    root = Window(None)
    root.title('Music Box')
    root.mainloop()
    
