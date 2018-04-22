from Tkinter import*
import ttk
import turtle
import tkcolorpicker 
import tkMessageBox as messagebox
import re
import L_system as L

#####custom fractals interface############


class customFractals:
    def __init__(self, parent, previous,bg, font):
        self.parent = parent
        self.bg = bg
        self.font =font

        
        self.wnd = Toplevel()
        self.wnd.geometry('1000x600')        
        self.wnd.title("Pre-define Fractals")
        self.wnd.resizable(False,False)
        self.wnd.configure(background='#888888')
        previous.destroy()
        
        self.kochsquarePic = PhotoImage(file="resources\kochsquare_resized.gif")
        
        self.kochsquareButton = Button(self.wnd,font=font, width = 27, height = 8, bg = self.bg, text = "Koch Square",command = L.koch_square) 
        self.kochsquareButton.grid(row=0, column=0)
        
        self.binarytreeButton = Button(self.wnd,font=font, width = 27, height = 8, bg = self.bg, text = "Binary Tree",command = L.binary_tree) 
        self.binarytreeButton.grid(row=0, column=1)  

        self.cantorButton = Button(self.wnd, font=font, width = 27, height = 8,bg = self.bg, text = "Cantor",command = L.cantor) 
        self.cantorButton.grid(row=0, column=2)   


        self.sierpinskiButton = Button(self.wnd,font=font, width = 27, height = 8, bg = self.bg, text = "Sierpinski",command = L.Sierpinski) 
        self.sierpinskiButton.grid(row=0, column=3)   
        
        self.plantButton = Button(self.wnd, font=font, width = 27, height = 8,bg = self.bg, text = "Plant",command = L.plant) 
        self.plantButton.grid(row=1,column=0)   
        
        self.snowflakeButton = Button(self.wnd,font=font, width = 27, height = 8, bg = self.bg, text = "Snow Flake",command = L.snowflake) 
        self.snowflakeButton.grid(row=1,column=1)          
                      
        self.Levy_CButton = Button(self.wnd, font=font, width = 27, height = 8,bg = self.bg, text = "Levy_c",command = L.Levy_C) 
        self.Levy_CButton.grid(row=1,column=2)  
        
        self.hilbertButton = Button(self.wnd,font=font, width = 27, height = 8, bg = self.bg, text = "Hilbert",command = L.Hilbert) 
        self.hilbertButton.grid(row=1, column=3)          
            
        self.customButton = Button(self.wnd,font=font, width = 27, height = 8, bg = self.bg, text = "Custom",command = L.custom) 
        self.customButton.grid(row=2, column=0)          
