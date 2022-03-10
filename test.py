from PIL import Image
import os
import numpy as np

width = 500
height = 500 
numsuit = 0
filename = "suit"

listofcolours = [[255,255,255],[0,0,0],[]]
img = Image.open("Accessories/sunglasses.png")
width = img.size[0]
height = img.size[1]
for colours in listofcolours:
    r = colours[0]
    g = colours[1]
    b = colours[2]
    for i in range(0,width):
        for j in range(0,height):
            data = img.getpixel((i,j))
            if (data[0]==41 and data[1]==47 and data[2]==51):
                img.putpixel((i,j),(r,g,b))
    img.save('Accessories/'+'testaccessories.png',"PNG")

