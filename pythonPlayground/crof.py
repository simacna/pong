thisIsABoolean = True

bullets = [thisisavariable for thisisavariable in range(10)]
# print(bullets)

def lengthRequirement(passwordLength):
  pwlen = len(passwordLength)

  if pwlen < 6:
    print("Password too short, please make psw longer than 6")
  else:
    print("your password is saved, than you")


print(lengthRequirement("sina"))

