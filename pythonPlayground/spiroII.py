#a class that draws a Spirograph

class Spiro:
  #constructor
  def __init__(self, xc, yc, col, R, r, l):
    #create the turtle object
    self.t = turtle.Turtle()

    #set cursor shape
    self.t.shape('turtle')

    #set step in degrees
    self.step = 5

    #set the drawing complete flag
    self.drawingComplete = False

    #set the parameters
    self.setparams(xc, yc, col, R, r, l)

    #initialize the drawing 
    self.restart()

  def setparams(self, xc, yc, col, R, r, l):
    #the Spirograph parameters
    self.xc = xc
    self.yc = yc
    self.R = int(R)
    self.r = int(r)
    self.l = l
    self.col = col

    #







