import time
import tkinter as tk

start_time = time.time()

def click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

window = tk.Tk()
window.geometry("300x350")
window.title("Calculator")
window.configure(bg="white")

display = tk.Entry(window, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

for number in range(10):
    row = number // 3 + 1
    column = number % 3

    button = tk.Button(
        window,
        text=str(number),
        font=("Arial", 18),
        command=lambda n=number: click(n),
    )
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

for column in range(3):
    window.grid_columnconfigure(column, weight=1)

for row in range(5):
    window.grid_rowconfigure(row, weight=1)

print(
    "Time taken to load the program:",
    round(time.time() - start_time, 5),
    "seconds"
)

window.mainloop()