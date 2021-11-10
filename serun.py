from tkinter import *
import tkinter.messagebox as mbx
import mysql.connector as mysql

# global variable  
already_loged_in = "no"
loged_in_id = "none"

# functions
# TODO: functions pe kam krna hai

def login():
    if login_id.get()=="" or login_password.get()=="":
        mbx.showerror(title="WARNING", message="LOG DETAILS ARE EMPTY")
    print(f"{login_id.get()}--{login_password.get()}")
    if login_id.get() == "ramu":
        login_frame.destroy()

def logout():
    for widgets in root.winfo_children():
      widgets.destroy()
    m1.add_command(label="Logout", command=logout)
    m1.add_command(label="Logout and close", command=quit)
    root.config(menu=mainmenu)
    login_frame = Frame(root, bg="#075E54", borderwidth=6, relief=SUNKEN)
    login_frame.pack(side=TOP, fill="both")
    Label(login_frame, text="LOGIN YOUR CREDENTIALS", font="bold 10", pady=5).grid(row=1, column=2)
    Label(login_frame, text="Enter Login ID", font="bold 10",bg="#075E54", foreground="white", pady=15, padx=10).grid(row=2, column=0)
    Label(login_frame, text="Enter Login Password",bg="#075E54", foreground="white", font="bold 10", pady=15, padx=10).grid(row=3, column=0)
    login_id_entry = Entry(login_frame, textvariable=login_id).grid(row=2, column=1)
    login_password_entry = Entry(login_frame, textvariable=login_password).grid(row=3, column=1)
    Button(login_frame, text="LOGIN", command=login, pady=4, padx=20, font="blue 12").grid(row=4, column=2)
    

# root
root = Tk()
root.geometry("800x700+400+25")
root.title("BIT ADMINISTRATION")
root.resizable(False,False)

# var  
login_id = StringVar()
login_password = StringVar()

# Menu
mainmenu = Menu(root)
m1 = Menu(mainmenu)



# menu 
m1.add_command(label="Logout", command=logout)
m1.add_command(label="Logout and close", command=quit)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="Log", menu=m1)
# mainmenu.add_command(label="Quit", command=quit)


login_frame = Frame(root, bg="#075E54", borderwidth=6, relief=SUNKEN)
Label(login_frame, text="LOGIN YOUR CREDENTIALS", font="bold 10", pady=5).grid(row=1, column=2)
Label(login_frame, text="Enter Login ID", font="bold 10",bg="#075E54", foreground="white", pady=15, padx=10).grid(row=2, column=0)
Label(login_frame, text="Enter Login Password",bg="#075E54", foreground="white", font="bold 10", pady=15, padx=10).grid(row=3, column=0)
login_id_entry = Entry(login_frame, textvariable=login_id).grid(row=2, column=1)
login_password_entry = Entry(login_frame, textvariable=login_password).grid(row=3, column=1)
Button(login_frame, text="LOGIN", command=login, pady=4, padx=20, font="blue 12").grid(row=4, column=2)
login_frame.pack(side=TOP, fill="both")




# mainloop 
root.mainloop()
