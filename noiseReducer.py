import PIL
import math
import time
import statistics
from PIL import Image, ImageEnhance

path = input("Path: ")
loops = int(input("Loops: "))

for z in range(loops):
    print(f"Loop {z}")

    # z increments depending on the loop amount therefore you want it to edit the previously edited image per loop
    if z > 0:
        im = Image.open(f"noiseNull{z}.jpg")
    else:
        im = Image.open(path)

    width, height = im.size
    rgb_im = im.convert('RGB')
    img = Image.new('RGB', (width, height), "black")  # create a new black image
    pixels = img.load()  # create the pixel map


    def returnMedian(neighbouringPixels):
        """
        The returnEdge function takes an array of RGB tuples and finds the median of each R G B value. It then returns a new tuple with said values

        :param neighbouringPixels: List
        :return: Tuple
        """

        # Red median
        findMedian = []
        for i in neighbouringPixels:
            if i[0] is not None: # The check to make sure is not None is completed because if a pixel is outside of the range of the image, it will be read as None
                findMedian.append(i[0])
        redMedian = int(statistics.median(findMedian))

        # Green median
        findMedian = []
        for i in neighbouringPixels:
            if i[1] is not None:
                findMedian.append(i[1])
        greenMedian = int(statistics.median(findMedian))

        # Blue median
        findMedian = []
        for i in neighbouringPixels:
            if i[2] is not None:
                findMedian.append(i[2])
        blueMedian = int(statistics.median(findMedian))

        return int(redMedian), int(greenMedian), int(blueMedian)

    looper = 0
    timeStart = time.time()

    for i in range(width):
        looper += 1
        # Display position in rows every 10 since printing is known to slow down code significantly
        if looper == 10:
            looper = 0
            print(f"Row: {i}/{width}")

        for j in range(height):
            r, g, b = rgb_im.getpixel((i, j))
            neighbours = []

            # The try checks if the neighbouring pixel is in the range of the image.
            # If it is not, it sets the RGB values to None

            # Pixel above
            try:
                upr, upg, upb = rgb_im.getpixel((i, j - 1))
            except Exception:
                upr, upg, upb = (None, None, None)

            # Pixel below
            try:
                downr, downg, downb = rgb_im.getpixel((i, j + 1))
            except Exception:
                downr, downg, downb = (None, None, None)

            # Pixel to left
            try:
                leftr, leftg, leftb = rgb_im.getpixel((i - 1, j))
            except Exception:
                leftr, leftg, leftb = (None, None, None)

            # Pixel to right
            try:
                rightr, rightg, rightb = rgb_im.getpixel((i + 1, j))
            except Exception:
                rightr, rightg, rightb = (None, None, None)

            # Appending tuples of neighbouring pixels
            neighbours.append((upr, upg, upb))
            neighbours.append((downr, downg, downb))
            neighbours.append((leftr, leftg, leftb))
            neighbours.append((rightr, rightg, rightb))

            r, g, b = returnMedian(neighbours)
            pixels[i, j] = (int((r)), int((g)), int((b)))  # Set the colour accordingly to their median

    timeCurrent = time.time()
    print(f"Time taken: {timeCurrent - timeStart}")

    img.save(f"./noiseNull{z + 1}.jpg")
