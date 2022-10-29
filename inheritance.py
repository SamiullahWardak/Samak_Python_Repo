class Parent:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def property():
        print('This is parent property!')

class Child(Parent):
    def __init__(self, name, salary, status, playing):
        super().__init__(name, salary)
        self.status = status
        self.playing = playing
        
    def property():
        print('This is child property!')


obj = Child('Sami', 50000, 'Single', 'Play with code!')
print("My name is ", obj.name, ". My salary is ", obj.salary, ".\nI am ", obj.status, 
      "And my property: {}".format(obj.property), obj.playing)
