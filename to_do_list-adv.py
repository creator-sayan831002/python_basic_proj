import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

def add_task():
    task = entry_task.get()
    if task and task != "Enter your task here...":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append((task, now))
        update_listbox()
        entry_task.delete(0, tk.END)
        entry_task.insert(0, "Enter your task here...")
        entry_task.config(fg=FG_ENTRY)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox_tasks.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for idx, (task, time) in enumerate(tasks, start=1):
        listbox_tasks.insert(tk.END, f"{idx}. {task} (Added: {time})")

# --- DARK THEME COLORS ---
BG_DARK = "#181a1b"
BG_FRAME = "#23272e"
BG_ENTRY = "#22252a"
BG_LISTBOX = "#23272e"
FG_LIGHT = "#f8f8f2"
FG_ENTRY = "#f1fa8c"
FG_LISTBOX = "#50fa7b"
BORDER_COLOR = "#44475a"
BTN_ADD_BG = "#6272a4"
BTN_ADD_ACTIVE = "#44475a"
BTN_DEL_BG = "#ff5555"
BTN_DEL_ACTIVE = "#bd2c2c"

root = tk.Tk()
root.title("To-Do List")
root.configure(bg=BG_DARK)

frame_tasks = tk.Frame(root, bg=BG_FRAME, highlightbackground=BORDER_COLOR, highlightthickness=2)
frame_tasks.pack(pady=15)

listbox_tasks = tk.Listbox(
    frame_tasks, height=10, width=50, font=("Segoe UI", 11, "bold"),
    bg=BG_LISTBOX, fg=FG_LIGHT, selectbackground="#44475a", selectforeground=FG_LISTBOX,
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
listbox_tasks.pack(side=tk.LEFT, padx=(0, 10))

scrollbar_tasks = tk.Scrollbar(frame_tasks, bg=BG_FRAME, troughcolor=BG_FRAME)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(
    root, width=40, font=("Segoe UI", 11, "bold"),
    bg=BG_ENTRY, fg=FG_ENTRY, insertbackground=FG_ENTRY,
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
entry_task.pack(pady=(0, 10))
# Set default text in the entry box
entry_task.insert(0, "Enter your task here...")

def on_entry_click(event):
    if entry_task.get() == "Enter your task here...":
        entry_task.delete(0, tk.END)
        entry_task.config(fg=FG_ENTRY)

entry_task.bind('<FocusIn>', on_entry_click)

button_add_task = tk.Button(
    root, text="Add Task", width=20, command=add_task,
    bg=BTN_ADD_BG, fg=FG_LIGHT, font=("Segoe UI", 10, "bold"),
    activebackground=BTN_ADD_ACTIVE, activeforeground=FG_LISTBOX,
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
button_add_task.pack(side=tk.LEFT, padx=(40, 10), pady=(0, 20))

button_delete_task = tk.Button(
    root, text="Delete Task", width=20, command=delete_task,
    bg=BTN_DEL_BG, fg=FG_LIGHT, font=("Segoe UI", 10, "bold"),
    activebackground=BTN_DEL_ACTIVE, activeforeground=FG_LIGHT,
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
button_delete_task.pack(side=tk.LEFT, padx=(10, 40), pady=(0, 20))

# --- Exit Button at the bottom ---
def exit_app():
    root.destroy()

button_exit = tk.Button(
    root, text="Exit", width=20, command=exit_app,
    bg="#091037", fg="#ff5555", font=("Segoe UI", 10, "bold"),
    activebackground="#1b1d28", activeforeground="#871212",
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
button_exit.pack(side=tk.BOTTOM, pady=(0, 20))

root.mainloop()