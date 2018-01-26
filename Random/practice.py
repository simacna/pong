def cracklePop():
    num = 1
    for num in range(1,100):
        if num%3==0 and num%5==0:
            print("CracklePop")
            
        elif (num%5==0):
            print("Pop")
        elif (num%3==0):
            print("Crackle")
            
        else:
            print (num)

cracklePop();
