from tkinter import *
from typing import Match

root = Tk()
root.title("Simple Calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

def button_click(number):
    curr = e.get()
    e.delete(0,END)
    e.insert(0, str(curr) + str(number)) # to enter a 2 or more digits number

def buttonClear():
    e.delete(0,END)

def buttonAdd():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    e.delete(0,END)

def buttonSubtract():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0,END)

def buttonMultiply():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    e.delete(0,END)

def buttonDivide():
    first_num = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    e.delete(0,END)



def buttonEqual():
    second_num = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,f_num + int(second_num))
    elif math == 'subtraction':
        e.insert(0,f_num - int(second_num))
    if math == 'multiplication':
        e.insert(0,f_num * int(second_num))
    if math == 'division':
        e.insert(0,f_num / int(second_num))
# Define Buttons

button_1 = Button(root,text="1",padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=40, pady=20, command=lambda: button_click(0))

button_addition = Button(root,text="+",padx=40, pady=20, command=buttonAdd)
button_equal = Button(root,text="=",padx=89, pady=20, command= buttonEqual)
button_clear = Button(root,text="Clear",padx=79, pady=20,command=buttonClear)

button_subtract = Button(root,text="-",padx=41,pady=20,command=buttonSubtract)
button_multiply = Button(root,text="*",padx=40,pady=20,command=buttonMultiply)
button_divide = Button(root,text="/",padx=41,pady=20,command=buttonDivide)
# put buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_addition.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()
