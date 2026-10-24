
import time
import tkinter as tk

start_time = time.time()


def click(number):
    current = display.get()
    display.insert(tk.END, str(number))


def operation(operator):
    current = display.get()

    if current and current[-1] in "+-*/":
        display.delete(len(current) - 1, tk.END)

    display.insert(tk.END, operator)


def calculate():
    expression = display.get()

    try:
        # Allow only calculator characters
        if not expression or any(
            char not in "0123456789.+-*/() " for char in expression
        ):
            raise ValueError

        result = eval(expression, {"__builtins__": {}}, {})
        display.delete(0, tk.END)
        display.insert(0, str(result))

    except (ValueError, ZeroDivisionError, SyntaxError, TypeError):
        display.delete(0, tk.END)
        display.insert(0, "Error")


def backspace():
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)


window = tk.Tk()
window.geometry("450x450")
window.title("Calculator")
window.configure(bg="white")

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right"
)
display.grid(
    row=0, column=0, columnspan=4,
    padx=5, pady=5, sticky="nsew"
)

# Number buttons: 0 to 9
for number in range(10):
    row = number // 3 + 1
    column = number % 3

    button = tk.Button(
        window,
        width=5,
        height=2,
        text=str(number),
        font=("Arial", 12),
        command=lambda n=number: click(n)
    )

    button.grid(
        row=row, column=column,
        padx=5, pady=5, sticky="nsew"
    )

# Operator buttons
for index, operator in enumerate(["+", "-", "*", "/"]):
    button = tk.Button(
        window,
        width=5,
        height=2,
        text=operator,
        font=("Arial", 12),
        command=lambda op=operator: operation(op)
    )

    button.grid(
        row=index + 1, column=3,
        padx=5, pady=5, sticky="nsew"
    )

# Equals button
equals_button = tk.Button(
    window,
    text="=",
    font=("Arial", 12),
    command=calculate
)
equals_button.grid(
    row=5, column=3,
    padx=5, pady=5, sticky="nsew"
)

# Delete button: clear everything
delete_button = tk.Button(
    window,
    width=10,
    text="Delete",
    command=lambda: display.delete(0, tk.END),
    font=("Arial", 10)
)
delete_button.grid(
    row=5, column=0,
    padx=5, pady=5, sticky="nsew"
)

# Backspace button: remove last character
backspace_button = tk.Button(
    window,
    width=10,
    text="Backspace",
    command=backspace,
    font=("Arial", 10)
)
backspace_button.grid(
    row=5, column=1,
    padx=5, pady=5, sticky="nsew"
)

# Configure layout resizing
for column in range(4):
    window.grid_columnconfigure(column, weight=1)

for row in range(6):
    window.grid_rowconfigure(row, weight=1)

print(
    "Time taken to load the program:",
    round(time.time() - start_time, 5),
    "seconds"
)

window.mainloop()
