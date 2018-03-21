def matches(inp):
  first_half = len(inp)//2
  first_half_list = inp[0:first_half]
  second_half_list = inp[first_half:]
  return second_half_list

print(matches([1,1,2,2]))