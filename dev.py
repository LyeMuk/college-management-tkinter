from tkinter import *
import tkinter.font as fnt
import tkinter.messagebox as mbx
import mysql.connector as mysql
from mysql.connector.errors import DatabaseError

root = Tk()
root.geometry("800x700+530+25")
root.title("BIT ADMINISTRATION")
root.resizable(False,False)

# loged data  
already_loged_in = "no"
loged_in_id = "3444"
loged_in_type = "student"
loged_uname = "BTECH-60001-19"



option_frame = Frame(root, bg="#A9A9A9", width=300, height=700, borderwidth=6, relief=SUNKEN)

def get_detail():
    pass
def update_detail():
    pass
id_to_get_detail = StringVar()
up_id = StringVar()
up_type = StringVar()
up_name = StringVar()
up_user_name = StringVar()
up_user_password = StringVar()
up_email = StringVar()
up_contact = StringVar()
up_address = StringVar()
up_year = StringVar()
up_departmant = StringVar()
show_detail_frame = Frame(root, width=500, height=700, borderwidth=8, relief=SUNKEN)
Label(show_detail_frame, text="ENTER UNIQUE ID TO GET DETAIL", font="bold 10").place(x=150, y=20)
id_to_get_detail_entry = Entry(show_detail_frame, textvariable=id_to_get_detail)
id_to_get_detail_entry.place(x=190, y=50, height="40")
id_to_get_detail_entry.insert(0,"Enter ID")
Button(show_detail_frame, text="GET DETAIL", command=get_detail, pady=4,bg="#e0e68a", padx=20).place(x=200, y=100)

detail = Frame(show_detail_frame, width=500, height=520, borderwidth=8, relief=SUNKEN)
Label(detail, text="id", font="bold 10").place(x=20, y=20)
up_id_entry = Entry(detail, textvariable=up_id)
up_id_entry.place(x=150, y=20, width="250")
Label(detail, text="type", font="bold 10").place(x=20, y=40)
up_type_entry = Entry(detail, textvariable=up_type)
up_type_entry.place(x=150, y=40, width="250")
Label(detail, text="name", font="bold 10").place(x=20, y=60)
up_name_entry = Entry(detail, textvariable=up_name)
up_name_entry.place(x=150, y=60, width="250")
Label(detail, text="user_name", font="bold 10").place(x=20, y=80)
up_user_name_entry = Entry(detail, textvariable=up_user_name)
up_user_name_entry.place(x=150, y=80, width="250")
Label(detail, text="user_password", font="bold 10").place(x=20, y=100)
up_user_password_entry = Entry(detail, textvariable=up_user_password)
up_user_password_entry.place(x=150, y=100, width="250")
Label(detail, text="email", font="bold 10").place(x=20, y=120)
up_email_entry = Entry(detail, textvariable=up_email)
up_email_entry.place(x=150, y=120, width="250")
Label(detail, text="contact", font="bold 10").place(x=20, y=140)
up_contact_entry = Entry(detail, textvariable=up_contact)
up_contact_entry.place(x=150, y=140, width="250")
Label(detail, text="address", font="bold 10").place(x=20, y=160)
up_address_entry = Entry(detail, textvariable=up_address)
up_address_entry.place(x=150, y=160, width="250")
Label(detail, text="year", font="bold 10").place(x=20, y=180)
up_year_entry = Entry(detail, textvariable=up_year)
up_year_entry.place(x=150, y=180, width="250")
Label(detail, text="departmant", font="bold 10").place(x=20, y=200)
up_departmant_entry = Entry(detail, textvariable=up_departmant)
up_departmant_entry.place(x=150, y=200, width="250")
Button(detail, text="UPDATE DETAIL", command=update_detail, pady=4, padx=20).place(x=190, y=240)


detail.place(x=0, y=140)
option_frame.pack(side=LEFT, fill="y")
show_detail_frame.pack(side=TOP, fill="x")
root.mainloop()