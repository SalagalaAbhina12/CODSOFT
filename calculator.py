import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def evaluate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x400") 
window.configure(bg="#9770e6") 

entry = tk.Entry(window, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=20, ipady=20, sticky="nsew")
entry.configure(bg="#ab96d6")  

button_bg = "#ab96d6"
button_fg = "white"
button_font = ("Arial", 15)


buttons = [
    'AC', 'DEL', '.', '/',
    '1', '2', '3', '*',
    '4', '5', '6', '-',
    '7', '8', '9', '+',
    '0', '00', '='  
]


for i in range(5):
    window.grid_rowconfigure(i, weight=1)

for j in range(4):
    window.grid_columnconfigure(j, weight=1)


row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        button = tk.Button(window, text=button, padx=10, pady=10, command=evaluate, bg=button_bg, fg=button_fg, font=button_font)
    elif button == 'AC':
        button = tk.Button(window, text=button, padx=10, pady=10, command=clear, bg=button_bg, fg=button_fg, font=button_font)
    elif button == 'DEL':
        button = tk.Button(window, text=button, padx=10, pady=10, command=delete, bg=button_bg, fg=button_fg, font=button_font)
    else:
        button = tk.Button(window, text=button, padx=10, pady=10, command=lambda b=button: button_click(b), bg=button_bg, fg=button_fg, font=button_font)

    button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


window.mainloop()
