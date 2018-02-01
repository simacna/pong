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
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

# print(anagramSolution1('abcd','dcba'))
