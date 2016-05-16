import Tkinter as Tk

class HomeView:
    def __init__(self, master):
        self.mainFrame = Tk.Frame(master)
        
        # This is the status label at the top of the Home View
        self.status = Tk.StringVar()
        self.status.set("Welcome to DJ RasPi!")
        self.statusLabel = Tk.Label(self.mainFrame, textvariable=self.status)
        self.statusLabel.grid(row=0, sticky="nsew")
        self.mainFrame.pack()
        
