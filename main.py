from Tkinter import*
from PIL import Image, ImageTk
import ttk
import turtle
import tkcolorpicker 
import tkMessageBox as messagebox
import re
import FractalsArt as frac
import CalligraphyArt as cal



#######MAIN WINDOW INTERFACE#########

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1000x600')
        self.root.title("Geometric Art")
        self.root.resizable(False,False)
        self.root.configure(background='#888888')
        self.bg = '#e9e9e9'
        self.font = ("Helvetica", 12)

                            
        self.main_cnv = Canvas(self.root, bg = "#e9e9e9", width = 1000, height = 600)
        self.main_cnv.pack()
        
        #background image
        self.left_image = Image.open("resources/plant.png")
        self.left_photo = ImageTk.PhotoImage(self.left_image)
        self.main_cnv.create_image(600,400, image = self.left_photo)
        
        
        #title
        self.main_cnv.create_text(480,70, text = "Geometry Art", font = ("Bucket O Blood",120), fill = "#0e969e")
##        self.main_cnv.create_text(270,70, text = "e", font = ("Bucket O Blood",120), fill = "#0e9e96")
##        self.main_cnv.create_text(320,50, text = "o", font = ("Bucket O Blood",120), fill = "#0e9e81")
##        self.main_cnv.create_text(370,70, text = "m", font = ("Bucket O Blood",120), fill = "#0e9e72")
##        self.main_cnv.create_text(420,50, text = "e", font = ("Bucket O Blood",120), fill = "#0e9e58")
##        self.main_cnv.create_text(470,70, text = "t", font = ("Bucket O Blood",120), fill = "#0e9e32")
##        self.main_cnv.create_text(520,50, text = "r", font = ("Bucket O Blood",120), fill = "#1e9e0e")
##        self.main_cnv.create_text(570,70, text = "i", font = ("Bucket O Blood",120), fill = "#459e0e")
##        self.main_cnv.create_text(620,50, text = "c", font = ("Bucket O Blood",120), fill = "#5d9e0e")
##        self.main_cnv.create_text(690,70, text = "A", font = ("Bucket O Blood",120), fill = "#889e0e")
##        self.main_cnv.create_text(740,50, text = "r", font = ("Bucket O Blood",120), fill = "#9e960e")
##        self.main_cnv.create_text(790,70, text = "t", font = ("Bucket O Blood",120), fill = "#9e750e")
                                  
                                  
                                  
                                  
        #main menu items binded with their callbacks                         
        self.main_cnv.create_text(500,250, text = "Fractals Art", font = ("Bucket O Blood",60), fill = "#100dd8", tag = "fractals", activefill = "#4a64e8")
        self.main_cnv.create_text(500,380, text = "Calligraphy Art", font = ("Bucket O Blood",60), fill = "#770dba", tag = "calligraphy", activefill = "#9151ba")
        self.main_cnv.tag_bind("fractals", '<ButtonRelease-1>', lambda e: self.openL())                            
        self.main_cnv.tag_bind("calligraphy", '<ButtonRelease-1>', lambda e: self.openC())                                  
                                  
        self.calligraphy_window = False                                                 
        self.root.mainloop()
        

    #open the fractals window
    def openL(self):
        self.L_window = frac.FractalsArt(self, self.bg, self.font)

    #open the calligraphy window
    def openC(self):
        self.C_window = cal.CalligraphyArt(self, self.bg, self.font)
        self.calligraphy_window= True        
    


application = Main()


