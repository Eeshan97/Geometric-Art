from Tkinter import*

from PIL import ImageTk as imgtk
from PIL import Image, ImageDraw
import math
import Segmentation as seg


class Draw:
    def __init__(self,parent, letters, color, bg, size, root, canvas, angle , regulator, reps):
        if len(letters) == 0:
            return
        self.root = root
        self.parent = parent
        self.letters = letters
        self.canvas = canvas
        self.angle = angle
        self.regulator = regulator
        self.reps = reps

        self.color = color
        self.bg = bg
        self.size = size

        self.width=0
        self.height = 0
        self.init_x = self.determine_initial_pos()
        self.init_y = 370
        self.current_x = self.init_x
        self.last = False
        self.canvas.delete("ALL")

        count = 0
        if bg == color:
            return
        for i in range(len(letters)):
            self.draw_letter(letters[i],i, letters, count)
            count+=1

#        if rotate!= 0:
        if len(letters)>0:
            self.canvas.addtag_all("ALL")
            self.adjust_size(size)
            self.draw_image(self.angle)
            self.adjust_canvas()
            if regulator == "translation":
                self.translate(self.angle)
                self.adjust_canvas(True)
            if regulator == "rotation":
                self.rotate(self.angle)
                self.adjust_canvas(True)

#                if regulator == "glide":
#                    self.glide()

    def determine_initial_pos(self):
        x = 350
        for i in range(len(self.letters)-1):
            x+= 30
        return x


    def draw_letter(self, letter, i, letters, count):
#        self.image = Image.new("RGB",(700, 700), "white")
#        self.draw = ImageDraw.Draw(self.image)
#        self. draw.pieslice([0,0,50,50],start=0,end=360,fill=self.color, outline= self.color)

#        self.drawingList = []
        if letter == "a":
            self.draw_a(count)


        elif letter == "b" or letter=="t" or letter=="th":
            if i==0:
                self.draw_b_t_th("B",letter,count)
            elif i==len(letters)-1:
                self.draw_b_t_th("E",letter,count)
            else:
                if self.last == False:
                    self.draw_b_t_th("M",letter,count)
                else:
                    self.draw_b_t_th("B",letter,count)

        elif letter == "j" or letter == "h" or letter == "kh":
            if i==len(letters) -1:
                self.draw_j_h_kh("E", letter,count)
            else:
                self.draw_j_h_kh("B",letter,count)

        elif letter == "d" or letter =="dh":
            self.draw_d_dh(letter,count)

        elif letter == "r" or letter == "z" or letter == "w":
            self.draw_r_z(letter,count)

        elif letter =="s" or letter == "sh":
            if i==len(letters) -1:
                self.draw_s_sh("E", letter,count)
            else:
                self.draw_s_sh("B", letter,count)

        elif letter =="S" or letter == "D":
            if i==len(letters) -1:
                self.draw_S_D("E", letter,count)
            else:
                self.draw_S_D("B", letter,count)
        elif letter =="T" or letter =="DH":
            self.draw_T_DH(letter,count)

        elif letter =="3" or letter =="gh":
            if i==len(letters) -1:
                self.draw_3_gh("E", letter,count)
            else:
                self.draw_3_gh("B",letter,count)

        elif letter =="f" or letter =="q":
            if i==len(letters) -1:
                self.draw_f_q("E", letter,count)
            else:
                self.draw_f_q("B",letter,count)

        elif letter =="k":
            if i==len(letters) -1:
                self.draw_k("E", letter,count)
            else:
                self.draw_k("B",letter,count)

        elif letter == "l":
            if i==len(letters) -1:
                self.draw_l("E", letter,count)
            else:
                self.draw_l("B",letter,count)

        elif letter == "m":
            if i==len(letters) -1:
                self.draw_m("E", letter,count)
            else:
                self.draw_m("B",letter,count)

        elif letter == "n":
            if i==0:
                self.draw_b_t_th("B",letter,count)
            elif i==len(letters)-1:
                self.draw_b_t_th("E",letter,count)
            else:
                if self.last == False:
                    self.draw_b_t_th("M",letter,count)
                else:
                    self.draw_b_t_th("B",letter,count)

        elif letter == "H":
            if i==0:
                self.draw_H("B",letter,count)
            elif i==len(letters)-1:
                self.draw_H("E",letter,count)
            else:
                if self.last == False:
                    self.draw_H("M",letter,count)
                else:
                    self.draw_H("B",letter,count)






    def draw_a(self,count):
        x= self.current_x
        y= self.init_y
        self.canvas.create_rectangle(x, y, x-17, y-60, fill=self.color, outline = self.color, tag = str(count))
        self.current_x-=22
        self.last = True

    def draw_b_t_th(self, pos,letter,count):
        x = self.current_x
        y = self.init_y
        if pos == "M":
            self.canvas.create_rectangle(x,y,x-40, y-5, fill=self.color, outline=self.color, tag = str(count))

            self.current_x-=40
            x = self.current_x
        if pos == "B":
            self.canvas.create_rectangle(x,y,x-15,y-15,fill=self.color, outline=self.color, tag = str(count))
            self.current_x-=15
            x = self.current_x
            self.canvas.create_rectangle(x,y,x-20,y-5, fill=self.color, outline=self.color, tag = str(count))

