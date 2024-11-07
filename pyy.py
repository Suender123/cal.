import tkinter as tk

# Function to update the input field with button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear current entry field
    entry.insert(tk.END, current + value)

# Function to clear the input field
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression entered
def button_equal():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, str(result))  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x600")  # Set window size

# Entry widget for displaying the input and output
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define button labels and layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create and place buttons in the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 20), command=button_equal)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 20), command=button_clear)
    else:
        button = tk.Button(root, text=text, width=5, height=3, font=("Arial", 20), command=lambda t=text: button_click(t))
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
