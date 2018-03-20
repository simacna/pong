class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def lists(self):
         return self.items

def par(pars):
    balanced = True
    s = Stack()
    index = 0

    while index < len(pars) and balanced:
        item = pars[index]
        if item == '(':
            s.push(item)
        else:
            s.pop()

        index = index + 1

    if s.isEmpty() and balanced:
        return True
    else:
        return False

print(par('((()))'))
print(par('(()'))





def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
            # print('s.push')
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

# print(parChecker('((()))'))
# print(parChecker('(()'))
