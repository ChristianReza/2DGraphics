# %%
from PIL import Image, ImageDraw
import colorsys
import numpy as np


class MyImage():
  def __init__(self, image):
    self.image = image
    self.width = image.size[0]
    self.height = image.size[1]

  def blackAndWhite(self):
    """Half the image black and white and draw a 
    rectable in the top right corner."""
    px = self.image.load()

    width = self.width
    height = self.height

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

    # im.show()

    im.save("blackAndWhite.png", "PNG")

  def crop(self, ulx, uly, lrx, lry):
      """Crop the image"""
      image = self.image.load()

      width = lrx - ulx
      height = lry - uly
      newIm = Image.new(mode="RGB", size=(width, height))
      newLoad = newIm.load()
      
      for h in range(height):
          for w in range(width):
              pixelInt = image[w + ulx, h + uly]
              newRGB = (pixelInt)
              newLoad[w, h] = newRGB

      # newim.show()

      newIm.save("cropped.png", "PNG")
      return self

  def translate(self, i, j, bool):
      """Translate the image"""
      px = self.image.load()
      width = self.width
      height = self.height
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


      # newim.show()


      newIm.save("trasnlate.png", "PNG")
      return self

  def translateNearestNeighbor(self, i, j, bool):
      """Translate image with nearest neighbor"""
      px = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGBA", size=(width, height))

      for y in range(height):
          for x in range(width):
              originalX = (x - i + .5)
              originalY = (y - j + .5)

              if (originalX < 0 or 
                  originalX >= width or
                      originalY < 0 or
                          originalY >= height):
                          continue

              pixelInt = px[originalX, originalY]
              newRBG = (pixelInt)
              newLoad = newIm.load()
              newLoad[x, y] = newRBG


      # # newim.show()

      newIm.save("trasnlateNearestNeighbor.png", "PNG")
      return self

  def translateLinear(self, i, j, bool):
      """Translate image with nearest neighbor"""
      px = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGBA", size=(width, height))

      for y in range(height):
          for x in range(width):
              originalX = (x - i + .5)
              leftPixel = originalX
              rightPixel = originalX + 1
              originalY = (y - j + .5)

              if (originalX < 0 or 
                  originalX >= width or
                      originalY < 0 or
                          originalY >= height):
                          continue
              
              pixelLeft = px[leftPixel, originalY]
              pixelRight = px[rightPixel, originalY]

              percent = i - int(i)
              # (Red * 1 - percent), (Green * 1 - percent), (Blue * 1 - percent)
              leftPixelColoration = (int(pixelLeft[0] * (1 - percent)), int(pixelLeft[1] * (1 - percent)), int(pixelLeft[2] * (1 - percent)))
              # (Red * percent), (Green * percent), (Blue * percent)
              rightPixelColoration = (int(pixelRight[0] * (percent)), int(pixelRight[1] * (percent)), int(pixelRight[2] * (percent)))

              finalRed = leftPixelColoration[0] + rightPixelColoration[0]
              finalGreen = leftPixelColoration[1] + rightPixelColoration[1]
              finalBlue = leftPixelColoration[2] + rightPixelColoration[2]

              finalColor = (finalRed, finalGreen, finalBlue)

              newLoad = newIm.load()
              newLoad[x, y] = finalColor


      # newim.show()

      newIm.save("translateLinear.png", "PNG")
      return self

  def scaleNearestNeighbor(self, scaleX, scaleY):
    """Scale nearest neighbor"""
    px = self.image.load()
    width = self.width
    height = self.height
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

    # newim.show()
    newIm.save("scale.png", "PNG")
    return self

  def roateNearestNeighbor(im, angle):
    """
    rotate around upper left pixel
    in image processesing, a positive angle
    rotates clockwise.

    atan2
    """

  def convertHSV():
    """Convert RGB to HSV"""
    r = 0.225
    g = 0.128
    b = 0.64
    print(colorsys.rgb_to_hsv(r, g, b))

  def blurImage(self, kernel):
      """blur image"""
      newPix = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGB", size=(width, height))
      newLoad = newIm.load()

      # Create image clone to blur
      for y in range(height):
          for x in range(width):
              rgb = newPix[x, y]
              r = rgb[0]
              g = rgb[1]
              b = rgb[2]
              newRGB = (r, g, b)
              newLoad[x, y] = newRGB
      # newim.show()


      for y in range(height):
          for x in range(width):
              sum = float(0)
              for ky in range(-1, 1):
                  for kx in range(-1, 1):
                      color = []
                      px = x + kx
                      py = y + ky
                      if (px >= 0 and
                              px < width and
                                  py >= 0 and
                                      py < height):
                          color = newPix[px, py]
                      
                      greyScale = 0 if color == [] else color[0] # get red value else 0
                      kernelValue = kernel[kx + 1][ky + 1]
                      sum += (greyScale * kernelValue)
                      
              newRBG = int(sum)
              
              newLoad[x, y] = (newRBG, newRBG, newRBG)


      # newim.show()
      newIm.save("blur.png", "PNG")
      return self
    
  def imageKernel(self, blur=3):
    """kernel for image blur"""
    kernel = np.empty((blur, blur))
    #     create matrix
    #    [[0. 0. 0.]
    #     [0. 0. 0.]
    #     [0. 0. 0.]]
    for y in range(blur):
      for x in range(blur):
          kernel[y][x] = float(1 / 9.0)
    im.blurImage(kernel)

# %%

print("Start")
# im = MyImage(Image.open("Beluga.jpg"))

im = MyImage(Image.open("chrome.jpg"))

# im.blackAndWhite()

im.crop(500, 500, im.width, im.height).translate(50, 50, False)

im.translate(50, 50, False)

im.translateNearestNeighbor(50.5, 50.5, False)

im.translateLinear(50.5, 50.5, False)

im.scaleNearestNeighbor(0.5, 0.5)

# roateNearestNeighbor(im, 20)

im.imageKernel()

print("Finish")

# %%
