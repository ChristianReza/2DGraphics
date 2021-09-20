# %%
from PIL import Image, ImageDraw
import colorsys

# %%
def blackAndWhite(im):
  """Half the image black and white and draw a 
  rectable in the top right corner."""
  px = im.load()

  width = im.size[0]
  height = im.size[1]

  for y in range(height):
    for x in range(width):
      rgb = px[x,y]

      r = rgb[0]
      g = rgb[1]
      b = rgb[2]

      if(x < width/2):
        g = r
        b = r

        newRGB = (r, g, b)
        px[x,y] = newRGB

  # Now draw a rectangle
  draw = ImageDraw.Draw(im)

  draw.rectangle((10, 10, 100, 100), outline = (255, 0, 0))

  im.show()

  im.save("blackAndWhite.png", "PNG")

# %%
def crop(im :Image, ulx, uly, lrx, lry):
    """Crop the image"""
    image = im.load()

    width = lrx - ulx
    height = lry - uly
    newIm = Image.new(mode="RGB", size=(width, height))
    newLoad = newIm.load()
    
    for h in range(height):
        for w in range(width):
            pixelInt = image[w + ulx, h + uly]
            newRGB = (pixelInt)
            newLoad[w, h] = newRGB

    newIm.show()

    newIm.save("cropped.png", "PNG")

# %%
def translate(im, i, j, bool):
    """Translate the image"""
    px = im.load()
    width = im.size[0]
    height = im.size[1]
    newIm = Image.new(mode="RGBA", size=(width, height))

    for h in range(height):
        for w in range(width):
            originalX = w - i
            originalY = h - j

            if (originalX < 0 or 
                originalX >= width or
                    originalY < 0 or
                        originalY >= height):
                        continue

            pixelInt = px[originalX, originalY]
            newRBG = (pixelInt)
            newLoad = newIm.load()
            newLoad[w, h] = newRBG


    newIm.show()


    newIm.save("trasnlate.png", "PNG")


def scaleNearestNeighbor(im, scaleX, scaleY):
  """Scale nearest neighbor"""
  px = im.load()
  width = im.size[0]
  height = im.size[1]
  newIm = Image.new(mode="RGB", size=(width, height))

  for y in range(height):
      for x in range(width):
        originalX = (x * (1/scaleX))
        originalY = (y * (1/scaleY))

        if (originalX < 0 or 
            originalX >= width or
                originalY < 0 or
                    originalY >= height):
                    continue
        
        pixelInt = px[originalX, originalY]
        newRBG = (pixelInt)
        newLoad = newIm.load()
        newLoad[x, y] = newRBG

  newIm.show()
  newIm.save("scale.png", "PNG")


def roateNearestNeighbor(im, angle):
  """
  rotate around upper left pixel
  in image processesing, a positive angle
  rotates clockwise.

  atan2
  """

# %%
def convertHSV():
  """Convert RGB to HSV"""
  r = 0.225
  g = 0.128
  b = 0.64
  print(colorsys.rgb_to_hsv(r, g, b))
  
  


# %%

print("Start")

im = Image.open("MuskDeer.jpg")

width = im.size[0]
height = im.size[1]

blackAndWhite(im)

crop(im, 500, 500, width, height)

translate(im, 50, 50, False)

scaleNearestNeighbor(im, 0.5, 0.5)

# roateNearestNeighbor(im, 20)

print("Finish")

# %%