#            self.canvas.create_oval(x-5,y+5,x-25,y+25, fill=self.color, outline= self.color)
            self.current_x-=20
            x = self.current_x
        if pos == "E":
            self.canvas.create_rectangle(x,y,x-20,y-5, fill=self.color, outline = self.color, tag = str(count))

#            self.canvas.create_oval(x-5,y+5,x-25,y+25, fill=self.color, outline = self.color)
            self.current_x-=20
            x = self.current_x
            self.canvas.create_arc(x+30,y+30,x-30,y-30, start=90, extent= 90,fill=self.color, outline=self.color, tag = str(count))

            self.current_x-=30
            x= self.current_x

        if letter == "b":
            self.canvas.create_oval(x+20,y+5,x+40,y+25, fill=self.color, outline= self.color, tag = str(count))


        if letter =="t":
            self.canvas.create_oval(x+5,y-25,x+25,y-45, fill=self.color, outline= self.color, tag = str(count))


            self.canvas.create_oval(x+20,y-25,x+45,y-45, fill=self.color, outline= self.color, tag = str(count))


        if letter =="th":
            self.canvas.create_oval(x+5,y-25,x+25,y-45, fill=self.color, outline= self.color, tag = str(count))

            self.canvas.create_oval(x+20,y-25,x+40,y-45, fill=self.color, outline= self.color, tag = str(count))

            self.canvas.create_oval(x+12,y-40,x+32,y-60, fill=self.color, outline= self.color, tag = str(count))

        if letter == "n":
            self.canvas.create_oval(x+15,y-25,x+35,y-45, fill=self.color, outline= self.color, tag = str(count))

        self.last = False


    def draw_j_h_kh(self, pos, letter,count):
        x = self.current_x
        y = self.init_y
        self.canvas.create_rectangle(x,y,x-40, y-15, fill=self.color, outline=self.color, tag = str(count))


        self.canvas.create_polygon(x,y-15, x-35, y-50, x-35, y-30, x-5, y, fill=self.color, outline= self.color, tag = str(count))

        self.current_x-=35
        x = self.current_x
        if letter=="j":
            self.canvas.create_oval(x+10,y+5,x+30,y+25, fill=self.color, outline= self.color, tag = str(count))
        if letter =="kh":
            self.canvas.create_oval(x+10,y-30,x+30,y-50, fill=self.color, outline= self.color, tag = str(count))

        if pos =="E":
            self.canvas.create_arc(x-10,y-30,x+45,y+35, start=145, extent= 180,fill=self.color, outline=self.color, tag = str(count))

        self.last = False

    def draw_d_dh(self,letter,count):
        x = self.current_x - 30
        y = self.init_y
