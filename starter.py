# %%
from PIL import Image, ImageDraw

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

    im.save("trasnlate.png", "PNG")



# %%
print("Start")


im = Image.open("Beluga.jpg")

width = im.size[0]
height = im.size[1]

blackAndWhite(im)

crop(im, 500, 500, width, height)

# translate(im, 50, 50, False)

print("Finish")

# %%
