from Tkinter import*
import ttk
import turtle
import tkcolorpicker 
import tkMessageBox as messagebox
import re
import customFractals as custom

##############Fractals Window#################

class FractalsArt:
    #initialize class attributes
    def __init__(self, parent,bg, font):
        self.parent = parent
        self.bg = bg
        self.font =font
        self.chosen_color = 'black'
        self.chosen_color_bool = False
        
        #open new window
        self.wnd = Toplevel()
        self.wnd.geometry('1000x600')        
        self.wnd.title("Fractals Art")
        self.wnd.resizable(False,False)
        self.wnd.configure(background='#e9e9e9')


        ###########user guide frame################
        self.separator_f1 = Frame(self.wnd, height=30, bg = self.bg).grid()
        self.docText = Text(self.wnd, bg='white')
        self.docText.grid(column=4,row=1,rowspan=25, padx=10)
        self.insertDoc()


        ###########fractals options##########
        self.generations_label = Label(self.wnd, text = "Number of generations:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=10)
        self.generations_label.grid(row=1)

        self.slider = Scale(self.wnd, from_=1, to=20, orient=HORIZONTAL)
        self.slider.grid(row=2)
        

        self.size_label = Label(self.wnd, text = "Size:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=10)
        self.size_label.grid(row=3)

        self.size_entry = Entry(self.wnd)
        self.size_entry.grid(row=4)

        self.color_label = Label(self.wnd, text= "Color:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=10)
        self.color_label.grid(column=1,row=1)  
        self.color_photo = PhotoImage(file="resources\img_colormap.gif")
        self.color_button = Button(self.wnd, padx=10, image=self.color_photo, width="10",height="10", command = self.color).grid(column=1,row=2)       
        
                
        self.axioms_label = Label(self.wnd, text= "Axioms:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3) 
        self.axioms_label.grid(row=5)
        self.axioms_entry = Entry(self.wnd)
        self.axioms_entry.grid(row=6)                                  
        
        self.v1_label = Label(self.wnd, text= "F:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3)   
        self.v1_label.grid(row=7,sticky=W)  
        self.v1_entry = Entry(self.wnd)
        self.v1_entry.grid(row=7)
        self.v2_label = Label(self.wnd, text= "G:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3)   
        self.v2_label.grid(row=8,sticky=W)        
        self.v2_entry = Entry(self.wnd)
        self.v2_entry.grid(row=8)              
        
        self.v3_label = Label(self.wnd, text= "X:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3)   
        self.v3_label.grid(row=9,sticky=W)  
        self.v3_entry = Entry(self.wnd)
        self.v3_entry.grid(row=9)
        
        self.v4_label = Label(self.wnd, text= "Y:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3)   
        self.v4_label.grid(row=10,sticky=W) 
        self.v4_entry = Entry(self.wnd)
        self.v4_entry.grid(row=10)
        
        self.v5_label = Label(self.wnd, text= "A:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3)   
        self.v5_label.grid(row=11,sticky=W) 
        self.v5_entry = Entry(self.wnd)
        self.v5_entry.grid(row=11)        
        
        self.v6_label = Label(self.wnd, text= "B:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3)   
        self.v6_label.grid(row=12,sticky=W)  
        self.v6_entry = Entry(self.wnd)
        self.v6_entry.grid(row=12)
                
        self.rangle_label = Label(self.wnd, text= "Right Angle:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3) 
        self.rangle_label.grid(row=3,column=1)
        self.rangle_entry = Entry(self.wnd)
        self.rangle_entry.grid(row=4, column=1)   
        
        self.langle_label = Label(self.wnd, text= "Left Angle:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3) 
        self.langle_label.grid(row=5, column=1)
        self.langle_entry = Entry(self.wnd)
        self.langle_entry.grid(row=6, column=1) 
        
        self.colorbool_label = Label(self.wnd, text= "Change Color:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3) 
        self.colorbool_label.grid(row=7, column=1)
        self.var = IntVar()

        self.c = Checkbutton(self.wnd, variable=self.var, bg =  self.bg)
        self.c.grid(row=8, column=1)    
           
        
        self.initpos_label = Label(self.wnd, text= "Initial Position:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3) 
        self.initpos_label.grid(row=9,column=1)
        self.initpos_entry = Entry(self.wnd)
        self.initpos_entry.grid(row=10, column=1)
        
        self.initangle_label = Label(self.wnd, text= "Initial Angle:", font=("Helvetica", 12), fg = 'black', bg= self.bg, padx=3) 
        self.initangle_label.grid(row=11,column=1)
        self.initangle_entry = Entry(self.wnd)
        self.initangle_entry.grid(row=12, column=1)       
        
        #####################################################################################
        
        ############Action buttons
        self.generate_button = Button(self.wnd, text = "generate",font=("Helvetica", 12), bg = self.bg, command=self.generate).grid(row=24,column=0, pady=7)
        self.custom_button = Button(self.wnd, text = "pre-defined",font=("Helvetica", 12), bg = self.bg, command=self.custom).grid(row=24,column=1, pady=7)
        
        
    ################Color picker#################
    def color(self):
        style = ttk.Style(self.wnd)
        style.theme_use('clam')

        self.chosen_color=tkcolorpicker.askcolor((255, 255, 0), self.wnd)
        self.chosen_color_bool = True
        
    
###################Generate button callback##############    
    def generate(self):
        
        axioms = self.axioms_entry.get()
        #make sure axioms are valid
        if self.axiomsCheck(axioms)==False:
            return
        
        #create dictionary for rules
        rules = {}
        rules["F"] = self.v1_entry.get()
        
        rules["G"] = self.v2_entry.get()
        rules["X"] = self.v3_entry.get()
        rules["Y"] = self.v4_entry.get()
        rules["A"] = self.v5_entry.get()
        rules["B"] = self.v6_entry.get()
        print rules
        if self.rulesCheck(rules, axioms)==False:
            return        
        generation = self.slider.get()
        
        size= self.size_entry.get()
        if self.sizeCheck1(size)==False:
            return 
        
        size = eval(size)
        if self.sizeCheck2(size)==False:
            return
                
        rangle= self.rangle_entry.get()
        langle= self.langle_entry.get()
        
        if self.rangleCheck1(rangle)==False:
            return
        if self.langleCheck1(langle)==False:
            return
        
        rangle = eval(rangle)
        langle = eval(langle)
        
        if self.rangleCheck2(rangle)==False:
            return
        if self.langleCheck2(langle)==False:
            return        
        
        
        if self.var == 0:
            colorbool = False
        else:
            colorbool=True
        
       
                                     

        initpos = self.initpos_entry.get()
        if self.initposCheck1(initpos)==False:
            return
        
        initpos = eval(initpos)
        
        initangle= self.initangle_entry.get()
        if self.initangleCheck1(initangle)==False:
            return
        initangle = eval(initangle)
        if self.initangleCheck2(initangle)==False:
            return
        if self.chosen_color_bool==True:
            color=self.chosen_color[1]
        else:
            color = self.chosen_color
        
        
        
        input_list = [initpos[0],initpos[1],initangle,color]

        import L_system  
        L_system.draw(axioms, rules, generation,size, rangle, langle, colorbool, input_list)
        return
    
    
    ########checks if axioms are valid
    def axiomsCheck(self, axioms):
        allowedVars = ["A","B","X","Y","F","G"]
        additionalVars = allowedVars + ["-","+","[","]"]
        if len(axioms)<1:
            messagebox.showerror("Error", "Invalid axioms, for more help refer to the user guide")
            return False
        for letter in axioms:
            if letter not in additionalVars:
                messagebox.showerror("Error", "Invalid axioms, for more help refer to the user guide")
                return False
        return True

    #######checks if rules are valid
    def rulesCheck(self, rules, axioms):
        allowedVars = ["A","B","X","Y","F","G"]
        additionalVars = allowedVars + ["-","+","[","]"] 
        usedVars = list(axioms)
        print usedVars
        for key in rules:
            value = rules[key]                  
            for letter in value:
                usedVars+=[letter]
        for key in rules:
            value= rules[key]
            if key in usedVars:
                if len(value)<1:
                    messagebox.showerror("Error", "Invalid rules, for more help refer to the user guide")
                    return False  
            for letter in value:
                if letter not in additionalVars:
                    messagebox.showerror("Error", "Invalid rules, for more help refer to the user guide")
                    return False                      
        return True
    
    def rangleCheck1(self, rangle):
        pattern = "\d+"
        if re.search(pattern, rangle)==None:
            messagebox.showerror("Error", "Invalid right angle, for more help refer to the user guide")            
            return False                
        return True
    
    
    #####checks if left angle is an int
    def langleCheck1(self, langle):
        pattern = "\d+"
        if re.search(pattern, langle)==None:
            messagebox.showerror("Error", "Invalid left angle, for more help refer to the user guide")            
            return False                
        return True  

    #####checks if right angle is an int
    def rangleCheck2(self, rangle):
        if rangle<0 or rangle>360:
            messagebox.showerror("Error", "Invalid left angle, for more help refer to the user guide")
            return False
        return True
    
    ####checks if left and right angles are valid ints
    def langleCheck2(self,langle):
        if langle<0 or langle>360:
            messagebox.showerror("Error", "Invalid left angle, for more help refer to the user guide")
            return False
        return True
    
    ####checks if initial pos is an int tuple    
    def initposCheck1(self, initpos):
        pattern = "\[-*\d+,-*\d+\]"
        if re.search(pattern, initpos)==None:
            messagebox.showerror("Error", "Invalid initial position, for more help refer to the user guide")        
            return False
        return True
    
    #####checks if initangle is an int
    def initangleCheck1(self, initangle):
        pattern = "\d+"
        if re.search(pattern, initangle)==None:
            messagebox.showerror("Error", "Invalid initial angle, for more help refer to the user guide")            
            return False                
        return True     
        
    #####checks if intiangle is a valid int   
    def initangleCheck2(self, initangle):
        if initangle<0 or initangle>360:
            messagebox.showerror("Error", "Invalid initial angle, for more help refer to the user guide")
            return False
        return True
    
    #####checks if size is an int
    def sizeCheck1(self, size):
        if re.search("\d+", size)==None:
            messagebox.showerror("Error", "Invalid size, for more help refer to the user guide")
            return False
        return True
  
    #####checks if size is a valid int
    def sizeCheck2(self,size):
        if size<0 or size>100:
            messagebox.showerror("Error","Invalid size, for more help refer to the user guide")
            return False
        return True
    
    ######browse user guide from text file
    def insertDoc(self):
        f = open("user_guide.txt")
        self.docText.tag_config("t1", underline=1, lmargin1=1, justify=CENTER, foreground="black", font=("Helvetica",20))
        self.docText.tag_config("t2", underline=1, justify=LEFT, lmargin1=1, foreground="black",font=("Helvetica",14))
        self.docText.tag_config("t3", justify=LEFT, lmargin1=1, foreground="black",font=("Helvetica",10))
        self.docText.insert(END, f.readline(),"t1")        
        self.docText.insert(END, f.readline(),"t2")
        self.docText.insert(END, f.readline(),"t3")
        self.docText.insert(END, f.readline(),"t3")
        self.docText.insert(END, f.readline(),"t2") 
        for i in range(6):
            self.docText.insert(END, f.readline(),"t3")        
        self.docText.insert(END, f.readline(),"t2")
        self.docText.insert(END, f.readline(),"t3")  
        self.docText.configure(state=DISABLED)
        
       
    def custom(self):
        self.custom_window = custom.customFractals(self.parent, self.wnd, self.bg, self.font)
        

        
        
    
        
        

        

##        self.t = turtle.RawTurtle()


        

##        self.f_2 = Frame(self.wnd).grid(row=0, column=1)


        
