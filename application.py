import tkinter as tk
from tkinter import messagebox


def add_task():                                        # Function to add a task
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def mark_complete():                                             # Function to mark a task as complete
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, {'bg': 'light green'})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

# Function to delete a selected task
def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to clear the entire task list
def clear_all():
    response = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if response:
        task_list.delete(0, tk.END)

# Create the main window
app = tk.Tk()
app.title("To-Do List")

# Create a task entry field
task_entry = tk.Entry(app)
task_entry.pack(pady=10, padx=10, fill=tk.X)

# Create an "Add Task" button
add_button = tk.Button(app, text="Add Task", command=add_task, bg="blue")
add_button.pack(pady=5, padx=10, fill=tk.X)

# Create a task list
task_list = tk.Listbox(app, selectbackground="lightyellow", selectmode=tk.SINGLE, height=10)
task_list.pack(padx=10, pady=5, fill=tk.X)

# Create a "Mark Complete" button
complete_button = tk.Button(app, text="Mark Complete", command=mark_complete, bg="green")
complete_button.pack(pady=5, padx=10, fill=tk.X)

# Create a "Delete Task" button
delete_button = tk.Button(app, text="Delete Task", command=delete_task, bg="blue")
delete_button.pack(pady=5, padx=10, fill=tk.X)

# Create a "Clear All" button
clear_button = tk.Button(app, text="Clear All", command=clear_all, bg="blue")
clear_button.pack(pady=5, padx=10, fill=tk.X)

# Start the Tkinter main loop
app.mainloop()
