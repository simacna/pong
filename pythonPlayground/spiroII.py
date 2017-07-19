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

class MyClass:
  i = 123

  def f(self):
    return "hi"
yo = MyClass()
# print(yo.f()) -- returns error

class myClass:
  def __init__(self):
    self.data = [1]

class Complex:
  def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart

x = Complex
x.counter = 1
while x.counter < 10:
  x.counter = x.counter * 2

# print(x.counter)

del x.counter

aa = yo.f
# print(aa())  -- works!

class Dog:
  def __init__(self, name):
    self.name = name
    self.tricks = []

  def add_trick(self, trick):
    self.tricks.append(trick)

d = Dog('Fido')
d.add_trick('dance')
print(d.tricks)






