#1. implent the simple methods getNum and getDen that will return num/den of a fraction
class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum
     def getNum(self):
      return(self.num)

fraction = Fraction(2,3)
# fraction.__add__('4/6')

#question 6-9 don't need code

a = True

if logical_xor(a):
    print("yes")


