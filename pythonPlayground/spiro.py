import math
import turtle

def drawCircleTurtle(x, y, r):
  turtle.up()
  turtle.setpos(x + r, r)
  turtle.down()

  for i in range(0, 365, 5):
    a = math.radians(i)
    turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

drawCircleTurtle(100, 100, 500)
turtle.mainloop()

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


class Dogg:
  def __init__(self, name):
    self.name = name
    self.tricks = []

  def tricks(self, tricks):
    self.tricks.append(tricks)

dog1 = Dog1('Sina')
print(dog1)


