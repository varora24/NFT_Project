from PIL import Image
import os
import numpy as np

numpicture = 0
for bg in os.listdir("backgrounds"):
    pathtobackground = "backgrounds/"+bg
    if not os.path.isfile(pathtobackground):
        continue
    background = Image.open(pathtobackground)
    for suitfile in os.listdir("Blazer+Tie"):
        suitpath = "Blazer+Tie/"+suitfile
        if not os.path.isfile(suitpath):
            continue
        suit = Image.open(suitpath)
        background.paste(suit,(0,0),suit)
        for facefile in os.listdir("face"):
            facepath = "face/"+facefile
            if not os.path.isfile(facepath):
                continue
            face = Image.open(facepath)
            background.paste(face,(0,0),face)
            for accessoriefile in os.listdir("Accessories"):
                backgroundcopy = background
                pathtoaccessories = "Accessories/"+accessoriefile
                if not os.path.isfile(pathtoaccessories):
                    continue
                acc = Image.open(pathtoaccessories)
                backgroundcopy.paste(acc,(0,0),acc)
                filename = "vermin#"+str(numpicture)+".png"
                numpicture+=1
                backgroundcopy.save("output/"+filename,"PNG")
