import TKinter as Tk

class HomeController():
    def __init__(self):
        self.root(Tk.TK())
        

    def run(self):
        self.root.title("DJ RasPi")
        self.root.deiconify()
        self.root.mainloop()
