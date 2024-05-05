import tkinter as tk
from tkinter import messagebox
import db_task

db = db_task.taskDB()

task_no=task_title=task_desc=None


def content_in_task():
    rows = db.display_values()
    tasks.config(state="normal")
    tasks.delete("1.0", "end")
    for data in rows:
        tasks.insert(tk.END,f"{data[0]}. {data[1]}: {data[2]}")
    tasks.config(state="disabled")
def clear_all_in_task():
    db.delete_all()
def new_task():
    global task_no,task_title,task_desc
    new_window = tk.Toplevel(root)
    new_window.title("Add New Task")

    # Add widgets to the new window
    tk.Label(new_window, text="Enter Title:").grid(row=0,column=0,sticky='w')
    task_title = tk.Entry(new_window)
    task_title.grid(row=0,column=1)

    tk.Label(new_window, text="Enter Task No:").grid(row=1,column=0,sticky='w')
    task_no = tk.Entry(new_window)
    task_no.grid(row=1,column=1)

    tk.Label(new_window,text="Descrip").grid(row=2,column=0,sticky='w')
    task_desc = tk.Text(new_window,height=10,width=40)
    task_desc.grid(row=3,column=0,columnspan=3)

    tk.Button(new_window,text="OK",command=lambda: save_new_data(new_window)).grid(row=4,column=0,columnspan=3)
    

def save_new_data(win):
    db.insert_into_table(task_no.get(),task_title.get(),task_desc.get("1.0", "end"))
    win.destroy()
   

def del_task():
    del_tas = tk.Toplevel(root)
    del_tas.title("Delete Task")

    tk.Label(del_tas,text="Enter your Task id").grid(column=0,row=0)
    task_id = tk.Entry(del_tas)
    task_id.grid(row=1,column=0,columnspan=3)

    del_btn = tk.Button(del_tas,text="Delete",command=lambda:del_from_db(del_tas,task_id.get()))
    del_btn.grid(row=2,column=0)

    
def del_from_db(win,id):
    db.delete_row(id)
    win.destroy()

def cls_all():
    intention = messagebox.askquestion("Are you Sure")
    if intention == "no":
        pass
    elif intention == "yes":
        tasks.config(state="normal")
        clear_all_in_task()
        tasks.insert(tk.END,content_in_task())
        tasks.config(state="disabled")

root = tk.Tk()


main_frame = tk.Frame(root, borderwidth=2,relief='ridge')
main_frame.pack(padx=20,pady=20)

tk.Label(main_frame,text="Your Tasks").grid(row=0,column=0,sticky='w')

tasks = tk.Text(main_frame,height=10,width=40)
tasks.grid(row=1,column=0,columnspan=5)
content_in_task()

clear_button = tk.Button(main_frame,text="Clear_All",command=cls_all).grid(row=2,column=0)

add_button = tk.Button(main_frame,text="Add New Task",command=new_task).grid(row=2,column=1)

del_button = tk.Button(main_frame,text="Delete Task",command=del_task).grid(row=2,column=2)

refresh_btn = tk.Button(main_frame,text="Refresh",command=content_in_task).grid(row=2,column=3)

root.mainloop()
db.close_connection()