#        self.canvas.create_arc(x-25,y-20, x+30, y+20,start = 0, extent =50, fill=self.color, outline= self.color)
        self.canvas.create_arc(x-30,y+30, x+30, y-30,start = 90, extent =-90, fill=self.color, outline= self.color, tag = str(count))

        self.canvas.create_rectangle(x,y,x-10, y-30, fill = self.color, outline=self.color, tag = str(count))


        self.current_x = x-15
        if letter =="dh":
            self.canvas.create_oval(x,y-30,x+20,y-50, fill=self.color, outline= self.color, tag = str(count))

        self.last = True

    def draw_r_z(self,letter,count):
        x = self.current_x
        y = self.init_y
        self.canvas.create_polygon(x,y,x-30, y+40, x-30, y+20, x, y-20, fill=self.color, outline= self.color, tag = str(count))


        if letter == "z":
            self.canvas.create_oval(x,y-25,x-20,y-45, fill=self.color, outline= self.color, tag = str(count))
        if letter == "w":
            self.canvas.create_oval(x+5,y,x-15,y-20)
        self.last =True
        self.current_x-=35

    def draw_s_sh(self,pos, letter,count):
        x = self.current_x
        y = self.init_y
        self.canvas.create_rectangle(x,y,x-15, y-15, fill = self.color, outline=self.color, tag = str(count))


        x-=15
        self.canvas.create_rectangle(x,y,x-10, y-5, fill = self.color, outline=self.color, tag = str(count))


        x-=10
        self.canvas.create_rectangle(x,y,x-15, y-15, fill = self.color, outline=self.color, tag = str(count))


        x-=15
        self.canvas.create_rectangle(x,y,x-10, y-5, fill = self.color, outline=self.color, tag = str(count))


        x-=10
        self.canvas.create_rectangle(x,y,x-15, y-15, fill = self.color, outline=self.color, tag = str(count))


        if pos == "E":
            self.canvas.create_arc(x,y-25,x-50,y+25,start = 0, extent = -180, fill = self.color, outline = self.color, tag = str(count))

            self.current_x = x - 50
        else:
            x-=15
            self.canvas.create_rectangle(x,y,x-20, y-5, fill = self.color, outline=self.color, tag = str(count))

            x-=20
            self.current_x=x
        if letter =="sh":
            if pos == "E":
                self.canvas.create_oval(x+5,y-25,x+25,y-45, fill=self.color, outline= self.color, tag = str(count))

                self.canvas.create_oval(x+20,y-25,x+40,y-45, fill=self.color, outline= self.color, tag = str(count))

                self.canvas.create_oval(x+12,y-40,x+32,y-60, fill=self.color, outline= self.color, tag = str(count))

            else:
                x += 20
                self.canvas.create_oval(x+5,y-25,x+25,y-45, fill=self.color, outline= self.color, tag = str(count))

                self.canvas.create_oval(x+20,y-25,x+40,y-45, fill=self.color, outline= self.color, tag = str(count))

                self.canvas.create_oval(x+12,y-40,x+32,y-60, fill=self.color, outline= self.color, tag = str(count))

        self.last = False

    def draw_S_D(self,  pos, letter,count):
        x = self.current_x
        y = self.init_y
        self.canvas.create_arc(x,y-25,x-60,y+25, start = 0, extent = 180, fill=self.color, outline= self.color, tag = str(count))

        x -= 55
        if pos =="E":
            self.canvas.create_arc(x,y-15,x-35,y+15, start = 0, extent = 30, fill=self.color, outline= self.color, tag = str(count))

            self.canvas.create_arc(x,y-25,x-60,y+25, start = 0, extent = -180, fill=self.color, outline= self.color, tag = str(count))
            x-=5
            x-=60
            self.current_x = x
        else:
            self.canvas.create_rectangle(x,y,x-20, y-5, fill = self.color, outline=self.color, tag = str(count))
            x-=20
            self.current_x = x
        if letter =="D":
            if pos =="E":
                self.canvas.create_oval(x+45,y-25,x+65,y-45, fill = self.color, outline=self.color, tag = str(count))

            else:
                self.canvas.create_oval(x+20, y-25,x+40, y-45, fill = self.color, outline=self.color, tag = str(count))
        self.last = False

    def draw_T_DH(self,letter,count):
        x= self.current_x
        y = self.init_y
        self.canvas.create_arc(x,y-25,x-60,y+25, start = 0, extent = 180, fill=self.color, outline= self.color, tag = str(count))


        self.canvas.create_rectangle(x-40, y, x-55, y-60, fill=self.color, outline = self.color, tag = str(count))


        if letter =="DH":
            self.canvas.create_oval(x-10, y-25,x-30, y-45, fill = self.color, outline=self.color, tag = str(count))

        self.current_x-=60
        self.last=False

    def draw_3_gh(self,pos, letter,count):
        x = self.current_x
        y = self.init_y
        self.canvas.create_arc(x+40,y-35,x-40,y+35, start=90, extent =90, fill=self.color, outline= self.color, tag = str(count))

        self.canvas.create_arc(x+15,y-20,x-15,y+20, start=90, extent =90, fill=self.bg, outline= self.bg, tag = str(count))

        if self.last == False :
            self.canvas.create_rectangle(x,y, x-15, y-5, fill=self.color, outline = self.color, tag = str(count))
        if pos == "B":
            self.canvas.create_rectangle(x-40, y, x-55, y-5, fill=self.color, outline = self.color, tag = str(count))

            self.current_x -= 55
        else:
            self.canvas.create_rectangle(x-40, y, x-45, y-5, fill=self.color, outline = self.color, tag = str(count))

            x -= 45
            self.canvas.create_arc(x-5,y-20,x+40,y+50, start=145, extent =180, fill=self.color, outline= self.color, tag = str(count))

            self.current_x -= 50
        if letter =="gh":
            if pos =="B":
                self.canvas.create_oval(x-10, y-35,x+10, y-55, fill = self.color, outline=self.color, tag = str(count))

            else:
                self.canvas.create_oval(x+30, y-35,x+50, y-55, fill = self.color, outline=self.color, tag = str(count))

        self.last = False

    def draw_f_q(self, pos, letter,count):
        x = self.current_x
        y = self.init_y
        self.canvas.create_arc(x+30,y-25, x-30, y+25, start=90, extent=90,fill = self.color, outline=self.color, tag = str(count))

        self.canvas.create_rectangle(x-30,y,x-60, y-5, fill=self.color, outline=self.color, tag = str(count))

        self.current_x -= 60
        x= self.current_x
        if pos == "E":
            self.canvas.create_arc(x+15,y-15,x-15,y+16,start=90, extent=90,fill = self.color, outline=self.color, tag = str(count))


            self.current_x -= 15
        self.last = False
        if letter == "f":
            self.canvas.create_oval(x+45, y-30,x+65, y-50, fill = self.color, outline=self.color, tag = str(count))

        if letter =="q":
            self.canvas.create_oval(x+45, y-30,x+65, y-50, fill = self.color, outline=self.color, tag = str(count))

            self.canvas.create_oval(x+45, y-45,x+65, y-65, fill = self.color, outline=self.color, tag = str(count))


    def draw_k(self,pos,letter,count):
        x = self.current_x
        y = self.init_y
        if pos == "E":
            self.canvas.create_rectangle(x, y, x-17, y-60, fill=self.color, outline = self.color, tag = str(count))

            self.canvas.create_rectangle(x-17, y, x-47, y-5, fill=self.color, outline = self.color, tag = str(count))

            self.canvas.create_polygon(x-20,y-25,x-35,y-25,x-20,y-45,x-20,y-35,x-25,y-35,x-20,y-25, fill=self.color, outline = self.color, tag = str(count))

            self.current_x -= 47

        if pos == "B":
            self.canvas.create_rectangle(x,y,x-40,y-5,fill=self.color, outline = self.color, tag = str(count))

            self.canvas.create_polygon(x,y,x-10,y,x-30,y-40,x-20,y-40,fill=self.color, outline = self.color, tag = str(count))

            self.canvas.create_rectangle(x,y-40,x-30,y-45,fill=self.color, outline = self.color, tag = str(count))

            self.current_x-= 40
        self.last=False

    def draw_l(self,pos,letter,count):
        x = self.current_x
        y = self.init_y
        if pos == "E":
            self.canvas.create_rectangle(x, y, x-17, y-60, fill=self.color, outline = self.color, tag = str(count))

            self.canvas.create_arc(x,y+25,x-50,y-25, start=0, extent =-180, fill=self.color, outline= self.color, tag = str(count))

            self.current_x-= 50

        if pos == "B":
            self.canvas.create_rectangle(x, y, x-17, y-60, fill=self.color, outline = self.color, tag = str(count))

            x-=17
        self.current_x -=17
        self.last = False

    def draw_m(self,pos,letter,count):
        x= self.current_x
        y=self.init_y
        if pos == "E":
            self.canvas.create_arc(x,y+10,x-25,y-15, start=0, extent =359, fill=self.color, outline= self.color, tag = str(count))

            self.canvas.create_rectangle(x-25, y, x-42, y+50, fill=self.color, outline = self.color, tag = str(count))

            self.current_x -= 42

        if pos == "B":
            self.canvas.create_arc(x,y+10,x-25,y-15, start=0, extent =359, fill=self.color, outline= self.color, tag = str(count))

            self.canvas.create_rectangle(x-20, y, x-40, y-5, fill=self.color, outline = self.color, tag = str(count))

            self.last = True
            self.current_x -= 40

    def draw_H(self, pos, letter, count):
        x = self.current_x
        y = self.init_y
        if pos == "E" or pos == "B":
            self.canvas.create_arc(x-30, y-30, x+30, y+30, start=90, extent = 90, fill = self.color, outline = self.color, tag = str(count))
            self.current_x -= 30
        if pos == "M":
            self.canvas.create_polygon(x,y,x-20, y+25, x-40, y, fill = self.color, outline = self.color, tag = str(count))
            self.current_x-= 40
        self.last = False







    def adjust_size(self, size):
        self.canvas.scale( "ALL",0.001, 0.001,size/5.0 ,size/5.0)
        dx = self.canvas.coords("ALL")[0]
        dx = dx/(size/5.0)-dx

        self.canvas.move("ALL", dx, dx)

