# Stack -> first in, last out
class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    # if len(self.items == []):
    #   return True
    # else:
    #   return False
    return self.items == []

  def push(self, item):
    # print(self.items += [item])
    return (self.items.append(item))


  def pop(self,item):
    return self.items.pop(item)

  def list(self):
    return self.items
    print (self.items)

  def test(self):
    return self.items

  def size(self):
    return len(self.items)

a = Stack()
a.push(2)
a.push(3)


print(a.size())
  #should print out
# print(list())
# print(a.test())

# print(a.size())

# s = Stack()
# s.push('a')
# print(s.is_empty())
# print(s.peek())
# print(s.is_empty())
# print(s.pop())
# print(s.is_empty())