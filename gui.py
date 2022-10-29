from tkinter import *

myWindow = Tk()
myWindow.title("Samak Window")
myWindow.geometry("420x200+200+60")


# Menu
myMenu = Menu(myWindow)
myMenu.add_cascade(label='File')
myMenu.add_cascade(label='Edit')
myMenu.add_cascade(label='Format')
myMenu.add_cascade(label='Run')
myMenu.add_cascade(label='Help')
# Adding menu to window
myWindow.config(menu=myMenu, bg="lightgray")


def copyName():
    name = nameE.get()
    copyNameL = Label(text=name, bg='gray', fg='white', width=15).grid(row=1, column=4)


def copyLastName():
    lastName = lastNameE.get()
    copyLastNameL = Label(text=lastName, bg='gray', fg='white', width=15).grid(row=2, column=4)


def copyAge():
    age = ageE.get()
    copyAgeL = Label(text=age, bg='gray', fg='white', width=15).grid(row=3, column=4)


def copyGender():
    gender = genderE.get()
    copyGenderL = Label(text=gender, bg='gray', fg='white', width=15).grid(row=4, column=4)


nameE = StringVar()
lastNameE = StringVar()
ageE = StringVar()
genderE = StringVar()

# mainP = Label(myWindow, width=800, height=30, bg='red')
# mainL = Label(text='Enter Your Details', font='20').grid(row=0, column=0, sticky='e')

# secP = Label(myWindow, width=100, height=200)
nameL = Label(text="Name", bg='gray', fg='white', width=15).grid(row=1, column=0)
lastNameL = Label(text="Last Name", bg='gray', fg='white', width=15).grid(row=2, column=0)
ageL = Label(text="Age", bg='gray', fg='white', width=15).grid(row=3, column=0, )
genderL = Label(text="Gender", bg='gray', fg='white', width=15).grid(row=4, column=0)

# Text boxes
nameText = Entry(textvariable=nameE).grid(row=1, column=1)
lNameText = Entry(textvariable=lastNameE).grid(row=2, column=1)
ageText = Entry(textvariable=ageE).grid(row=3, column=1)
genderText = Entry(textvariable=genderE).grid(row=4, column=1)

# Buttons
nameB = Button(text='Copy name', bg='gray', fg='white', command=copyName).grid(row=1, column=2)
lNameB = Button(text='Copy last name', bg='gray', fg='white', command=copyLastName).grid(row=2, column=2)
ageB = Button(text='Copy age', bg='gray', fg='white', command=copyAge).grid(row=3, column=2)
genderB = Button(text='Copy gender', bg='gray', fg='white', command=copyGender).grid(row=4, column=2)

myWindow.mainloop()
