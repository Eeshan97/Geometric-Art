from turtle import *
import time

def Koch_string_helper(text,generation):
    print text
    print '\n'
    if generation <= 0:
        return text
    temp = ""
    for i in text:
        if i == "A":
            temp = temp + "ALARALA"
        else:
            temp += i
    text = temp
    return Koch_string_helper(text, generation -1)

def Koch_string(generation):
    return Koch_string_helper("A",generation-1)



def draw(length,generation):
    text = Koch_string(generation)
    if(generation>7):
        distance =900
    else:
        distance = length/2
    penup()
    clear()
    setpos(0,0)
    backward(distance)
    left(90)
    backward(distance/2)
    right(90)
    pendown()
    length /= 3**(generation-1)
    if length < 1:
        length = 1
    for i in text:
        if(i == "A"):
            forward(length)
        elif i == "L":
            left(60)
        else:
            right(120)

def koch():
    for i in range(1,8):
        if i > 4:
            delay(0)
        draw(700,i)
        time.sleep(1)

    done()

koch()
