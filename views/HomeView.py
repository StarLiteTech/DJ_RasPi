import Tkinter as Tk

class HomeView:
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.status = Tk.StringVar()
        self.status.set("Welcome to DJ RasPi!")
        self.statusLabel = Tk.Label(master, textvariable=self.status)
        self.statusLabel.pack()
        
        self.frame.pack()
