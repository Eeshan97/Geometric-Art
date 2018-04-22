from Tkinter import*
import ttk



class dictionary:
    def __init__(self, parent):
        self.parent=parent
        self.wnd = Toplevel()
        self.title_frame = Frame(self.wnd)
        self.title_frame.grid(row=0,column=0)
        self.wnd.geometry('600x500')        
        self.wnd.title("Letters Dictionaryy")
        self.wnd.resizable(False,False)
        self.wnd.config(bg = 'white')
        
        self.letters_frame = Frame(self.wnd, bg = 'white')
        self.letters_frame.grid(row=1,column=0, sticky=N+W)
        self.top_label = Label(self.title_frame,font = ("Helvetica", 25), text = "Click on the letters you'd like to choose", bg = "white")
        self.top_label.grid(row=0, column=0)
        
        self.a = PhotoImage(file="resources\\a.gif")
        self.a_button = Button(self.letters_frame, image = self.a, width="50",height="50", relief = FLAT, command = lambda: self.draw("a"))
        self.a_button.grid(row=0,column=1, sticky = N+W)
        self.a_label = Label(self.letters_frame, bg = 'white', text= "a", font=("Helvetica",30, "bold")).grid(row=0,column=0, sticky=N+W, padx=5)
        
        self.b = PhotoImage(file="resources\\b.gif")
        self.b_button = Button(self.letters_frame, image = self.b, width="50",height="50", relief = FLAT, command = lambda: self.draw("b"))
        self.b_button.grid(row=1,column=1, sticky = N+W)
        self.b_label = Label(self.letters_frame, bg = 'white', text= "b", font=("Helvetica",30, "bold")).grid(row=1,column=0, sticky=N+W, padx=5)
        
        self.t = PhotoImage(file="resources\\t.gif")
        self.t_button = Button(self.letters_frame, image = self.t, width="50",height="50", relief = FLAT, command = lambda: self.draw("t"))
        self.t_button.grid(row=2,column=1, sticky = N+W)
        self.t_label = Label(self.letters_frame, bg = 'white', text= "t", font=("Helvetica",30, "bold")).grid(row=2,column=0, sticky=N+W, padx=5)
        
        self.th = PhotoImage(file="resources\\th.gif")
        self.th_button = Button(self.letters_frame, image = self.th, width="50",height="50", relief = FLAT, command = lambda: self.draw("th"))
        self.th_button.grid(row=3,column=1, sticky = N+W)
        self.th_label = Label(self.letters_frame, bg = 'white', text= "th", font=("Helvetica",30, "bold")).grid(row=3,column=0, sticky=N+W, padx=5)
        
        self.j = PhotoImage(file="resources\\j.gif")
        self.j_button = Button(self.letters_frame, image = self.j, width="50",height="50", relief = FLAT, command = lambda: self.draw("j"))
        self.j_button.grid(row=4,column=1, sticky = N+W)
        self.j_label = Label(self.letters_frame, bg = 'white', text= "j", font=("Helvetica",30, "bold")).grid(row=4,column=0, sticky=N+W, padx=5)


        self.h = PhotoImage(file="resources\\h.gif")
        self.h_button = Button(self.letters_frame, image = self.h, width="50",height="50", relief = FLAT, command = lambda: self.draw("h"))
        self.h_button.grid(row=5,column=1, sticky = N+W)
        self.h_label = Label(self.letters_frame, bg = 'white', text= "h", font=("Helvetica",30, "bold")).grid(row=5,column=0, sticky=N+W, padx=5)

        self.kh = PhotoImage(file="resources\\kh.gif")
        self.kh_button = Button(self.letters_frame, image = self.kh, width="50",height="50", relief = FLAT, command = lambda: self.draw("kh"))
        self.kh_button.grid(row=6,column=1, sticky = N+W)
        self.kh_label = Label(self.letters_frame, bg = 'white', text= "kh", font=("Helvetica",30, "bold")).grid(row=6,column=0, sticky=N+W, padx=5)
        
        ttk.Separator(self.letters_frame,orient=VERTICAL).grid(row=0,column=2, sticky=N+S, padx=15, pady=2, rowspan=7 )

        self.d = PhotoImage(file="resources\\d.gif")
        self.d_button = Button(self.letters_frame, image = self.d, width="50",height="50", relief = FLAT, command = lambda: self.draw("d"))
        self.d_button.grid(row=0,column=4, sticky = N+W)
        self.d_label = Label(self.letters_frame, bg = 'white', text= "d", font=("Helvetica",30, "bold")).grid(row=0,column=3, sticky=N+W, padx=5)

        self.dh = PhotoImage(file="resources\\dh.gif")
        self.dh_button = Button(self.letters_frame, image = self.dh, width="50",height="50", relief = FLAT, command = lambda: self.draw("dh"))
        self.dh_button.grid(row=1,column=4, sticky = N+W)
        self.dh_label = Label(self.letters_frame, bg = 'white', text= "dh", font=("Helvetica",30, "bold")).grid(row=1,column=3, sticky=N+W, padx=5)

        self.r = PhotoImage(file="resources\\r.gif")
        self.r_button = Button(self.letters_frame, image = self.r, width="50",height="50", relief = FLAT, command = lambda: self.draw("r"))
        self.r_button.grid(row=2,column=4, sticky = N+W)
        self.r_label = Label(self.letters_frame, bg = 'white', text= "r", font=("Helvetica",30, "bold")).grid(row=2,column=3, sticky=N+W, padx=5)

        self.z = PhotoImage(file="resources\\z.gif")
        self.z_button = Button(self.letters_frame, image = self.z, width="50",height="50", relief = FLAT, command = lambda: self.draw("z"))
        self.z_button.grid(row=3,column=4, sticky = N+W)
        self.z_label = Label(self.letters_frame, bg = 'white', text= "z", font=("Helvetica",30, "bold")).grid(row=3,column=3, sticky=N+W, padx=5)
        
        self.s = PhotoImage(file="resources\\s.gif")
        self.s_button = Button(self.letters_frame, image = self.s, width="50",height="50", relief = FLAT, command = lambda: self.draw("s"))
        self.s_button.grid(row=4,column=4, sticky = N+W)
        self.s_label = Label(self.letters_frame, bg = 'white', text= "s", font=("Helvetica",30, "bold")).grid(row=4,column=3, sticky=N+W, padx=5)
        
        self.sh = PhotoImage(file="resources\\sh.gif")
        self.sh_button = Button(self.letters_frame, image = self.sh, width="50",height="50", relief = FLAT, command = lambda: self.draw("sh"))
        self.sh_button.grid(row=5,column=4, sticky = N+W)
        self.sh_label = Label(self.letters_frame, bg = 'white', text= "sh", font=("Helvetica",30, "bold")).grid(row=5,column=3, sticky=N+W, padx=5)
        
        self.sad = PhotoImage(file="resources\\sad.gif")
        self.sad_button = Button(self.letters_frame, image = self.sad, width="50",height="50", relief = FLAT, command = lambda: self.draw("S"))
        self.sad_button.grid(row=6,column=4, sticky = N+W)
        self.sad_label = Label(self.letters_frame, bg = 'white', text= "S", font=("Helvetica",30, "bold")).grid(row=6,column=3, sticky=N+W, padx=5)

        ttk.Separator(self.letters_frame,orient=VERTICAL).grid(row=0,column=5, sticky=N+S, padx=15, pady=2, rowspan=7 )

        self.dad = PhotoImage(file="resources\\dad.gif")
        self.dad_button = Button(self.letters_frame, image = self.dad, width="50",height="50", relief = FLAT, command = lambda: self.draw("D"))
        self.dad_button.grid(row=0,column=7, sticky = N+W)
        self.dad_label = Label(self.letters_frame, bg = 'white', text= "D", font=("Helvetica",30, "bold")).grid(row=0,column=6, sticky=N+W, padx=5)
        
        self.tah = PhotoImage(file="resources\\tah.gif")
        self.tah_button = Button(self.letters_frame, image = self.tah, width="50",height="50", relief = FLAT, command = lambda: self.draw("T"))
        self.tah_button.grid(row=1,column=7, sticky = N+W)
        self.tah_label = Label(self.letters_frame, bg = 'white', text= "T", font=("Helvetica",30, "bold")).grid(row=1,column=6, sticky=N+W, padx=5)

        self.dha = PhotoImage(file="resources\\dha.gif")
        self.dha_button = Button(self.letters_frame, image = self.dha, width="50",height="50", relief = FLAT, command = lambda: self.draw("DH"))
        self.dha_button.grid(row=2,column=7, sticky = N+W)
        self.dha_label = Label(self.letters_frame, bg = 'white', text= "DH", font=("Helvetica",30, "bold")).grid(row=2,column=6, sticky=N+W, padx=5)
        
        self.ein = PhotoImage(file="resources\\3.gif")
        self.ein_button = Button(self.letters_frame, image = self.ein, width="50",height="50", relief = FLAT, command = lambda: self.draw("3"))
        self.ein_button.grid(row=3,column=7, sticky = N+W)
        self.ein_label = Label(self.letters_frame, bg = 'white', text= "3", font=("Helvetica",30, "bold")).grid(row=3,column=6, sticky=N+W, padx=5)
        
        self.gh = PhotoImage(file="resources\\gh.gif")
        self.gh_button = Button(self.letters_frame, image = self.gh, width="50",height="50", relief = FLAT, command = lambda: self.draw("gh"))
        self.gh_button.grid(row=4,column=7, sticky = N+W)
        self.gh_label = Label(self.letters_frame, bg = 'white', text= "gh", font=("Helvetica",30, "bold")).grid(row=4,column=6, sticky=N+W, padx=5)
        
        self.f = PhotoImage(file="resources\\f.gif")
        self.f_button = Button(self.letters_frame, image = self.f, width="50",height="50", relief = FLAT, command = lambda: self.draw("f"))
        self.f_button.grid(row=5,column=7, sticky = N+W)
        self.f_label = Label(self.letters_frame, bg = 'white', text= "f", font=("Helvetica",30, "bold")).grid(row=5,column=6, sticky=N+W, padx=5)
        
        self.q = PhotoImage(file="resources\\q.gif")
        self.q_button = Button(self.letters_frame, image = self.q, width="50",height="50", relief = FLAT, command = lambda: self.draw("q"))
        self.q_button.grid(row=6,column=7, sticky = N+W)
        self.q_label = Label(self.letters_frame, bg = 'white', text= "q", font=("Helvetica",30, "bold")).grid(row=6,column=6, sticky=N+W, padx=5)
        
        
        ttk.Separator(self.letters_frame,orient=VERTICAL).grid(row=0,column=8, sticky=N+S, padx=15, pady=2, rowspan=7 )
        
        self.k = PhotoImage(file="resources\\k.gif")
        self.k_button = Button(self.letters_frame, image = self.k, width="50",height="50", relief = FLAT, command = lambda: self.draw("k"))
        self.k_button.grid(row=0,column=10, sticky = N+W)
        self.k_label = Label(self.letters_frame, bg = 'white', text= "k", font=("Helvetica",30, "bold")).grid(row=0,column=9, sticky=N+W, padx=5)
        
        self.l = PhotoImage(file="resources\\l.gif")
        self.l_button = Button(self.letters_frame, image = self.l, width="50",height="50", relief = FLAT, command = lambda: self.draw("l"))
        self.l_button.grid(row=1,column=10, sticky = N+W)
        self.l_label = Label(self.letters_frame, bg = 'white', text= "l", font=("Helvetica",30, "bold")).grid(row=1,column=9, sticky=N+W, padx=5)

        self.m = PhotoImage(file="resources\\m.gif")
        self.m_button = Button(self.letters_frame, image = self.m, width="50",height="50", relief = FLAT, command = lambda: self.draw("m"))
        self.m_button.grid(row=2,column=10, sticky = N+W)
        self.m_label = Label(self.letters_frame, bg = 'white', text= "m", font=("Helvetica",30, "bold")).grid(row=2,column=9, sticky=N+W, padx=5)

        self.n = PhotoImage(file="resources\\n.gif")
        self.n_button = Button(self.letters_frame, image = self.n, width="50",height="50", relief = FLAT, command = lambda: self.draw("n"))
        self.n_button.grid(row=3,column=10, sticky = N+W)
        self.n_label = Label(self.letters_frame, bg = 'white', text= "n", font=("Helvetica",30, "bold")).grid(row=3,column=9, sticky=N+W, padx=5)

        self.ha = PhotoImage(file="resources\\ha.gif")
        self.ha_button = Button(self.letters_frame, image = self.ha, width="50",height="50", relief = FLAT, command = lambda: self.draw("H"))
        self.ha_button.grid(row=4,column=10, sticky = N+W)
        self.ha_label = Label(self.letters_frame, bg = 'white', text= "H", font=("Helvetica",30, "bold")).grid(row=4,column=9, sticky=N+W, padx=5)

        self.w = PhotoImage(file="resources\\w.gif")
        self.w_button = Button(self.letters_frame, image = self.w, width="50",height="50", relief = FLAT, command = lambda: self.draw("w"))
        self.w_button.grid(row=5,column=10, sticky = N+W)
        self.w_label = Label(self.letters_frame, bg = 'white', text= "w", font=("Helvetica",30, "bold")).grid(row=5,column=9, sticky=N+W, padx=5)

        self.y = PhotoImage(file="resources\\y.gif")
        self.y_button = Button(self.letters_frame, image = self.y, width="50",height="50", relief = FLAT, command = lambda: self.draw("y"))
        self.y_button.grid(row=6,column=10, sticky = N+W)
        self.y_label = Label(self.letters_frame, bg = 'white', text= "y", font=("Helvetica",30, "bold")).grid(row=6,column=9, sticky=N+W, padx=5)

    def draw(self, letter):
        if self.parent.text_entry.get()!="":
            self.parent.text_entry.insert(END," ")    
        self.parent.text_entry.insert(END,letter)    

        
        
        
        
        
        
        
        
        
        
        
        
        #    def b_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"b")    
#    def t_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")            
#        self.parent.text_entry.insert(END,"t")    
#    def th_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"th")    
#    def j_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"j")    
#    def h_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"h")    
#    def kh_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"kh")    
#    def d_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"d")    
#    def dh_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"dh")    
#    def r_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"r")    
#    def z_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"z")    
#    def s_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"s")    
#    def sh_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"sh")    
#    def S_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"S")    
#    def D_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"D")    
#    def T_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"T")    
#    def DH_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"DH")    
#    def ein_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"3")    
#    def gh_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"gh")    
#    def f_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"f")    
#    def q_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"q")    
#    def k_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"k")    
#    def l_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"l")    
#    def m_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"m")    
#    def n_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"n")    
#    def H_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"H")    
#    def w_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"w")    
#    def y_command(self):
#        if self.parent.text_entry.get()!="":
#            self.parent.text_entry.insert(END," ")    
#        self.parent.text_entry.insert(END,"y")    