import tkinter as tk

def show_message():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Program")

# Create a label
label = tk.Label(root, text="Click the button")
label.pack()

# Create a button
button = tk.Button(root, text="Click Me", command=show_message)
button.pack()

# Run the main loop
root.mainloop()