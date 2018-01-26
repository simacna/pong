class Dog():
    cry = "bark"
    
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        return "I am " + self.name + "a dog!" + cry
        
Lassie = Dog("lassie")

one = Lassie.greeting
print(one)
