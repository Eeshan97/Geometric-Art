from turtle import *
import random
import time


def initial(i):
    penup()
    colormode(255)
    setpos(i[0],i[1])
    seth(i[2])
    pencolor(i[3])
    pendown()

# text is a string
# rules is a dictionary
def L_helper(text,rules,generation):
    if generation <= 1: return text
    temp = ""
    text = text.upper()
    for i in text:
        if i in rules and i != "":
            temp += rules[i]
        else:
            temp += i
    k = random.randint(len(temp)/10,len(temp)-len(temp)/10)
    text = temp[:k] + "C" + temp[k:]
    return L_helper(text,rules,generation-1)

#division is the ratio of the 2nd generation line and 1st generation line
#rangle is the angle we wat to turn right by
#langle is the angle we want to turn left by
# X will mimic F but provided for recursion
# Y will mimic G
def draw(text,rules,generation,length,rangle,langle,color,initialpos,thick = 1):
    initial(initialpos)
    colormode(255)
    text = L_helper(text.upper(),rules,generation)
    text = text.upper()
    which_color = 0
    stacklist = []
    angle = 90
    for i in text:
        #print stacklist
        #print "angle:", angle
        if i != "X" and i!= "F" and thick > 1:
            width(thick)
            thick -= 1
        if i == "[":
            stacklist = [(xcor(),ycor(), length, angle,thick)] + stacklist
            if length<1: length = 1
        elif i == "F" or i == "X":
            forward(length)
        elif i == "C" and color:
            if which_color%3 == 0:
                pencolor(0,255,225)
            elif which_color%3 == 1:
                pencolor(255,0,225)
            else:
                pencolor(240,0255,0)
            which_color += 1
        elif i == "G" or i == "Y":
            penup()
            forward(length)
            pendown()
        elif i == "-":
            right(rangle)
            angle -= rangle
            #print "right"
        elif i == "+":
            left(langle)
            angle += langle
            #print "left"
        elif i=="]":
            penup()
            #print heading()
            temp = stacklist[0]
            if len(stacklist) > 1 :
                stacklist = stacklist[1:]
            else:
                stacklist = []
            setpos(temp[0],temp[1])
            seth(temp[3])
            angle = temp[3]
            #print heading()
            length = temp[2]
            thick = temp[4]
            width(thick)
            pendown()

                                
#draw("G",{"G" : "F[+G][G]F[+G]-FG", "F" : "FF"},7,5,1,25,25,True,(350,-350,90))

def koch_square():
#The koch square
    left(90)
    delay(0)
    for i in range(2):
        draw("F",{"F" : "F+F-F-F+F"},6,1,90,90,True,(0,0,90*((i+1)%2),"black"))
        draw("F",{"F" : "F-F+F+F-F"},6,1,90,90,True,(0,0,90*i,"red"))
        draw("F",{"F" : "F-F+F+F-F"},6,-1,90,90,True,(0,0,90*i,"green"))
        draw("F",{"F" : "F+F-F-F+F"},6,-1,90,90,True,(0,0,90*i,"blue"))
    ht()
    done()

def binary_tree():
    delay(0)
    draw("X",{"F" : "FF", "X" : "F[+X]-X"},11,1,45,45,False,(0,-450,90,"green"),5)
    ht()
    done()

def cantor():
    for i in range(1,7):
        draw("F",{"F" : "FGF", "G" : "GGG"},i,1000/(i**3),45,45,False,(-800,400-100*i,0,"black"))
        time.sleep(1)
    ht()
    done()


def Sierpinski():
    delay(0)
    draw("F-X-X",{"F" : "F-X+F+X-F", "X" : "XX"},11,1,120,120,True,(-700,-450,60,"black"))
    ht()
    done()

def plant():
    delay(0)
    width(5)
    draw("A",{"A" : "F[+A][A]F[+A]-FA", "F" : "FF"},10,1,25,25,False,(-175,-480,90,"#659D32"),5)
    width(5)
    draw("A",{"A" : "F[-A][A]F[-A]+FA", "F" : "FF"},10,1,25,25,False,(175,-480,90,"black"),5)
    ht()
    done()

def snowflake():
    delay(0)
    draw("F--F--F--",{"F" : "F-F++F-"},8,3,60,60,True,(0,0,0,"black"))
    ht()
    done()

def Levy_C():
    delay(0)
    draw("F",{"F" : "+F--F+"},14,3,45,45,True,(-300,100,0,"black"))
    draw("F",{"F" : "-F++F-"},14,3,45,45,True,(-300,-100,0,"blue"))
    ht()
    done()

def Hilbert():
    delay(0)
    draw("A",{"A" : "+BF-AFA-FB+", "B" : "-AF+BFB+FA-"},8,4,90,90,True,(-300,-300,0,"black"))
    ht()
    done()

def custom():
    delay(0)
    width(3)
    draw("A",{"A" : "F[+A][A]F[+A]-FA", "F" : "FF"},8,1,25,25,False,(-860,-460,90,"#659D32"),3)
    width(3)
    draw("A",{"A" : "F[-A][A]F[-A]+FA", "F" : "FF"},8,1,25,25,False,(860,150,90,"#659D32"),3)
    width(3)
    draw("A",{"A" : "F[+A][A]F[+A]-FA", "F" : "FF"},8,1,25,25,False,(-860,150,90,"#659D32"),3)
    width(3)
    draw("A",{"A" : "F[-A][A]F[-A]+FA", "F" : "FF"},8,1,25,25,False,(860,-460,90,"#659D32"),3)
    draw("F",{"F" : "+F--F+"},14,3,45,45,True,(-470,-150,90,"black"))
    draw("F",{"F" : "-F++F-"},14,3,45,45,True,(470,-150,90,"blue"))
    draw("F-X-X",{"F" : "F-X+F+X-F", "X" : "XX"},7,3,120,120,True,(-350,75,0,"black"))
    draw("F-X-X",{"F" : "F-X+F+X-F", "X" : "XX"},7,-3,120,120,True,(310,-100,0,"black"))
    draw("A",{"A" : "+BF-AFA-FB+", "B" : "-AF+BFB+FA-"},7,3,90,90,True,(-100,-100,0,"black"))
    draw("F",{"F" : "+F--F+"},14,3,45,45,True,(-120,205,0,"black"))
    draw("F",{"F" : "-F++F-"},14,3,45,45,True,(-120,-205,0,"blue"))
    ht()
    done()

