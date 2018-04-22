from Tkinter import*
import ttk
import turtle
from tkcolorpicker import askcolor
import tkMessageBox as messagebox
import re
import customFractals as custom
import letters_dictionary as LD
import letters_draw as L

##############Fractals Window#################

class CalligraphyArt:
    def __init__(self, parent,bg, font):
        self.parent = parent
        self.bg = bg
        self.font =font
        
        self.wnd = Toplevel()
        self.wnd.geometry('1000x700')        
        self.wnd.title("Calligraphy Art")
        self.wnd.resizable(False,False)
        self.wnd.configure(background=self.bg)


        self.canvas_frame = Frame(self.wnd, width=700,height=700,bg=self.bg)
        self.canvas_frame.grid(row=0,column=0, padx=5,pady=5)
        self.main_cnv = Canvas(self.canvas_frame,width=700,height=700, bg="white")
        self.main_cnv.pack()
        
        self.right_frame = Frame(self.wnd, bg = self.bg)
        self.right_frame.grid(row=0, column=1, sticky=N)
        
        self.bg_label = Label(self.right_frame, bg=self.bg, text = "Background:",font=("Helvetica",10)) 
        self.bg_label.grid(row=0,column=0,sticky=N, padx=2,pady=3)
        
        self.color_photo = PhotoImage(file="resources\img_colormap.gif")
        self.bg_button = Button(self.right_frame, padx=10, image=self.color_photo, width="10",height="10", command = self.bg_com)   
        self.bg_button.grid(row=0,column=1, sticky=N,padx=2,pady=3)
        
        self.fg_label = Label(self.right_frame, bg=self.bg, text = "Foreground:",font=("Helvetica",10)) 
        self.fg_label.grid(row=0,column=2,sticky=N, padx=4,pady=3)
        
        self.fg_button = Button(self.right_frame, padx=10, image=self.color_photo, width="10",height="10", command = self.fg_com)   
        self.fg_button.grid(row=0,column=3, sticky=N,pady=3)        
        
        
        self.letters_label = Label(self.right_frame, bg=self.bg, text="Letters:" , font = ("Helvetica",10))
        self.letters_label.grid(row=1,column=0,padx=2,pady=3,sticky=N+W)
        self.text_entry = Entry(self.right_frame,width=15, bg="white")
        self.text_entry.grid(row=2,column=0, columnspan=2, padx=2,pady=3,sticky=S+W)
        self.info_button = PhotoImage(file="resources/info.gif")
        self.letters_info = Button(self.right_frame,image = self.info_button, width=10,height=10, command = self.open_dict )
        self.letters_info.grid(row=1,column=1,padx=2,pady=3,sticky=N+W)
        
        
        self.size_label = Label(self.right_frame, text = "Size:", bg=self.bg, font=("Helvetica",10))
        self.size_label.grid(row=1,column=2,padx=2,pady=3,sticky=N+W)
        self.size_scale = Scale(self.right_frame, from_=1, to_=15, orient= HORIZONTAL)
        self.size_scale.grid(row=2,column=2,padx=2,pady=3, sticky=N+W)
        
        
        self.angle_label = Label(self.right_frame, text="Initial Angle:", bg=self.bg, font=("Helvetica",10))
        self.angle_label.grid(row=3,column=0,padx=2,pady=3,sticky=N+W)
        self.angle_scale = Scale(self.right_frame, from_=0, to_=359, width=15, orient= HORIZONTAL)
        self.angle_scale.grid(row=4,column=0,padx=2,pady=3, sticky=N+W)
        
        self.regulator_label = Label(self.right_frame, text = "Regulator:", bg = self.bg, font =("Helvetica",10),width=15)
        self.regulator_label.grid(row=3, column =2, padx=2, pady=3, sticky = N+W)
        self.regulator_list = Listbox(self.right_frame, width =10)
        self.regulator_list.insert(END, "translation")
        self.regulator_list.insert(END, "rotation")
        self.regulator_list.insert(END,"None")
        self.regulator_list.grid(row=4, column =2, padx=2, pady=3, rowspan =3)
        
        self.repitions_label = Label(self.right_frame, text = "Number of repitions:", bg = self.bg, font =("Helvetica",10))
        self.repitions_label.grid(row=5, column = 0, padx = 2, pady=3, sticky = N+W)
        self.repitions_scale = Scale(self.right_frame, from_=1, to_=8, orient = HORIZONTAL)
        self.repitions_scale.grid(row =6, column =0 , padx =2 , pady = 3, sticky = N+W)
        
