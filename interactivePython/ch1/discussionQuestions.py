# Construct a class hierarchy for people on a college campus. Include faculty, staff, 
# and students. What do they have in common? What distinguishes them from one another?


# class People:
#   def __init__(self, money):
#     self.money =  money

#   def returnMoney(self, money):
#     return money*2


# test = People(2)
# print(People.returnMoney(2))

# def this_is_a_test(input1):
#   if(input1 == type(int)):
#     print("this is a number")
#   else:
#     print("this isn't an int")

# a = this_is_a_test('Friday')
# print(a)

#1.16 discussion questions

'''
Construct a class hierarchy for people on a college campus. 
Include faculty, staff, and students. What do they have in common? What distinguishes them from one another?
'''

class College:

  def __init__(self, position, title):
    self.position = position
    self.title = title

  def role(self):
    print("I'm a " + self.position) 

# a = College_Campus("staff", "mr")
# a.role()

class Faculty(College):
  def __init__(self, position, title, staffID):
    College.__init__(self, position, title)
    self.staffID = staffID

  def creds(self):
    print("im a " + self.position + self.title + self.staffID)

# b = Faculty
# b.role('Prof', 'Mr', 1111)

college = College('prof', 'mr')
faculty = Faculty('prof', 'mr', 111)
print(faculty.creds())

class Complex:
  def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart

x = Complex(2,-5)
# print(x.r)



















