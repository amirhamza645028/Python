import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Variable to store the screen content
screen_var = tk.StringVar()
screen_var.set("")

# Create the display screen
screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", justify="right", bd=10, relief=tk.RIDGE)
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons and arrange them
frame = tk.Frame(root)
frame.pack()

for i, button in enumerate(buttons):
    btn = tk.Button(frame, text=button, font="Arial 15 bold", padx=20, pady=20)
    btn.grid(row=i//4, column=i%4, sticky="nsew")
    btn.bind("<Button-1>", click)

# Run the application
root.mainloop()
