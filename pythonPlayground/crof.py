# thisIsABoolean = True

# bullets = [thisisavariable for thisisavariable in range(10)]
# # print(bullets)

# def lengthRequirement(passwordLength):
#   pwlen = len(passwordLength)

#   if pwlen < 6:
#     print("Password too short, please make psw longer than 6")
#   else:
#     print("your password is saved, than you")


# print(lengthRequirement("sina"))

# a = [x for x in range(3)]

# c = a *3
# print(c)
# myList = [1,2,3,4]
# A = [myList]*3
# print(A)
# myList[2]=45
# print(A)
# A[0][1] = 20
# print(A)
# myList = [0] 
# C = [myList] * 6
# print(C)

# myList = [1024, 3, True, 6.5]
# myList.append(False) #[1024, 3, True, 6.5, False]
# myList.insert(2, 4.5) #[1024, 3, 2, True, 6.5, False]
class Length:

    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }
    
    def __init__(self, value, unit = "m" ):
        self.value = value
        self.unit = unit
    
    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]
    
    def __add__(self, other):
        l = self.Converse2Metres() + other.Converse2Metres()
        return Length(l / Length.__metric[self.unit], self.unit )
    
    def __str__(self):
        return str(self.Converse2Metres())
    
    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"

# if __name__ == "__main__":
#     x = Length(4)
#     print(x)
#     y = eval(repr(x))

#     z = Length(4.5, "yd") + Length(1)
#     print(repr(z))
#     print(z)


capitals = {'a':1, 'b':2, 'c':3}
# print('a' in capitals)
# for i in capitals:
#   # print(capitals[i], "is number", i)
#   #print(i)  - prints keys, i.e. a, b, c
#   print(capitals.items())

# a = list(capitals.values())
# print(a[1])

