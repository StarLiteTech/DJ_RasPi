import Tkinter as Tk
from views import HomeView

class HomeController():
    def __init__(self):
        self.root = Tk.Tk()
        self.view = HomeView.HomeView(self.root)
        self.makeButtonFrame()                
        self.view.frame.pack()
        

    def makeButtonFrame(self):
        # Set up the frame
        self.view.buttonFrame = Tk.Frame(self.view.frame)
        

        # Set up the Albums button
        self.view.albumsButton = Tk.Button(self.view.buttonFrame, text="Albums", command=self.albumsButtonCB)
        self.view.albumsButton.grid(row=0, sticky="nsew")
        # Set up the Artists button
        self.view.artistsButton = Tk.Button(self.view.buttonFrame, text="Artists", command=self.artistsButtonCB)
        self.view.artistsButton.grid(row=0, column=1, sticky="nsew")
        
        # Set up the Playlists button
        self.view.playlistsButton = Tk.Button(self.view.buttonFrame, text="Playlists", command=self.playlistsButtonCB)
        self.view.playlistsButton.grid(row=1, column=0, sticky="nsew")
        
        # Set up the Songs button
        self.view.songsButton = Tk.Button(self.view.buttonFrame, text="Songs", command=self.songsButtonCB)
        self.view.songsButton.grid(row=1, column=1, sticky="nsew")
        
        self.view.buttonFrame.pack() 

    def run(self):
        self.root.title("DJ RasPi")
        self.root.deiconify()
        self.root.mainloop()

    def albumsButtonCB(self):
        self.view.status.set("Albums button pressed")
        self.view.statusLabel.pack()
        self.view.frame.pack()


    def artistsButtonCB(self):
        self.view.status.set("Artists button pressed")
        self.view.statusLabel.pack()
        self.view.frame.pack()


    def playlistsButtonCB(self):
        self.view.status.set("Playlists button pressed")
        self.view.statusLabel.pack()
        self.view.frame.pack()


    def songsButtonCB(self):
        self.view.status.set("Songs button pressed")
        self.view.statusLabel.pack()
        self.view.frame.pack()
