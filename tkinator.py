import time
start_time = time.time()
import os
from tkinter import *
count=0
def click():#This is a function that will be called when the button is clicked
    global count
    count+=1
    print("Button clicked", count, "times")#This is a function that will print the number of times the button has been clicked

window = Tk()#This creates a window using the Tkinter library
window.geometry("450x450")#This sets the size of the window
window.title("Calculator")#This sets the title of the window
window.configure(bg="white")
label = Label(window, text="Calculator", 
              font=("Arial", 20, "bold"), 
              bg="white", 
              fg="black")#This is a function that will create a label with the text "Calculator" and set the font, background color, and foreground color
label.pack(pady=10)
button=Button(window, text="click me",
              command=click,
              font=("Comic Sans MS", 25))#This is a function called button that is used to click to perform a function and can modify the button
button.pack(pady=10)
entry = Entry(window, width=30, font=("Arial", 20))#This is a function that will create an entry box where the user can input text
entry.pack(pady=10)
submit_button = Button(window, text="Submit", command=lambda: print("You entered:", entry.get()), font=("Comic Sans MS", 20))#This is a function that will create a button that will print the text entered in the entry box when clicked
submit_button.pack(pady=10)
delete_button = Button(window, text="Delete", command=lambda: entry.delete(0, END), font=("Comic Sans MS", 20))#This is a function that will create a button that will delete the text entered in the entry box when clicked
delete_button.pack(pady=10)
backspace_button = Button(window, text="Backspace", command=lambda: entry.delete(len(entry.get())-1, END), font=("Comic Sans MS", 20))#This is a function that will create a button that will delete the last character entered in the entry box when clicked
backspace_button.pack(pady=10)
print("Time taken to load the program: ", round(time.time() - start_time, 5), "seconds")#This is a function that will print the time taken to load the program
window.mainloop()#This is a function that will keep the window open until the user closes it