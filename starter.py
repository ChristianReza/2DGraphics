from PIL import Image, ImageDraw

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

  im.save("out.png", "PNG")



print("Start")

im = Image.open("Beluga.jpg")
blackAndWhite(im)

print("Finish")

