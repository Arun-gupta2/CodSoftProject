import tkinter as tk
from tkinter import messagebox
def add_task():
    task=task_entry.get()
    if task:
        Task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","please enter a task")
            
def delete_task():
    selected_task=Task_listbox.curselection()
    if selected_task:
        Task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("warning","please select task to delete")
    
root=tk.Tk()
root.title("to-do list app")
tk.Label(root,text="TO_DO LIST APP",font=("helvetica",20)).pack()
task_entry=tk.Entry(root,width=50,font=("helvetica",12),bd=5)
task_entry.pack(pady=20)
add_buuton=tk.Button(root,text="Add task",command=add_task)
add_buuton.pack(pady=8)
Task_listbox=tk.Listbox(root,font=("arial" ,14),height=13,width=40)
Task_listbox.pack(pady=10)
delete_button=tk.Button(root,text="Delete task",command=delete_task)
delete_button.pack(pady=5)
exit_button=tk.Button(root,text="Exit",command=root.destroy)
exit_button.pack(pady=5)
root.mainloop()
