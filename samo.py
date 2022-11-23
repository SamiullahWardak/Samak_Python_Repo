import time

# t = time.asctime() # Current time -> (Wed Nov 23 15:40:16 2022)
# print(t)

# print(time.time())
# print(time.localtime(1665892444.2473166))   # Full details of current time, Example bellow:
# print(time.localtime(time.time()))          # tm_year=2022, tm_mon=11, tm_mday=23, tm_hour=15, tm_min=44, tm_sec=1, tm_wday=2, tm_yday=327, tm_isdst=0

# for a in range(1,6):
#     print("\n")
#     input("Press Enter:")
#     for b in range(1,11):
#         time.sleep(0.5) # Sleep for half second(s) then print another line
#         print(b, " x ", a, " = ", a*b)

# writeFileObj = open("D:/Paython Zarif_B/python_txt/file1.txt", 'w')
# writeFileObj.write("This file was created by Python code, \n a few seconds before!")
# print("\nFile creation and write was successful!\nPath: D:/Paython Zarif_B/python_txt/file1.txt\n")
# writeFileObj.close()

# readFileObj = open("file.txt", 'r')
# print("Read from file was successful, your text here:")
# txt=readFileObj.read()
# print(txt)
# readFileObj.close()

import os


# os.rename("file.txt", "renamedFile.txt")
# os.rename("renamedFile.txt", "file.txt")
# print('File renamed, successfully!')

# # print current directory
# print(os.getcwd())
# # Change current directory
# os.chdir("D:")
# os.chdir("C:/Users/Samak Wardak/Pycharm_Code/Samak_Python_Repo")
# print(os.getcwd())

# # Make a folder
# os.mkdir("D:/Paython Zarif_B/python_txt/Samak_Folder")
# # Remove Directory
# os.removedirs("D:/Paython Zarif_B/python_txt/Samak_Folder")

# try:
#     100/0
# except:
#     print("Not dividable")

# class Animal:
#     name = "ani2"

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print("{} can eat".format(self.name))


# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name

#     def walk(self):
#         print("{} can walk".format(self.name))

# myDog = Dog("max")
# myDog.eat()
# myDog.walk()
# myDog.name="Maxi"
# myDog.eat()
# myDog.walk()

# anim1 = Animal("cat")
# anim1.eat()

