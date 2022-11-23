# mlist=["sami", 55, 33, 44, 33, 22, "Wardak"]
# print(id(mlist))
# mlist.reverse()
# print(id(mlist))    # (id)s are the same for both
# print(mlist)

# mlist = [2, 3, 4, 66, 44, 107, 33, 12]
# def fov(x):
#     if x % 2 == 1:
#         return True
#     else:
#         return False
# mlist2 = list(filter(fov, mlist))
# mlist2.sort(reverse=True)
# print(mlist2)

# from functools import reduce
# print(reduce(lambda x, y: x + y, list(range(1, 100))))

# from tkinter import *
# def red():
#     root.config(bg="#add00a")
# def green():
#     root.config(bg="#bbbbbb")
# root = Tk()
# root.geometry("400x200")
# root.title("Samak Wardak")
# btn = Button(root, text="My_Button", font="Arial 8", fg="white", bg="gray", width="20", height="2", command=red)
# btn.pack()
# btn1 = Button(root, text="Your_Button", font="Arial 8", fg="white", bg="gray", width="20", height="2", command=green)
# btn1.place(x=200, y=100)
# btn1.pack()
# root.mainloop()

name1 = "Sami"
name2 = "Samak"
print('Hello, %s this is me, %s' % (name1, name2))
print(f'Hello, {name2} this is me, {name1}')
print("%s samsung %s" %(name1, name2))