class StaticVariable:
    def __init__(self) -> None:
        print("constructor called!")
    __myName__ = "Samiullah"
    def show(self):
        print("My name in show function:", self.__myName)

# obj = StaticVariable()
# obj.show()

class Another:
    def __init__(self) -> None:
        print("Another constructor called!")
    def anotherShow(self):
        # obj1 = StaticVariable()
        # print("My another name in another show fuunction:", obj1.__myName)
        print("My another name in another show fuunction:", StaticVariable.__myName__)

objFinal = Another()
objFinal.anotherShow()

# class Parent:
#     def __init__(self):
#         print("Constructor called!")
#         print(Parent.__module__)
#         print(Parent.__name__)
#     def displayMyName(self, myName):
#         print("My name:", myName)

# obj = Parent()
# obj.displayMyName("Samiullah Wardak")

# string = str("myString")

# print(string)

# def passObjectsToThisFunction(obj1, obj2):
#     print(hasattr(obj1, 'displayMyName'))
#     print(getattr(obj2, '__init__', False))

# passObjectsToThisFunction(obj, string)

# myObjects = [obj, string]
# print(myObjects, " _____ ", type(myObjects))