#        print "sizE"
        return

    def draw_image(self, angle):
        self.blank = Image.new("RGBA",(700,700),self.bg)
        self.image = ImageDraw.Draw(self.blank)
        all_tags = self.canvas.find_all()

        for i in all_tags:
#            print self.canvas.gettags(i)
            if self.canvas.type(i) == "rectangle":
                coords = self.canvas.coords(i)
                self.image.rectangle(coords, outline=self.color, fill = self.color)

            if self.canvas.type(i) == "polygon":
                coords = self.canvas.coords(i)
                self.image.polygon(coords, outline = self.color, fill = self.color)
            if self.canvas.type(i) =="arc":
                coords = self.canvas.coords(i)
                for k in range(len(coords)):
                    coords[k] = int(coords[k])

                start= self.canvas.itemcget(i,option="start")
                extent= self.canvas.itemcget(i,option="extent")
                start, extent = int(eval(start)), int(eval(extent))
                self.image.pieslice(coords, -start-extent, -start, fill = self.color)
            if self.canvas.type(i) == "oval":
                coords = self.canvas.coords(i)
                for i in range(len(coords)):
                    coords[i] = int(coords[i])
                self.image.ellipse(coords, fill = self.color, outline=self.color)

        self.img = seg.cropPic(self.blank)
