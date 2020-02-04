import PIL
import math
import time
import statistics
from PIL import Image, ImageEnhance
path = input("Path: ")
loops = int(input("Loops: "))

for z in range(loops):
    print(f"Loop {z}")
    if z > 0:
        im = Image.open(f"noiseNull{z}.jpg")
    else:
        im = Image.open(path)
    width, height = im.size
    rgb_im = im.convert('RGB')

    img = Image.new( 'RGB', (width,height), "black") # create a new black image
    pixels = img.load() # create the pixel map

    def returnEdge(neigh):
        findMedian = []
        #red
        for i in neigh:
            if i[0] is not None:
                findMedian.append(i[0])
        redMed = int(statistics.median(findMedian))
        findMedian = []        #green
        for i in neigh:
            if i[1] is not None:
                findMedian.append(i[1])
        greenMed = int(statistics.median(findMedian))
        findMedian = []
        #blue
        for i in neigh:
            if i[2] is not None:
                findMedian.append(i[2])
        blueMed = int(statistics.median(findMedian))

        return int(redMed), int(greenMed), int(blueMed)
        
    looper = 0
    now = time.time()
    for i in range(width):
        looper +=1
        if looper == 10:
            looper = 0
            print(f"Row: {i}/{width}")
        for j in range(height):
            r, g, b = rgb_im.getpixel((i, j))
            neighbours=[]
            try:
                upr, upg,upb = rgb_im.getpixel((i, j-1))
                
            except Exception:
                upr, upg,upb = (None,None,None)
            try:
                downr, downg,downb = rgb_im.getpixel((i, j+1))
                
            except Exception:
                downr,downg,downb = (None,None,None)
            try:
                leftr, leftg, leftb = rgb_im.getpixel((i-1, j))
                
            except Exception:
                leftr, leftg, leftb = (None,None,None)
            try:
                rightr, rightg, rightb = rgb_im.getpixel((i+1, j))
                
            except Exception:
                rightr, rightg, rightb = (None,None,None)

            neighbours.append((upr,upg,upb))
            neighbours.append((downr, downg,downb))
            neighbours.append((leftr, leftg, leftb))
            neighbours.append((rightr, rightg, rightb))

            r,g,b = returnEdge(neighbours)

                
            pixels[i,j] = (int((r)),int((g)),int((b))) # set the colour accordingly
            
    befr = time.time()
    print(befr-now)
    #img.show(title= f"Loop {z}")
    
    img.save(f"./noiseNull{z+1}.jpg")


