# %%
from PIL import Image, ImageDraw
import colorsys, math
import numpy as np


class MyImage():
  def __init__(self, fileName):
    self.image = Image.open(fileName)
    self.fileName = fileName
    self.width = self.image.size[0]
    self.height = self.image.size[1]


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
        # g = rgb[1]
        # b = rgb[2]

        # if(x < width/2):
        g = r
        b = r

        newRGB = (r, g, b)
        px[x,y] = newRGB

    # Now draw a rectangle
    # draw = ImageDraw.Draw(self.image)

    # draw.rectangle((10, 10, 100, 100), outline = (255, 0, 0))

    # im.save("blackAndWhite.png", "PNG")
    # self.image = im
    # self.width = im.size[0]
    # self.height = im.size[1]
    return self


  def crop(self, ulx, uly, lrx=0, lry=0):
      """Crop the image"""
      image = self.image.load()

    #   width = lrx - ulx
      width = self.width - ulx
    #   height = lry - uly
      height = self.height - uly
      newIm = Image.new(mode="RGB", size=(width, height))
      newLoad = newIm.load()
      
      for h in range(height):
          for w in range(width):
              pixelInt = image[w + ulx, h + uly]
              newRGB = (pixelInt)
              newLoad[w, h] = newRGB

      # newIm.save("cropped.png", "PNG")
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
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


      # newIm.save("trasnlate.png", "PNG")
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
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

      # newIm.save("trasnlateNearestNeighbor.png", "PNG")
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
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

      # newIm.save("translateLinear.png", "PNG")
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
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
    # newIm.save("scale.png", "PNG")
    self.image = newIm
    self.width = newIm.size[0]
    self.height = newIm.size[1]
    return self


  def roateNearestNeighbor(self, angle):
    """
    rotate around upper left pixel
    in image processesing, a positive angle
    rotates clockwise.
    atan2
    """
    px = self.image.load()
    width = self.width
    height = self.height
    newIm = Image.new(mode="RGB", size=(width, height))
    
    centerX = width/2
    centerY = height/2

    for y in range(height):
        for x in range(width):
          distanceX = x - centerX
          distanceY = y - centerY
          distance = math.sqrt(distanceX * distanceX + distanceY * distanceY)
          postAngle = math.atan2(distanceY, distanceX)
          preAngle = postAngle - (float)(angle)
          
          originalX = (int) ((distance * math.cos(preAngle) + .5) + centerX)
          originalY = (int) ((distance * math.sin(preAngle) + .5) + centerY)
          if (originalX < 0 or originalX >= width or originalY < 0 or originalY >= height):
              continue
          
          pixelInt = px[originalX, originalY]
          newRBG = (pixelInt)
          newLoad = newIm.load()
          newLoad[x, y] = newRBG
          
    self.image = newIm
    self.width = newIm.size[0]
    self.height = newIm.size[1]
    return self


  def histogram(self, cap):
    """Create histogram of image"""
    px = self.image.load()
    width = 256
    height = 300
    histogramImage = Image.new(mode="RGB", size=(width, height), color=(0,0,0))
    counts = [0] * width
    for y in range(self.height):
        for x in range(self.width):
    # Generate the histogram info
            rgb = px[x,y]
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            hsv = [0] * 3
            self.convertRGBtoHSV(r, g, b, hsv)
            value = (int)(hsv[2]*255)
            counts[value] += 1

    # Render the histogram
    maxValue = max(counts)
    if(cap != -1):
        maxValue = cap
    for x in range (len(counts)):
        draw = ImageDraw.Draw(histogramImage)
        percent = (counts[x] / maxValue * height)
        draw.rectangle([(x, height - percent), (x+1, height)], outline=(255,255,255))
    
    histogramImage.save("histogram.png", "PNG")
    return self


  def brighten(self, i):
      """brighten image"""
      px = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGBA", size=(width, height))

      for y in range(height):
          for x in range(width):
              rgb = px[x,y]
              r = rgb[0]
              g = rgb[1]
              b = rgb[2]
              
              hsv = [0] * 3
              
              self.convertRGBtoHSV(r, g, b, hsv)
              
              value = (hsv[2])
              
              value += i / (float)(255.0)
              value = min((float)(1.0), max(0, value))
              newColor = colorsys.hsv_to_rgb(hsv[0], hsv[1], value)
              newRed = (int)(newColor[0]*255)
              newGreen = (int)(newColor[1]*255)
              newBlue = (int)(newColor[2]*255)
              again = [0] * 3
              self.convertRGBtoHSV(newRed, newGreen, newBlue, again)
              
              
              newLoad = newIm.load()
              newRBG = (newRed, newGreen, newBlue)
              newLoad[x, y] = newRBG
              
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
      return self


  def contrast(self, amount):
      px = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGBA", size=(width, height))

      for y in range(height):
          for x in range(width):
              rgb = px[x,y]
              r = rgb[0]
              g = rgb[1]
              b = rgb[2]
              hsv = [0] * 3
              
              self.convertRGBtoHSV(r, g, b, hsv)
              
              value = (hsv[2])
              adjustedValue = value - (float)(.5)
              adjustedValue = adjustedValue * amount
              adjustedValue = adjustedValue + (float)(.5)
              adjustedValue = min((float)(1.0), max(0, adjustedValue))
              newColor = colorsys.hsv_to_rgb(hsv[0], hsv[1], adjustedValue)
              newRed = (int)(newColor[0]*255)
              newGreen = (int)(newColor[1]*255)
              newBlue = (int)(newColor[2]*255)
              
              again = [0] * 3
              self.convertRGBtoHSV(newRed, newGreen, newBlue, again)
              
              newLoad = newIm.load()
              newRBG = (newRed, newGreen, newBlue)
              newLoad[x, y] = newRBG
              
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
      return self


  def dither(self):
      self.grayscale()
      px = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGBA", size=(width, height))
      
      errorList = [[0 for c in range(height)] for r in range(width)]

      for y in range(height - 1):
          for x in range(width - 1):
              error = errorList[x][y]
              rgb = px[x,y]
              r = rgb[0]
            #   g = rgb[1]
            #   b = rgb[2]
            #   value = rgb[0]
            #   self.grayscale()
              
              bw = r
              adjusted = bw + error
              
              finalColor = [0, 0, 0]
              if (adjusted < 128):
                finalColor = [0, 0, 0]
                error += bw - 0
              else:
                finalColor = [255, 255, 255]
                error += bw - 255
                
              if (x < newIm.width - 1):
                  errorList[x + 1][y] += error * (7 / (float)(16.0))
              if (y < newIm.height - 1):
                  if (x > 0):
                      errorList[x - 1][y + 1] += error * (3 / (float)(16.0))
                  errorList[x][y + 1] += error * (5 / 16.0)
              if (x < newIm.width - 1):
                  errorList[x + 1][y + 1] += error * (1 / 16.0)
              

              newLoad = newIm.load()
              newRBG = (finalColor[0], finalColor[1], finalColor[2])
              newLoad[x, y] = newRBG
              
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
      return self


  def ditherColor(self):
      """Dither with color!"""
      px = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGBA", size=(width, height))
      
      # Create an empty list
      colors = []
      for i in range(8):
          colors.append([])
      
      colors[0].append((0,0,0))
      colors[1].append((255, 255, 255))
      colors[2].append((255, 0, 0))
      colors[3].append((0, 255, 0))
      colors[4].append((0, 0, 255))
      colors[5].append((255, 255, 0))
      colors[6].append((0, 255, 255))
      colors[7].append((255, 0, 255))
      
    #   print(colors[1])
    #   print(colors[1][0])
    #   print(colors[1][0][0])
      
       
      for y in range(height):
          rangeR = 0
          rangeG = 0
          rangeB = 0
          for x in range(width):
              rgb = px[x,y]
              r = rgb[0]
              g = rgb[1]
              b = rgb[2]
              adjust = ((r + rangeR), (g + rangeG), (b + rangeB))
              
            #   pickedColor = Arrays.stream(myColors).reduce((a, b) -> a.distanceL1(adjusted) < b.distanceL1(adjusted) ? a : b).get();
              for i in colors:
                  temp = i[0]
                  a = self.distance(temp, adjust)
                  b = self.distance(temp, adjust)
              
              rangeR = adjust[0]
              rangeG = adjust[1]
              rangeB = adjust[2]
              
              newLoad = newIm.load()
              newRBG = (rangeR, rangeG, rangeB)
              newLoad[x, y] = newRBG
      
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
      return self


  def distance(self, colorA, colorB):
      return abs(colorA[0] - colorB[0]) + abs(colorA[1] - colorB[1]) + abs(colorA[2] - colorB[2])


  def grayscale(self):
      px = self.image.load()
      width = self.width
      height = self.height
      newIm = Image.new(mode="RGBA", size=(width, height))

      for y in range(height):
          for x in range(width):
              rgb = px[x,y]
              r = rgb[0]
              g = rgb[1]
              b = rgb[2]
              hsv = [0] * 3

              self.convertRGBtoHSV(r, g, b, hsv)

              value = math.floor(min(255, hsv[2] * (float)(255.0)))

              newLoad = newIm.load()
              newRBG = (value, value, value)
              newLoad[x, y] = newRBG

      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
      return self


  def convertRGBtoHSV(self, r, g, b, hsv):
      """Populate HSV"""
      hue = -1
      saturation = -1
      value = -1

      red = (r / 255.0)
      green = (g / 255.0)
      blue = (b / 255.0)

      cMax = max(max(red, green), blue)
      value = cMax
      cMin = min(min(red, green), blue)
      delta = cMax - cMin

      if (cMax == 0):
        hue = 0
        value = 0
        saturation = 0
      else:
        if (delta == 0):
          hue = 0
          saturation = (cMax - cMin) / cMax
  
        else:
  
          saturation = (cMax - cMin) / cMax
  
          if (cMax == red):
            hue = (60 * (green - blue) / delta + 0) % 360
          elif (cMax == green):
            hue = (60 * (blue - red) / delta + 120) % 360
          elif (cMax == blue):
            hue = (60 * (red - green) / delta + 240) % 360
  
          hue /= 360

      hsv[0] = hue
      hsv[1] = saturation
      hsv[2] = value
      return self


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
      self.image = newIm
      self.width = newIm.size[0]
      self.height = newIm.size[1]
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
    return self


  def preview(self):
    self.image.show()


  def done(self):
    print("saving...")
    self.image.save("finished.png", "PNG")


  def reset(self):
    print("resetting image...")
    self.image = Image.open(self.fileName)
    return self


  def printDim(self):
      print("Your image dimensions are:")
      print('width: {}\theight: {}' .format(self.width, self.height))