#        img.save("trial.png")

        rot = self.img.rotate(angle, expand = 1)
        fff = Image.new('RGBA', rot.size, self.bg)

        out = Image.composite(rot, fff, rot)

        out.save("resources/calligraphy.gif")

        self.blank = self.blank.crop((self.current_x-75, 250, self.init_x, 420))
        self.blank.save('resources/test.png')
        return

    def translate(self, deg):
        new = Image.new("RGBA",(700,700),self.bg)
        for i in range(self.reps):
            if i%2 == 0:
                new.paste(self.img,(350-50*i, 350 - 50*i))
            else:
                new.paste(self.img,(350+50*i, 350+50*i))


        rot = new.rotate(deg, expand = 1)
        fff = Image.new('RGBA', rot.size, self.bg)

        out = Image.composite(rot, fff, rot)
        new = out
        new.save("resources/test.gif")




    #copied from https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
    def rotate(self, deg):
        new = Image.new("RGBA",(700,700),self.bg)
        new.paste(self.img, (320,320))
        for i in range(self.reps):
            ox, oy = 350, 350
            px, py = 350 + 200, 350

            angle = 360.0/ self.reps * i
            qx = ox + math.cos(math.radians(angle)) * (px - ox) - math.sin(math.radians(angle)) * (py - oy)
            qy = oy + math.sin(math.radians(angle)) * (px - ox) + math.cos(math.radians(angle)) * (py - oy)
            new.paste(self.img, (int(qx),int(qy)))

        rot = new.rotate(deg, expand = 1)
        fff = Image.new('RGBA', rot.size, self.bg)

        out = Image.composite(rot, fff, rot)
        new = out
        new.save("resources/test.gif")



    def adjust_canvas(self, regulator=False):
        if regulator == False:
            self.im = PhotoImage(file= "resources/calligraphy.gif")
        else:
            self.im = PhotoImage(file = "resources/test.gif")

        self.canvas.create_image(self.init_x,370,image= self.im, tag = "image")

        return

    def move_canvas(self,offset):
        if len(self.letters)>0:
            self.canvas.move("image", offset[0],offset[1])

    def update_cnv(self, parent, Ctext, Ccolor, Cbg, Csize, Cangle, canvas, regulator, reps):

        if Cbg == Ccolor:
            return

        if Ctext != self.letters or Ccolor != self.color or Cbg != self.bg or Csize != self.size or Cangle!= self.angle or regulator != self.regulator or reps!= self.reps:
#            print "here"
            self.init_x = self.determine_initial_pos()
            self.init_y = 370
            self.current_x = self.init_x
            self.last = False
            self.canvas.delete("ALL")

            self.letters = Ctext
            self.color = Ccolor
            self.bg = Cbg
            self.size = Csize
            self.angle = Cangle
            self.canvas = canvas
            self.parent = parent
            self.reps = reps
            self.regulator = regulator
            count = 0
            for i in range(len(self.letters)):
                self.draw_letter(self.letters[i],i, self.letters, count)
                count+=1

#            b = self.canvas.bbox("1")
#            print b
            if len(self.letters)>0:
                self.canvas.addtag_all("ALL")
#                print self.canvas.bbox("ALL")
                self.adjust_size(self.size)
                self.draw_image(self.angle)
                self.canvas.delete("ALL")

                self.adjust_canvas()
            if regulator == "translation":
                self.translate(self.angle)
                self.adjust_canvas(True)

            if regulator == "rotation":
                self.rotate(self.angle)
                self.adjust_canvas(True)






