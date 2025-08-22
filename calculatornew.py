import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            messagebox.showerror("Math error", "Cannot divide by zero.")
        else:
            result.set(float(entry1.get()) / denominator)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

# Create main window
window = tk.Tk()
window.title("Simple Calculator")

# Number 1 input
tk.Label(window, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=5)

# Number 2 input
tk.Label(window, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Operation buttons
tk.Button(window, text="Add", width=10, command=add).grid(row=2, column=0, pady=10)
tk.Button(window, text="Subtract", width=10, command=subtract).grid(row=2, column=1, pady=10)
tk.Button(window, text="Multiply", width=10, command=multiply).grid(row=3, column=0, pady=10)
tk.Button(window, text="Divide", width=10, command=divide).grid(row=3, column=1, pady=10)

# Result display
result = tk.StringVar()
tk.Label(window, text="Result:").grid(row=4, column=0, padx=10, pady=10)
tk.Label(window, textvariable=result).grid(row=4, column=1, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
