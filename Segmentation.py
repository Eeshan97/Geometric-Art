# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:52:43 2017

@author: Laila Elbeheiry
@andrew id: loe
@modification history:
    start           end
    11/11 22:52     12/11 03:32 
    25/11 10:03     25/11 15:43
"""
from PIL import Image



#returns the y position of beginning of blob
def findFirstY(pixels,w,h):
    #loop through each row from specified row to the end
    for b in range(0,h):
        for a in range(w):
            #if pixel is black then blob has started
            if pixels[a,b]!= pixels[0,0]:
                return b
    else: return "done"
    

#returns the y position of ending of blob
def findLastY(pixels,w,h):
    #loop through each row from specified row to the end
    for b in range(h-1,0,-1):
        inLine=False
        for a in range(w):
            #if the row has a black pixel then blob hasn't ended
            if pixels[a,b]!=pixels[0,0]:
                return b
    else: return "done"
    

#returns x coordinate of beginning of blob
#loop through each column starting from a specified column
def findFirstX(pixels,w,h):
    for a in range(0,w):
        for b in range(h):
            #if the column has a black pixel return its x coordinate
            if pixels[a,b]!=pixels[0,0]:
                return a
    else: return "done"
    
    
#returns x coordinate of ending of blob
#loop through each column starting from a specified column    
def findLastX(pixels,w,h):
    for a in range(w-1,0,-1):
        background=True
        for b in range(h):
            #if column has a black pixel then its still in the blob
            if pixels[a,b]!=pixels[0,0]:
                return a
    else: return "done"
    
def cropPic(im):
    w,h=im.size
    pixels=im.load()
    x_1 = findFirstX(pixels,w,h)
    x_2 = findLastX(pixels,w,h)
    y_1 = findFirstY(pixels,w,h)
    y_2 = findLastY(pixels,w,h)
    if x_1  =="done"or x_2  =="done"or y_1  =="done"or y_2 =="done":
        return "done"
    return im.crop((x_1,y_1,x_2,y_2))
    



                