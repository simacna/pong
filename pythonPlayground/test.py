# *arg argument
def args(arg1, *arg):
  print("first arg1", arg1)
  for args in arg:
    print("yo i'm another arg", args)

# ar = args(1, 'two', 3)
capitals = {'WA-K': 'Tacoma-V', 'OR-K': 'Salem-V'}
# **kwargs
# print(capitals['OR-K'])
def args(a, **kwargs):
  for key, value in kwargs:
    print('i am ', key, value)

def a(kw):
  for k in kw:
    print(k," .. .. ",kw[k])

a(capitals)

