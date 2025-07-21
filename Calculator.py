import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(button_text))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error (div by 0)")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# Calculator window's layout
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")

entry = tk.Entry(root, width=20, font=("Arial", 24), bd=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# arranging the button for calculator
buttons = [
    ('C', '(', ')', '='),
    ('7', '8', '9', '+'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '*'),
    ('0', '%', '//', '/'),
]

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        action = (
            calculate if char == '=' else
            clear if char == 'C' else
            lambda ch=char: click(ch)
        )
        tk.Button(root, text=char, width=5, height=2, font=("Arial", 18),
                  command=action).grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
    
