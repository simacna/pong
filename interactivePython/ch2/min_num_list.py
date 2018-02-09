def min_list(list):
  min = list[0]
  for idx in list:
    if list[idx] < min:
      min = list[idx]
  return min

# print(min_list(a))
# print(range(10))


#section 2.4

def sina_anagram(s1, s2):
  string1 = []
  string2 = []

  for _ in s1:
    string1.append(_)
  for _ in s2:
    string2.append(_)




# print(sina_anagram('hello', 'worsld'))
variable = 'hello'
# s = variable.split(' ')
# print(s)
test = []
for _ in variable:
  test.append(_)

# print(test)
# b = list(map(string,variable))



def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            print("pos2", pos2)
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
            # print('alist[pos2]', alist[pos2])
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

# print(anagramSolution1('abc','dcba'))

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches



#write two python functions to find the min number in a list.
#first function should compare each number to every other number.
#2nd function should be linear O(n)

def findMin(alist):
  overallmin = alist[0]
  for i in alist:
    print('i', i)
    issmallest = True
    for j in alist:
      print('j', j)
      if i > j:
        issmallest = False
        print('overallmin', overallmin)
    if issmallest:
        overallmin = i
  return overallmin

# print(findMin([0,4,-1]))

def func1(input):
  a = input[0]
  for idx in range(len(input)):
    if a > input[idx]:
      a = input[idx]
  return a

def func2(input):
  return min(input)
# print(func2([-1,2,-10,4]))

# [for idx in range(26) print((ord(idx) - ord('a')))]


#2.6 - lists

def test1():
  l = []
  for i in range(100):
    l.append(i)
  return l

def test2():
  l = [i for i in range(100)]
  return l


def test3():
  l = []
  for i in range(100):
    l = l + [i]
  return l

def test4():
  l = list(range(100))
  return l

def test5():
  return list(range(100))


import timeit



















