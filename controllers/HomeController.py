import Tkinter as Tk
from views import HomeView

class HomeController():
    def __init__(self):
        self.root = Tk.Tk()
        self.view = HomeView(self.root)
        

    def run(self):
        self.root.title("DJ RasPi")
        self.root.deiconify()
        self.root.mainloop()
