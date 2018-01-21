class Descriptor(object):

  def __init__(self):
    self._name = ''

  def __get__(self, instance, owner):
    print("Getting: %s" %self._name)
    return self._name

  def __set__(self, instance, name):
    print("Setting: %s" % name)
    self._name = name.title()

  def __delete__(self, instance):
    print("Deleting: %s" %self._name)
    del self._name

class Person(object):
  name = Descriptor()

# user = Person()
# print(user)

class Day(object):
    def __init__(self, visits, contacts):
        self.visits = visits
        self.contacts = contacts
    def __str__(self):
        return “Visits: %i, Contacts: %i” % (self.visits, self.contacts)

day1 = Day(10,1)
print(day1)
#just for a git commit..