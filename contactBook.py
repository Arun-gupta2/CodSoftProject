import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contacts.append((name,phone))
        contact_list.insert(tk.END, f"Name: {name}, Phone: {phone}")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        contact_list.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        name = name_entry.get()
        phone = phone_entry.get()
       
        if name and phone:
            contact_list.delete(selected_index)
            contact_list.insert(selected_index, f"Name: {name}, Phone: {phone}")
            clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")
    else:
        messagebox.showwarning("Warning", "Please select a contact to update.")

def search_contact():
    search_term = search_entry.get().lower()
   
    for name,phone in contacts:
        if search_term in name.lower():
            p=phone
            isContact=True
            break
        else:
            isContact=False
        
        
        
    if isContact==True:
        messagebox.showinfo("Search results",f"name: {search_term} ,phone {p}")
    elif isContact==False:
        messagebox.showwarning("warning","no contact found")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact)

contacts = []
app = tk.Tk()
app.title("Contact Book")
tk.Label(app,text="WELCOME TO CONTACT BOOK",font=("helvetica",20)).pack()

name_label = tk.Label(app, text="Name:")
name_label.pack(pady=10)

name_entry = tk.Entry(app)
name_entry.pack()

phone_label = tk.Label(app, text="Phone:")
phone_label.pack(pady=10)

phone_entry = tk.Entry(app)
phone_entry.pack()



add_button = tk.Button(app, text="Add Contact", command=add_contact)
add_button.pack(pady=10)

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=10)

update_button = tk.Button(app, text="Update Contact", command=update_contact)
update_button.pack(pady=10)

search_label = tk.Label(app, text="Search:")
search_label.pack(pady=10)

search_entry = tk.Entry(app)
search_entry.pack()

search_button = tk.Button(app, text="Search", command=search_contact)
search_button.pack()

contact_list = tk.Listbox(app,width=32)
contact_list.pack(pady=10)

app.mainloop()
