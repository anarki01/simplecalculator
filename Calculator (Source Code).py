import tkinter as tkinter
import os
import sys
import pynput
from tkinter import *
from pynput.keyboard import Key, Controller


keyboard = Controller()
root = tkinter.Tk()


def one():
    keyboard.press('1') 
    keyboard.release('1')

def two():
    keyboard.press('2') 
    keyboard.release('2')

def three():
    keyboard.press('3') 
    keyboard.release('3')

def four():
    keyboard.press('4') 
    keyboard.release('4')

def five():
    keyboard.press('5') 
    keyboard.release('5')

def six():
    keyboard.press('6') 
    keyboard.release('6')

def seven():
    keyboard.press('7') 
    keyboard.release('7')

def eight():
    keyboard.press('8') 
    keyboard.release('8')

def nine():
    keyboard.press('9') 
    keyboard.release('9')

def zero():
    keyboard.press('0')
    keyboard.release('0')

def backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

def add():
    keyboard.press('+')
    keyboard.release('+')

def rootbtract():
    keyboard.press('-')
    keyboard.release('-')

def multiply():
    keyboard.press('*')
    keyboard.release('*')

def divide():
    keyboard.press('÷')
    keyboard.release('÷')

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)





def solve(event):

    
    # to solve the equation and print the rerootlts
    evaluate = eval(equation.get())
    evaluate2 = evaluate

    count=0
    while(evaluate>0):
        count=count+1
        evaluate=evaluate//10
        print("The number of digits in the number are:",count)

    
    
    if (count < 16):
        solution = tkinter.Label(answer, text=evaluate2, bg='#222a38', fg='#ffa200', font=('Monospace', 15))
        solution.grid(row=1, column=1, ipadx=100)
    else:
        tooLong = tkinter.Label(answer, text="Too Big!", bg='#222a38', fg='#ffa200', font=('Monospace', 15))
        tooLong.grid(row=1, column=1, ipadx=100)
    

    
    
    
    
    

        
#define frames
intro = tkinter.Frame(root)
buttons = tkinter.Frame(root, bg='#222a38', border=5)
operators = tkinter.Frame(root, bg='#222a38', border=5)
rootbmit = tkinter.Frame(root, bg='#222a38', border = 5)
userInput = tkinter.Frame(root, bg='#222a38', border=5)
answer = tkinter.Frame(root, bg='#222a38', border=3)
        
#define widgets
greet = tkinter.Label(intro, text="Enter Your Equation: ", font=('Monospace', 12), bg='#222a38', fg='#ffa200', pady=10)
        
# Number buttons
oneButton = tkinter.Button(buttons, text="1", bg='#364359', height=2, width=12, command=one)
twoButton = tkinter.Button(buttons, text="2", bg='#364359', height=2, width=12, command=two)
threeButton = tkinter.Button(buttons, text="3", bg='#364359', height=2, width=12, command=three)
fourButton = tkinter.Button(buttons, text="4", bg='#364359', height=2, width=12, command=four)
fiveButton = tkinter.Button(buttons, text="5", bg='#364359', height=2, width=12, command=five)
sixButton = tkinter.Button(buttons, text="6", bg='#364359', height=2, width=12, command=six)
sevenButton = tkinter.Button(buttons, text="7", bg='#364359', height=2, width=12, command=seven)
eightButton = tkinter.Button(buttons, text="8", bg='#364359', height=2, width=12, command=eight)
nineButton = tkinter.Button(buttons, text="9", bg='#364359', height=2, width=12, command=nine)
zeroButton = tkinter.Button(buttons, text="0", bg='#364359', height=2, width=12, command=zero)

# operator buttons
addition = tkinter.Button(operators, text="+", bg='#364359', height=2, width=20, command=add)
rootbtraction = tkinter.Button(operators, text="—", bg='#364359', height=2, width=20, command=rootbtract)
multiplication = tkinter.Button(operators, text="×", bg='#364359', height=2, width=20, command=multiply)
division = tkinter.Button(operators, text="÷", bg='#364359', height=2, width=20, command=divide)

# rootbmit button
rootbmitButton = tkinter.Button(rootbmit, text="SOLVE!", bg='#364359', height = 3, width=43, command=enter)

# user input
equation = tkinter.Entry(userInput, width=30, font=('Monospace', 13))
back = tkinter.Button(userInput, text="Back", font=('Monospace', 10), height=1, width=6, command=backspace)




# set root as main window
root.title("Calculator")
root.geometry('400x510')
root.iconbitmap(r'C:\Users\Rayyan\Documents\Python\calculator\favicon.ico')
root.resizable(0, 0)
root.config(bg='#222a38')

# Pack Frames
intro.pack()
userInput.pack(pady=(0,5))
answer.pack(fill='y', expand=True)
buttons.pack()
operators.pack()
rootbmit.pack()

# pack user entry
equation.grid(row=0, column=0)
back.grid(row=0, column=1, padx=10)




# pack number buttons
greet.pack()
oneButton.grid(row=0, column=0)
twoButton.grid(row=0, column=1)
threeButton.grid(row=0, column=2)
fourButton.grid(row=1, column=0)
fiveButton.grid(row=1, column=1)
sixButton.grid(row=1, column=2)
sevenButton.grid(row=2, column=0)
eightButton.grid(row=2, column=1)
nineButton.grid(row=2, column=2)
zeroButton.grid(row=3, column=1)

# pack operator buttons
addition.grid(row=0, column=0)
rootbtraction.grid(row=0, column=1)
multiplication.grid(row=1, column=0)
division.grid(row=1, column=1)

# pack rootbmit button
rootbmitButton.grid(row=0, column=0)

root.bind('<Return>', solve)


# run main window


root.mainloop()
