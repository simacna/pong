# *arg argument
def args(arg1, *arg):
  print("first arg1", arg1)
  for args in arg:
    print("yo i'm another arg", args)

a = args(1, 'two', 3)

# **kwargs

def args(a, **kwargs):
  for key, value in kwargs:
    print('i am ', key, value)

def a(kw):
  for k in kw:
    print(k, kw[k])
    

