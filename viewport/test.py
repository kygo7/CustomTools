import tkinter as tk


class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #INTEGER
        self.integer = tk.IntVar()
        self.integer.set(0)
        #BUTTONS
        tk.Button(self, text='Quit', command=self.destroy).pack()
        tk.Button(self, text='+', command=self.plus_one).pack()
        tk.Button(self, text='-', command=self.take_one).pack()
        #ENTRY
        self.entry0 = tk.Entry(self, textvariable=str(self.integer), justify="center", width=4)
        self.entry0.pack()

    def plus_one(self):
        x =  self.integer.get() + 1
        self.integer.set(x)

    def take_one(self):
        x =  self.integer.get() - 1
        self.integer.set(x)

app = Main()
app.mainloop()