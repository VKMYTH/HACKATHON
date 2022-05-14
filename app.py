import tkinter as tk
from tkinter import ttk
import json

root = tk.Tk()
root.geometry("400x360")
root.configure(bg="light blue")
s = ttk.Style(root)
s.configure('TNotebook', tabposition='n')

tk.Label(root, text="Accounts Corp.", bg="light blue", font=('bold')).pack(side="top")


tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Sign In")
tabControl.add(tab2, text='Your Account')

tabControl.pack(expand=1, fill="both")

info_file = 'info.json'


def analyze():
    if len(user_name.get()) > 0 and len(user_address.get()) > 0 and len(user_number.get()) > 0 and len(user_email.get()) > 0:
        submitting_info_message = f"Thank you for submitting your information, {user_name.get()}, to Account Corp. \n You can proceed to the Accounts Page."
        save_into_file([user_name.get(), user_address.get(), user_number.get(), user_email.get()])
        for label in tab1.children.values(): label.destroy()
        tk.Label(tab1, text=submitting_info_message, wraplength=500).pack(side="bottom")
    else:
        raise ValueError(tk.Label(tab1, text="No Information Provided; Please Try Again").pack(side="bottom"))


user_name = tk.StringVar()

name_label = tk.Label(tab1, text="Name: ", wraplength=500, bg="light blue")
name_label.pack(side="top", padx=(0, 10))
name_entry = tk.Entry(tab1, width=10, textvariable=user_name, bg="lightblue")
name_entry.pack(side="top")
name_entry.focus()


user_address = tk.StringVar()

address_label = tk.Label(tab1, text="Address: ", bg="light blue")
address_label.pack(side="top", padx=(0, 10))
address_entry = tk.Entry(tab1, width=15, textvariable=user_address, bg="light blue")
address_entry.pack(side="top")
address_entry.focus()

user_number = tk.StringVar()

number_label = tk.Label(tab1, text="Phone Number: ", bg="light blue")
number_label.pack(side="top", padx=(0, 10))
number_entry = tk.Entry(tab1, width=15, textvariable=user_number, bg="light blue")
number_entry.pack(side="top")
number_entry.focus()

user_email = tk.StringVar()

email_label = tk.Label(tab1, text="Email Address: ", bg="light blue")
email_label.pack(side="top", padx=(0, 10))
email_entry = tk.Entry(tab1, width=15, textvariable=user_email, bg="light blue")
email_entry.pack(side="top")
email_entry.focus()

submit_button = tk.Button(tab1, text="Submit Information", command=analyze, bg="light blue")
submit_button.pack(side="top", fill="x", expand=True)


def initialize():
    with open(info_file, 'w') as file:
        json.dump([], file)


def save_into_file(credentials):
    with open('info.txt', 'w') as writer:
        for word in credentials:
            writer.write(word)


def get_info_from_file():
    with open('info.txt', 'r') as reader:
        return reader.readlines()


root.mainloop()


