def min_list(list):
  min = list[0]
  for idx in list:
    if list[idx] < min:
      min = list[idx]
  return min

a = [x for x in range(10)]

print(min_list(a))
# print(range(10))