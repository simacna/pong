# *arg argument
def args(arg1, *arg):
  print("first arg1", arg1)
  for args in arg:
    print("yo i'm another arg", args)

a = args(1, 'two', 3)

# **kwargs

# def args(a, **)