# %%
selectedImage = input("Enter the name and extension of the image file to modify: ")
im = MyImage(selectedImage)

print("Start")

def switch(action):
    return switcher.get(action, default)()

def blackAndWhite():
    im.blackAndWhite()
def translate():
    im.printDim()
    newX = int(input("Enter pixel amount to move image: "))
    newY = int(input("Enter pixel amount to move image: "))
    im.translate(newX, newY, False)
    im.printDim()
def translateNearestNeighbor():
    im.printDim()
    newX = int(input("Enter pixel amount to move image: "))
    newY = int(input("Enter pixel amount to move image: "))
    im.translateNearestNeighbor(newX, newY, False)
    im.printDim()
def crop():
    im.printDim()
    ulx = int(input("Enter new upper left X-pixel: "))
    uly = int(input("Enter new upper left Y-pixel: "))
    im.crop(ulx, uly)
    im.printDim()
def translateLinear():
    im.printDim()
    newX = int(input("Enter pixel amount to move image: "))
    newY = int(input("Enter pixel amount to move image: "))
    im.translateLinear(newX, newY, False)
    im.printDim()
def scaleNearestNeighbor():
    im.printDim()
    newX = float(input("Enter scale for X: "))
    newY = float(input("Enter scale for Y: "))
    im.scaleNearestNeighbor(newX, newY)
    im.printDim()
