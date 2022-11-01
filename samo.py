# import time
#
# t = time.asctime()
# print(t)
#
# print(time.time())
# print(time.localtime(1665892444.2473166))
#
# for a in range(1,6):
#     print("\n")
#     input("Press Enter:")
#     for b in range(1,11):
#         time.sleep(0.5)
#         print(b, " x ", a, " = ", a*b)
#
#
# writeFileObj = open("D:/Paython Zarif_B/python_txt/file1.txt", 'w')
# writeFileObj.write("This file was created by Python code, \n a few seconds before!")
# print("\nFile creation and write was successful!\nPath: D:/Paython Zarif_B/python_txt/file1.txt\n")
# writeFileObj.close()

#
# readFileObj = open("D:/Paython Zarif_B/python_txt/file1.txt", 'r')
# print("Read from file was successful, your text here:")
# txt=readFileObj.read()
# print(txt)
# readFileObj.close()
#
import os


# os.rename("D:/Paython Zarif_B/python_txt/sam.txt", "D:/Paython Zarif_B/python_txt/samuilla_hWardak.txt")

# # print current directory
# print(os.getcwd())
# # Change current directory
# os.chdir("D:/Paython Zarif_B/python_txt")
# print(os.getcwd())
#
# # Make a folder
# os.mkdir("D:/Paython Zarif_B/python_txt/Samak_Folder")
# # Remove Directory
# os.removedirs("D:/Paython Zarif_B/python_txt/Samak_Folder")

# try:
#     100/0
# except:
#     print("Not dividable")

class Animal:
    name = "ani2"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{} can eat".format(self.name))


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("{} can walk".format(self.name))


myDog = Dog("max")
myDog.eat()
myDog.walk()
myDog.name="Maxi"
myDog.eat()
myDog.walk()

anim1 = Animal("cat")
anim1.eat()



