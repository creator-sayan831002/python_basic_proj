import tkinter as tk
from tkinter import messagebox
import csv
import os

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    if name and phone and email:
        contacts.append((name, phone, email))
        update_listbox()
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        save_contacts_to_csv()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def delete_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        update_listbox()
        save_contacts_to_csv()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

def update_listbox():
    listbox_contacts.delete(0, tk.END)
    for idx, (name, phone, email) in enumerate(contacts, start=1):
        listbox_contacts.insert(tk.END, f"{idx}. {name} | {phone} | {email}")

def save_contacts_to_csv():
    with open("contacts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])
        writer.writerows(contacts)

def load_contacts_from_csv():
    if os.path.exists("contacts.csv"):
        with open("contacts.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) == 3:
                    contacts.append(tuple(row))
        update_listbox()

# --- LIGHT THEME COLORS ---
BG_LIGHT = "#f5f5f5"
BG_FRAME = "#e0e0e0"
BG_ENTRY = "#ffffff"
BG_LISTBOX = "#ffffff"
FG_DARK = "#222222"
FG_ENTRY = "#333399"
FG_LISTBOX = "#00695c"
BORDER_COLOR = "#bdbdbd"
BTN_ADD_BG = "#64b5f6"
BTN_ADD_ACTIVE = "#1976d2"
BTN_DEL_BG = "#ff8a65"
BTN_DEL_ACTIVE = "#d84315"

root = tk.Tk()
root.title("Contact Book")
root.configure(bg=BG_LIGHT)

frame_contacts = tk.Frame(root, bg=BG_FRAME, highlightbackground=BORDER_COLOR, highlightthickness=2)
frame_contacts.pack(pady=15)

listbox_contacts = tk.Listbox(
    frame_contacts, height=10, width=60, font=("Segoe UI", 11, "bold"),
    bg=BG_LISTBOX, fg=FG_DARK, selectbackground="#b3e5fc", selectforeground=FG_LISTBOX,
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
listbox_contacts.pack(side=tk.LEFT, padx=(0, 10))

scrollbar_contacts = tk.Scrollbar(frame_contacts, bg=BG_FRAME, troughcolor=BG_FRAME)
scrollbar_contacts.pack(side=tk.RIGHT, fill=tk.Y)

listbox_contacts.config(yscrollcommand=scrollbar_contacts.set)
scrollbar_contacts.config(command=listbox_contacts.yview)

frame_entries = tk.Frame(root, bg=BG_LIGHT)
frame_entries.pack(pady=(0, 10))

label_name = tk.Label(frame_entries, text="Name:", bg=BG_LIGHT, fg=FG_DARK, font=("Segoe UI", 10, "bold"))
label_name.grid(row=0, column=0, padx=5, pady=2, sticky="e")
entry_name = tk.Entry(frame_entries, width=20, font=("Segoe UI", 11, "bold"),
                      bg=BG_ENTRY, fg=FG_ENTRY, insertbackground=FG_ENTRY,
                      borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2)
entry_name.grid(row=0, column=1, padx=5, pady=2)

label_phone = tk.Label(frame_entries, text="Phone:", bg=BG_LIGHT, fg=FG_DARK, font=("Segoe UI", 10, "bold"))
label_phone.grid(row=0, column=2, padx=5, pady=2, sticky="e")
entry_phone = tk.Entry(frame_entries, width=20, font=("Segoe UI", 11, "bold"),
                       bg=BG_ENTRY, fg=FG_ENTRY, insertbackground=FG_ENTRY,
                       borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2)
entry_phone.grid(row=0, column=3, padx=5, pady=2)

label_email = tk.Label(frame_entries, text="Email:", bg=BG_LIGHT, fg=FG_DARK, font=("Segoe UI", 10, "bold"))
label_email.grid(row=0, column=4, padx=5, pady=2, sticky="e")
entry_email = tk.Entry(frame_entries, width=25, font=("Segoe UI", 11, "bold"),
                       bg=BG_ENTRY, fg=FG_ENTRY, insertbackground=FG_ENTRY,
                       borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2)
entry_email.grid(row=0, column=5, padx=5, pady=2)

frame_buttons = tk.Frame(root, bg=BG_LIGHT)
frame_buttons.pack(pady=(0, 20))

button_add_contact = tk.Button(
    frame_buttons, text="Add Contact", width=18, command=add_contact,
    bg=BTN_ADD_BG, fg=FG_DARK, font=("Segoe UI", 10, "bold"),
    activebackground=BTN_ADD_ACTIVE, activeforeground=FG_LISTBOX,
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
button_add_contact.pack(side=tk.LEFT, padx=(40, 10))

button_delete_contact = tk.Button(
    frame_buttons, text="Delete Contact", width=18, command=delete_contact,
    bg=BTN_DEL_BG, fg=FG_DARK, font=("Segoe UI", 10, "bold"),
    activebackground=BTN_DEL_ACTIVE, activeforeground=FG_LISTBOX,
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
button_delete_contact.pack(side=tk.LEFT, padx=(10, 40))

def exit_app():
    root.destroy()

button_exit = tk.Button(
    root, text="Exit", width=20, command=exit_app,
    bg="#23272e", fg="#ff5555", font=("Segoe UI", 10, "bold"),
    activebackground="#181a1b", activeforeground="#ff5555",
    borderwidth=2, relief="groove", highlightbackground=BORDER_COLOR, highlightthickness=2
)
button_exit.pack(side=tk.BOTTOM, pady=(0, 20))

load_contacts_from_csv()

root.mainloop()