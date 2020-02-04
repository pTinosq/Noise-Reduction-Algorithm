# Python noise reduction algorithm

As part of the A-Level OCR B course we have to learn the main different types of image manipulation and how they're achieved.
I decided that the best way for me to learn the algorithm was to make it myself so here is a simple algorithm that'll remove noise from images using a fairly common but not necessarily effective method.

# Dependancy
- Python 3.7+
- [PIL (pillow) module](https://pillow.readthedocs.io/en/stable/) 

# How it works
- The user enters the image path
- The user enters how many noise reduction passes (Usually method is redundant after 7-10 passes)
- The algorithm will loop through each pixel in the image, get the pixel's RGB values along with its neighbours' RGB values. It will then find the median of those values and replace the pixel with that value.

# Usage
Run the .py and provide a path to the image <string>. The algorithm works by reading every single pixel in the image therefore I do not recommend using this algorithm on images with a large dimension.
Example path: ../images/baguette.jpg

Then the algorithm will ask you for the number of passes <integer>. This is how many times the algorithm will be repeated.
  
The algorithm will proceed to go line by line, row by row and run the algorithm mentioned in the **How it works** section.

Once completed it will show the final image and then it will save it in the same directory as the .py file under the name __noiseNull{passNumber}.jpg__ where passNumber is the final pass that was run.

# Known issues

- The image will end up getting blurred after too many passes
- Large areas of noise will not be removed but smoothened out
- After the 7-10th passes there is no significant change to the image
