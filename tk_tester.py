import tkinter as tk

class Gui():

    def __init__(self): #initiate GUI elements
        self.gui = tk.Tk()
        self.gui.title('Clipboard Tester')
        self.gui.geometry('500x500')
        self.gui.configure(background='#000000')

        copy1 = tk.Button(self.gui, text='1', bd=1).grid(row=0, column=0)
        copy2 = tk.Button(self.gui, text='2', bd=1).grid(row=0, column=1)
        copy3 = tk.Button(self.gui, text='3', bd=1).grid(row=0, column=2)
        copy4 = tk.Button(self.gui, text='4', bd=1).grid(row=0, column=3)
        copy5 = tk.Button(self.gui, text='5', bd=1).grid(row=0, column=4)
        copy6 = tk.Button(self.gui, text='6', bd=1).grid(row=1, column=0)
        copy7 = tk.Button(self.gui, text='7', bd=1).grid(row=1, column=1)
        copy8 = tk.Button(self.gui, text='8', bd=1).grid(row=1, column=2)
        copy9 = tk.Button(self.gui, text='9', bd=1).grid(row=1, column=3)
        copy0 = tk.Button(self.gui, text='0', bd=1).grid(row=1, column=4)
        sep1 = tk.Label(self.gui, text='Copy Above', bg='#000000', fg='#ffffff', width=10).grid(row=2, column=1)
        paste1 = tk.Button(self.gui, text='1', bd=1).grid(row=3, column=0)
        paste2 = tk.Button(self.gui, text='2', bd=1).grid(row=3, column=1)
        paste3 = tk.Button(self.gui, text='3', bd=1).grid(row=3, column=2)
        paste4 = tk.Button(self.gui, text='4', bd=1).grid(row=3, column=3)
        paste5 = tk.Button(self.gui, text='5', bd=1).grid(row=3, column=4)
        paste6 = tk.Button(self.gui, text='6', bd=1).grid(row=4, column=0)
        paste7 = tk.Button(self.gui, text='7', bd=1).grid(row=4, column=1)
        paste8 = tk.Button(self.gui, text='8', bd=1).grid(row=4, column=2)
        paste9 = tk.Button(self.gui, text='9', bd=1).grid(row=4, column=3)
        paste0 = tk.Button(self.gui, text='0', bd=1).grid(row=4, column=4)

        
        self.gui.mainloop()
Gui()