#        self.initial_pos_label = Label(self.right_frame, text = "Initial position:", bg = self.bg, font =("Helvetica",10))
#        self.initial_pos_label.grid(row=7, column = 0, padx = 2, pady=3, sticky = N+W)
#        self.initial_pos_widget = Canvas(self.right_frame, width = 50, height = 50)
#        self.initial_pos_widget.grid(row=8, column = 0, padx = 2, pady = 3, sticky=N+W)
#        self.initial_pos_widget.create_oval(0,0, 50,50, outline="black", tag = "pos", fill=self.bg)
#        self.initial_pos_widget.create_line(25,0,25,50,fill="black")
#        self.initial_pos_widget.create_line(0,25,50,25,fill="black")
#        self.initial_pos_widget.tag_bind("pos", '<Button 1>', self.set_pos)
#        print self.initial_pos_widget.x
        
        
        
        
        
        self.Ctext = []
        self.Csize = 1
        self.Ccolor = ""
        self.Cbg = ""
        self.fg_color = '#000000'
        self.bg_color = '#FFFFFF'
        self.regulator = self.regulator_list.get(ACTIVE)
        self.reps = self.repitions_scale.get()
        self.pos = None
        
        self.draw_wnd = None    
        self.wnd.after(0,self.draw)                

        
#    def set_pos(self, event):
#        print event.x
#        print event.y
#        self.pos = [0,0]
#        self.pos[0] = 8 * (event.x - 25)
#        self.pos[1] = 8 * (event.y - 25)
        
         
    def bg_com(self):
        style = ttk.Style(self.wnd)
        style.theme_use('clam')

        self.bg_color=askcolor((255, 255, 0), self.wnd)
        self.bg_color = self.bg_color[1]
        self.main_cnv.config(bg = self.bg_color)
        return self.bg_color
        
    def fg_com(self):
        style = ttk.Style(self.wnd)
        style.theme_use('clam')

        self.fg_color =askcolor((255, 255, 0), self.wnd)
        self.fg_color = self.fg_color[1]
        
        

    def open_dict(self):
        dictionary = LD.dictionary(self)
        
    def draw(self):
        
        text = self.text_entry.get()
        
        
        text = text.split()
        Ctext = text
        Csize = self.size_scale.get()
        Ccolor = self.fg_color
        Cbg = self.bg_color
        Cangle = self.angle_scale.get()
        valid = False
        pattern = "^\d+$"

        self.wnd.after(5,self.draw)            

        self.Ctext = Ctext
        self.Csize = Csize
        self.Ccolor = Ccolor
        self.Cbg = Cbg
        self.Cangle = Cangle
        self.reps = self.repitions_scale.get()
        self.regulator = self.regulator_list.get(ACTIVE)        
        if self.draw_wnd == None:
            if len(self.Ctext)>0:
                self.draw_wnd = L.Draw(self,self.Ctext, self.Ccolor, self.Cbg, self.Csize, self.parent, self.main_cnv, self.Cangle, self.regulator, self.reps)
        else:
            self.draw_wnd.update_cnv(self, self.Ctext, self.Ccolor, self.Cbg, self.Csize, self.Cangle, self.main_cnv, self.regulator, self.reps)
        
        return            
        


        