def roateNearestNeighbor():
    angle = float(input("Rotate around center by what angle: "))
    im.roateNearestNeighbor(angle)
def histogram():
    im.histogram(-1)
def brighten():
    brightenBy = int(input("Brighten by what: "))
    im.brighten(brightenBy)
def contrast():
    contrastBy = int(input("Contrast by what: "))
    im.contrast(contrastBy)
def ditherColor():
    im.ditherColor()
def dither():
    im.dither()
def grayscale():
    im.grayscale()
def preview():
    im.preview()
def save():
    im.done()
    return "saved"
def reset():
    im.reset()
def default():
    return "Invalid Request"

switcher = {
    "1": blackAndWhite,
    "2": translate,
    "3": translateNearestNeighbor,
    "4": crop,
    "5": translateLinear,
    "6": scaleNearestNeighbor,
    "7": roateNearestNeighbor,
    "8": histogram,
    "9": brighten,
    "10": contrast,
    "11": ditherColor,
    "12": dither,
    "13": grayscale,
    "p": preview,
    "s": save,
    "r": reset,
    }

print("What kind of action would you like to preform on your image?")
options = """
 1: Black and White
 2: Translate
 3: Translate Nearest Neighbor
 4: Crop
 5: Translate Linear
 6: Scale Nearest Neighbor
 7: Roate Nearest Neighbor
 8: Histogram
 9: Brighten
 10: Contrast
 11: Dither Color
 12: Dither BW
 13: Grayscale
 p: Preview
 s: Save
 r: Reset image
 q: Quit
"""
print(options)
request = ''
while (request != 'q'):
    request = input("Option #: ")
    print("request is :" + request)
    switch(request)

