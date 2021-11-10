# imports 
from tkinter import *
import tkinter.messagebox as mbx
import tkinter.font as fnt
import mysql.connector as mysql
from mysql.connector.errors import DatabaseError

from tkinter import ttk

# root 
root = Tk()
root.geometry("800x700+530+25")
root.title("BIT ADMINISTRATION")
root.resizable(False,False)

# loged data  
already_loged_in = "no"
loged_in_id = "no"
loged_in_type = "no"
loged_uname = "no"
loged_dept = "no"


# var  
login_id = StringVar()
login_password = StringVar()

acc_type = StringVar()
acc_name = StringVar()
acc_username = StringVar()
acc_user_password = StringVar()
acc_email = StringVar()
acc_contact = StringVar()
acc_address = StringVar()
acc_year = StringVar()
acc_departmant = StringVar()

n_dep = StringVar()
n_date = StringVar()
n_sub = StringVar()
n_body = StringVar()
n_id = StringVar()

feed_dept = StringVar()
feed_subj = StringVar()
feed_msg = StringVar()
det_feed = StringVar()

resolve_feed = StringVar()

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

# functions 
def get_detail():
    if id_to_get_detail.get()=="":
        mbx.showerror(title="WARNING", message="NEED ID TO SHOW DETAIL")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
            cursor = con.cursor()
            sql = f"select * from logdata where user_name='{id_to_get_detail.get()}'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows==[]:
                mbx.showerror(title="WARNING", message="NO DATA FOUND")
            else:
                up_id_entry.delete(0, "end")
                up_type_entry.delete(0, "end")
                up_name_entry.delete(0, "end")
                up_user_name_entry.delete(0, "end")
                up_user_password_entry.delete(0, "end")
                up_email_entry.delete(0, "end")
                up_contact_entry.delete(0, "end")
                up_address_entry.delete(0, "end")
                up_year_entry.delete(0, "end")
                up_departmant_entry.delete(0, "end")


                up_id_entry.insert(0, rows[0][0])
                up_type_entry.insert(0, rows[0][1])
                up_name_entry.insert(0, rows[0][2])
                up_user_name_entry.insert(0, rows[0][3])
                up_user_password_entry.insert(0, rows[0][4])
                up_email_entry.insert(0, rows[0][5])
                up_contact_entry.insert(0, rows[0][6])
                up_address_entry.insert(0, rows[0][7])
                up_year_entry.insert(0, rows[0][8])
                up_departmant_entry.insert(0, rows[0][9])
                detail.place(x=0, y=140)
        except Exception as exp:
            mbx.showerror(title="WARNING", message=f"{exp}")

def update_detail():
    con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
    cursor = con.cursor()
    sql = f"UPDATE logdata SET type='{up_type_entry.get()}', name='{up_name_entry.get()}', user_password='{up_user_password_entry.get()}', email='{up_email_entry.get()}', contact='{up_contact_entry.get()}', address='{up_address_entry.get()}', year='{up_year_entry.get()}', departmant='{up_departmant_entry.get()}' WHERE user_name='{id_to_get_detail.get()}'"
    try:
        cursor.execute(sql)
        cursor.execute("commit")
        mbx.showinfo(title="SUCCESS", message=f"FEEDBACK UPDATED SUCCESSFULLY")
        con.close()
    except Exception as exp:
        mbx.showerror(title="WARNING", message=f"{exp}")  

def view_detail_func():
    for widgets in root.winfo_children():
        widgets.pack_forget()
    option_frame.pack(side=LEFT, fill="y")
    show_detail_frame.pack(side=TOP, fill="x")

def Re_back_feed():
    if resolve_feed.get()=="":
        mbx.showerror(title="WARNING", message="please select id")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
            cursor = con.cursor()
            global loged_uname
            sql = f"UPDATE feed SET responder = '{loged_uname}' WHERE id={resolve_feed.get()}"
            cursor.execute(sql)
            cursor.execute("commit")
            mbx.showinfo(title="SUCCESS", message=f"FEEDBACK UPDATED SUCCESSFULLY")
            responded_feed_entry.delete(0, 'end')
            con.close()
        except Exception as exp:
            mbx.showerror(title="WARNING", message=f"{exp}")  

def refresh_feed():
    for widget in rspfrm.winfo_children():
        widget.destroy()
    global loged_dept
    NULL = "NULL"
    sql = f"select id, sender, subject, responder from feed where dep='{loged_dept}' and responder = '{NULL}'"
    con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    tv = ttk.Treeview(rspfrm, columns=(1,2,3,4), show="headings", height='10')
    tv.pack()
    tv.heading(1, text="id")
    tv.column(1, minwidth=0, width=100, stretch=NO)
    tv.heading(2, text="sender")
    tv.column(2, minwidth=0, width=100, stretch=NO)
    tv.heading(3, text="subject")
    tv.column(3, minwidth=0, width=200, stretch=NO)
    tv.heading(4, text="responder")
    tv.column(4, minwidth=0, width=100, stretch=NO)
    for i in rows:
        tv.insert('', 'end', values=i)
    rspfrm.place(x=0, y=280)

def send_feed():
    if feed_dept.get()=="" or feed_subj.get()=="" or feed_msg.get()=="":
        mbx.showerror(title="WARNING", message="ALL FIELDS ARE REQUIRED TO CREATE FEEDBACK")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
        cursor = con.cursor()
        NULL = 'NULL'
        cursor.execute("SELECT MAX(id) FROM feed")
        rows = cursor.fetchall()
        n_p = (rows[0][0])+1
        global loged_uname
        cursor.execute("insert into feed values('"+ str(n_p) +"','"+ loged_uname +"','"+ feed_dept.get() +"','"+ feed_subj.get() +"','"+ feed_msg.get() +"','"+ NULL +"')")
        cursor.execute("commit")
        mbx.showinfo(title="SUCCESS", message=f"SUCCESSFULL FEEDBACK SUBMISSION")
        feed_dept_entry.delete(0, 'end')
        feed_subj_entry.delete(0, 'end')
        feed_msg_entry.delete(0, 'end')
        con.close()

def send_feed_enter():
    for widgets in root.winfo_children():
        widgets.pack_forget()
    option_frame.pack(side=LEFT, fill="y")
    send_feed_frame.pack(side=TOP, fill="x")

def rec_feed_enter():
    if loged_in_type=="teacher":
        for widgets in root.winfo_children():
            widgets.pack_forget()
        option_frame.pack(side=LEFT, fill="y")
        res_feed_frame.pack(side=TOP, fill="x")
    else:
        mbx.showerror(title="WARNING", message="ONLY FOR TEACHERS")

def back_feed():
    if n_id.get()=="":
        mbx.showerror(title="WARNING", message="NOTICE Id must be given in order to DELETE record")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
            cursor = con.cursor()
            cursor.execute("delete from feed where id='"+ det_feed.get() +"'")
            cursor.execute("commit")
            mbx.showinfo(title="SUCCESS", message=f"FEEDBACK PULLEDOUT SUCCESSFULLY")
            det_feed_entry.delete(0, 'end')
            con.close()
        except Exception as exp:
            mbx.showerror(title="WARNING", message=f"{exp}")       

def res_feed():
    for widget in ffrm.winfo_children():
        widget.destroy()
    global loged_uname
    sql = f"select id, sender, subject, responder from feed where sender='{loged_uname}' and responder != 'NULL'"
    con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    tv = ttk.Treeview(ffrm, columns=(1,2,3,4), show="headings", height='10')
    tv.pack()
    tv.heading(1, text="id")
    tv.column(1, minwidth=0, width=100, stretch=NO)
    tv.heading(2, text="sender")
    tv.column(2, minwidth=0, width=100, stretch=NO)
    tv.heading(3, text="subject")
    tv.column(3, minwidth=0, width=200, stretch=NO)
    tv.heading(4, text="responder")
    tv.column(4, minwidth=0, width=100, stretch=NO)
    for i in rows:
        tv.insert('', 'end', values=i)
    ffrm.place(x=0, y=280)

def create_notice():
    if n_dep.get()=="" or n_date.get()=="" or n_sub.get()=="" or n_body.get()=="":
        mbx.showerror(title="WARNING", message="ALL FIELDS ARE REQUIRED TO CREATE NOTICE")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
        cursor = con.cursor()
        cursor.execute("SELECT MAX(idnotice) FROM notice")
        rows = cursor.fetchall()
        n_p = (rows[0][0])+1
        global loged_uname
        cursor.execute("insert into notice values('"+ str(n_p) +"','"+ loged_uname +"','"+ n_dep.get() +"','"+ n_date.get() +"','"+ n_sub.get() +"','"+ n_body.get() +"')")
        cursor.execute("commit")
        mbx.showinfo(title="SUCCESS", message=f"NOTICE CREATED SUCCESSFULLY by author {loged_uname}")
        n_dep_entry.delete(0, 'end')
        n_date_entry.delete(0, 'end')
        n_sub_entry.delete(0, 'end')
        n_body_entry.delete(0, 'end')
        con.close()

def delete_notice():
    if n_id.get()=="":
        mbx.showerror(title="WARNING", message="NOTICE Id must be given in order to DELETE record")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
            cursor = con.cursor()
            cursor.execute("delete from notice where idnotice='"+ n_id.get() +"'")
            cursor.execute("commit")
            mbx.showinfo(title="SUCCESS", message=f"NOTICE DELEATED SUCCESSFULLY")
            n_id_entry.delete(0, 'end')
            con.close()
        except Exception as exp:
            mbx.showerror(title="WARNING", message=f"{exp}")

def view_notice():
    for widget in nfrm.winfo_children():
        widget.destroy()
    if n_dep.get()=="":
        sql = "select idnotice, author, subject from notice"
    else:
        sql = f"select idnotice, author, subject from seproject.notice where dep='{n_dep.get()}'"
    con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    tv = ttk.Treeview(nfrm, columns=(1,2,3), show="headings", height='10')
    tv.pack()
    tv.heading(1, text="id")
    tv.column(1, minwidth=0, width=75, stretch=NO)
    tv.heading(2, text="author")
    tv.column(2, minwidth=0, width=75, stretch=NO)
    tv.heading(3, text="subject")
    tv.column(3, minwidth=0, width=300, stretch=NO)
    for i in rows:
        tv.insert('', 'end', values=i)
    nfrm.place(x=0, y=280)

def enter_notice():
    print("enter_notice")
    for widgets in root.winfo_children():
        widgets.pack_forget()
    option_frame.pack(side=LEFT, fill="y")
    notice_frame.pack(side=TOP, fill="x")

def view_acc():
    if acc_type.get()=="" or acc_departmant.get()=="":
        mbx.showerror(title="WARNING", message="Account TYPE and DEPARTMENT are MUST")
    else:
        if  acc_type.get()=="student" and acc_year.get()=="":
            mbx.showerror(title="WARNING", message="You have opted for student so year is also must")
        else:
            if acc_type.get()=="student":
                sql = f"select type, name, user_name, email, departmant from logdata where type='student' and year='{acc_year.get()}' and departmant='{acc_departmant.get()}'"
            elif acc_type.get()=="teacher":
                sql = f"select type, name, user_name, email, departmant from seproject.logdata where type='teacher' and departmant='{acc_departmant.get()}';"
            con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
            cursor = con.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            all_acc = Tk()
            all_acc.geometry("1000x250+10+25")
            all_acc.title(f"{acc_type.get()} {acc_departmant.get()} {acc_year.get()}")
            all_acc.resizable(False,False)
            frm = Frame(all_acc)
            frm.pack(side=TOP, fill="y")
            tv = ttk.Treeview(frm, columns=(1,2,3,4,5), show="headings", height='11')
            tv.pack()
            tv.heading(1, text="type")
            tv.heading(2, text="name")
            tv.heading(3, text="user_name")
            tv.heading(4, text="email")
            tv.heading(5, text="departmant")
            for i in rows:
                tv.insert('', 'end', values=i)
            con.close()
            all_acc.mainloop()

def create_acc():
    if acc_type.get()=="" or acc_name.get()=="" or acc_user_password.get()=="" or acc_email.get()=="" or acc_contact.get()=="" or acc_address.get()=="" or acc_year.get()=="" or acc_departmant.get()=="":
        mbx.showerror(title="WARNING", message="ALL FIELDS ARE REQUIRED")
    else:
        global loged_in_type
        if loged_in_type == "teacher":
            p1 = "tech"
            p2 = acc_departmant.get()
            con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
            cursor = con.cursor()
            cursor.execute("SELECT MAX(id) FROM logdata")
            rows = cursor.fetchall()
            n_p = (rows[0][0])+1
            uid = f"{p1}-{p2}-{n_p}"
            if acc_type.get()=="student":
                p1 = acc_departmant.get()
                lp = acc_year.get()
                uid = f"{p1}-{n_p}-{lp}"
            try:
                cursor.execute("insert into logdata values('"+ str(n_p) +"','"+ acc_type.get() +"', '"+ acc_name.get() +"','"+ uid +"', '"+ acc_user_password.get() +"', '"+ acc_email.get() +"', '"+ str(acc_contact.get()) +"', '"+ acc_address.get() +"', '"+ acc_year.get() +"', '"+ acc_departmant.get() +"')")
                cursor.execute("commit")
                mbx.showinfo(title="SUCCESS", message=f"ACCOUNT {uid} CREATED SUCCESSFULLY WITH GIVEN PASSWORD")
                acc_type_entry.delete(0, 'end')
                acc_name_entry.delete(0, 'end')
                acc_user_password_entry.delete(0, 'end')
                acc_email_entry.delete(0, 'end')
                acc_contact_entry.delete(0, 'end')
                acc_address_entry.delete(0, 'end')
                acc_year_entry.delete(0, 'end')
                acc_departmant_entry.delete(0, 'end')
                con.close()
            except Exception as exp:
                mbx.showerror(title="WARNING", message=f"{exp}")
        else:
            mbx.showerror(title="WARNING", message="YOU ARE NOT AUTHORISED OF CREATING ACCOUNT")

def delete_acc():
    if acc_username.get()=="":
        mbx.showerror(title="WARNING", message="User Name Id must be geven in order to DELETE record")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
        cursor = con.cursor()
        try:
            cursor.execute("delete from logdata where user_name='"+ acc_username.get() +"'")
            mbx.showinfo(title="SUCCESS", message=f"ACCOUNT {acc_username.get()} DELEATED SUCCESSFULLY")
            print(f"delete account {acc_username.get()}")
            cursor.execute("commit")
            acc_username_entry.delete(0, 'end')
            con.close()
        except Exception as exp:
            mbx.showerror(title="WARNING", message=f"{exp}")

def login():
    u_name = login_id.get()
    u_passwrd = login_password.get()
    if u_name=="" or u_passwrd=="":
        mbx.showerror(title="WARNING", message="LOG DETAILS ARE EMPTY")
    else:
        con = mysql.connect(host="localhost", user="root", password="1234", database="seproject")
        cursor = con.cursor()
        cursor.execute("select * from logdata where user_name='"+ u_name +"' and user_password='"+ u_passwrd +"'")
        rows = cursor.fetchall()
        if rows == []:
            mbx.showerror(title="WARNING", message="WRONG LOGIN CREDENTIALS")
        else:
            print(f"loged in as { u_name }")
            global already_loged_in
            already_loged_in = "yes"
            global loged_in_id
            loged_in_id = rows[0][0]
            global loged_in_type
            loged_in_type = rows[0][1]
            global loged_uname 
            loged_uname = rows[0][3]
            global loged_dept
            loged_dept = rows[0][9]
            mbx.showinfo(title="SUCCESS", message=f"LOGED IN SUCCESSFULLY AS {loged_uname}")
            for widgets in root.winfo_children():
                widgets.pack_forget()
            option_frame.pack(side=LEFT, fill="y")
            blank_frame.pack(side=TOP, fill="x")
            root.title(f"BIT ADMINISTRATION      Logedin as:- ({loged_in_type}) {loged_uname}")
        con.close()

def set_login():
    None_login_frame.pack(side=LEFT, fill="y")
    login_frame.pack(side=TOP, fill="x")
    return "Set_login_packed"

def logout():
    print("logout")
    global loged_uname 
    mbx.showinfo(title="SUCCESS", message=f"Loged out successfully from account {loged_uname}")
    global already_loged_in
    already_loged_in = "no"
    global loged_in_id
    loged_in_id = "no"
    global loged_in_type
    loged_in_type = "no"
    loged_uname = "no"
    global loged_dept
    loged_dept = "no"
    root.title("BIT ADMINISTRATION")
    for widgets in root.winfo_children():
        widgets.pack_forget()
    None_login_frame.pack(side=LEFT, fill="y")
    login_frame.pack(side=TOP, fill="x")

def enter_acc():
    print("enter_acc")
    for widgets in root.winfo_children():
        widgets.pack_forget()
    option_frame.pack(side=LEFT, fill="y")
    useracount_frame.pack(side=TOP, fill="x")

# frames 
res_feed_frame = Frame(root, width=500, height=700, borderwidth=8,bg="#e0e68a", relief=SUNKEN)
Label(res_feed_frame, text="RESPOND TO FEEDBACKS", font="bold 10").place(x=150, y=20)
Button(res_feed_frame, text="RESPOND FEEDBACK", command=Re_back_feed, pady=4,bg="#dcdcdc", padx=20).place(x=50, y=60)
responded_feed_entry = Entry(res_feed_frame, textvariable=resolve_feed)
responded_feed_entry.place(x=300, y=60, height=30)
responded_feed_entry.insert(0, "ENTER FEEDBACK ID")
Button(res_feed_frame, text="REFRESH RESPONDS", command=refresh_feed, pady=4,bg="#e0e68a", padx=20).place(x=170, y=120)
rspfrm = Frame(res_feed_frame, width=500, height=400, borderwidth=8, relief=SUNKEN)

None_login_frame = Frame(root, bg="#A9A9A9", width=300, height=700, borderwidth=6, relief=SUNKEN)
Label(None_login_frame, text="PLEASE LOGIN YOUR CREDENTIALS", font="bold 10",bg="#A9A9A9", pady=5).place(x=30, y=325)

login_frame = Frame(root, width=500, height=700, borderwidth=8, relief=SUNKEN)
Label(login_frame, text="LOGIN YOUR CREDENTIALS", font="bold 10", pady=5).grid(row=1, column=1)
Label(login_frame, text="Enter Login ID", font="bold 10", pady=15, padx=10).grid(row=2, column=0)
Label(login_frame, text="Enter Login Password", font="bold 10", pady=15, padx=10).grid(row=3, column=0)
login_id_entry = Entry(login_frame, textvariable=login_id).grid(row=2, column=1)
login_password_entry = Entry(login_frame, textvariable=login_password).grid(row=3, column=1)
Button(login_frame, text="LOGIN", command=login, pady=4,bg="#A9A9A9", padx=20, font="blue 12").grid(row=4, column=1)

blank_frame = Frame(root, width=500, height=700, borderwidth=8, relief=SUNKEN)

option_frame = Frame(root, bg="#A9A9A9", width=300, height=700, borderwidth=6, relief=SUNKEN)
Button(option_frame, text="User Accounts", command=enter_acc, pady=5,bg="#dcdcdc", padx=5, font = fnt.Font(size = 8)).place(x=80, y=25)
Button(option_frame, text="Manage Notice", command=enter_notice, pady=5,bg="#dcdcdc", padx=5, font = fnt.Font(size = 8)).place(x=80, y=75)
Button(option_frame, text="SEND FEEDBACK", command=send_feed_enter, pady=5,bg="#dcdcdc", padx=5, font = fnt.Font(size = 8)).place(x=80, y=125)
Button(option_frame, text="FEEDBACK RESPONCE", command=rec_feed_enter, pady=5,bg="#e0e68a", padx=5, font = fnt.Font(size = 8)).place(x=80, y=175)
Button(option_frame, text="VIEW ACCOUNT DETAIL", command=view_detail_func, pady=5,bg="#dcdcdc", padx=5, font = fnt.Font(size = 8)).place(x=80, y=225)
Button(option_frame, text="QUIT", command=quit, pady=5,bg="#555555", padx=5, font = fnt.Font(size = 8)).place(x=110, y=605)
Button(option_frame, text="Logout", command=logout, pady=5,bg="#555555", padx=5, font = fnt.Font(size = 8)).place(x=105, y=650)

useracount_frame = Frame(root, width=500, height=700, borderwidth=8, relief=SUNKEN)
Label(useracount_frame, text="REGISTER A USER", font="bold 10", padx=15, pady=10).place(x=190, y=35)
Label(useracount_frame, text="Account Type", font="bold 10").place(x=70, y=100)
acc_type_entry = Entry(useracount_frame, textvariable=acc_type)
acc_type_entry.place(x=280, y=100)
Label(useracount_frame, text="Name", font="bold 10").place(x=70, y=130)
acc_name_entry = Entry(useracount_frame, textvariable=acc_name)
acc_name_entry.place(x=280, y=130)
Label(useracount_frame, text="User Password", font="bold 10").place(x=70, y=160)
acc_user_password_entry = Entry(useracount_frame, textvariable=acc_user_password)
acc_user_password_entry.place(x=280, y=160)
Label(useracount_frame, text="User Email", font="bold 10").place(x=70, y=190)
acc_email_entry = Entry(useracount_frame, textvariable=acc_email)
acc_email_entry.place(x=280, y=190)
Label(useracount_frame, text="User Contact", font="bold 10").place(x=70, y=220)
acc_contact_entry = Entry(useracount_frame, textvariable=acc_contact)
acc_contact_entry.place(x=280, y=220)
Label(useracount_frame, text="User Address", font="bold 10").place(x=70, y=250)
acc_address_entry = Entry(useracount_frame, textvariable=acc_address)
acc_address_entry.place(x=280, y=250)
Label(useracount_frame, text="Joining year", font="bold 10").place(x=70, y=280)
acc_year_entry = Entry(useracount_frame, textvariable=acc_year)
acc_year_entry.place(x=280, y=280)
Label(useracount_frame, text="User departmant", font="bold 10").place(x=70, y=310)
acc_departmant_entry = Entry(useracount_frame, textvariable=acc_departmant)
acc_departmant_entry.place(x=280, y=310)
Label(useracount_frame, text="User Name Id (dont fill to create)", font="bold 10").place(x=70, y=340)
acc_username_entry = Entry(useracount_frame, textvariable=acc_username)
acc_username_entry.place(x=280, y=340)
Button(useracount_frame, text="CREATE", command=create_acc, pady=4,bg="#dcdcdc", padx=20).place(x=50, y=420)
Button(useracount_frame, text="DELETE", command=delete_acc, pady=4,bg="#dcdcdc", padx=20).place(x=180, y=420)
Button(useracount_frame, text="VIEW ALL", command=view_acc, pady=4,bg="#A9A9A9", padx=20).place(x=310, y=420)

notice_frame = Frame(root, width=500, height=700, borderwidth=8, relief=SUNKEN)
Label(notice_frame, text="MANAGE NOTICE", font="bold 10").place(x=200, y=20)
Label(notice_frame, text="NOTICE DEPARTMENT", font="bold 10").place(x=30, y=60)
n_dep_entry = Entry(notice_frame, textvariable=n_dep)
n_dep_entry.place(x=230, y=60, width="200")
Label(notice_frame, text="NOTICE DATE", font="bold 10").place(x=30, y=80)
n_date_entry = Entry(notice_frame, textvariable=n_date)
n_date_entry.place(x=230, y=80, width="200")
Label(notice_frame, text="NOTICE SUBJECT", font="bold 10").place(x=30, y=100)
n_sub_entry = Entry(notice_frame, textvariable=n_sub)
n_sub_entry.place(x=230, y=100, width="200")
Label(notice_frame, text="NOTICE BODY", font="bold 10").place(x=30, y=120)
n_body_entry = Entry(notice_frame, textvariable=n_body)
n_body_entry.place(x=230, y=120, width="200", height="100")
Button(notice_frame, text="CREATE", command=create_notice, pady=4,bg="#dcdcdc", padx=20).place(x=50, y=230)
Button(notice_frame, text="DELETE", command=delete_notice, pady=4,bg="#dcdcdc", padx=20).place(x=190, y=230)
n_id_entry = Entry(notice_frame, textvariable=n_id)
n_id_entry.place(x=280, y=230, width="50", height="30")
n_id_entry.insert(1, "Enter ID")
Button(notice_frame, text="VIEW ALL", command=view_notice, pady=4,bg="#A9A9A9", padx=20).place(x=380, y=230)
nfrm = Frame(notice_frame, width=480, height=380, borderwidth=8, relief=SUNKEN, bg="#e0e68a")

send_feed_frame = Frame(root, width=500, height=700, borderwidth=8,bg="#e0e68a", relief=SUNKEN)
Label(send_feed_frame, text="SEND YOUR FEEDBACK HERE", font="bold 10").place(x=150, y=20)
Label(send_feed_frame, text="ENTER RECIEPIENT DEPARTMENT", font="bold 10").place(x=50, y=50)
Label(send_feed_frame, text="ENTER THE SUBJECT", font="bold 10").place(x=50, y=80)
Label(send_feed_frame, text="ENTER YOUR MESSAGE BODY HERE", font="bold 10").place(x=50, y=110)
feed_dept_entry = Entry(send_feed_frame, textvariable=feed_dept)
feed_dept_entry.place(x=300, y=50)
feed_subj_entry = Entry(send_feed_frame, textvariable=feed_subj)
feed_subj_entry.place(x=300, y=80)
feed_msg_entry = Entry(send_feed_frame, textvariable=feed_msg)
feed_msg_entry.place(x=300, y=110)
Button(send_feed_frame, text="SEND FEEDBACK", command=send_feed, pady=4,bg="#dcdcdc", padx=20).place(x=50, y=150)
Button(send_feed_frame, text="PULLBACK FEEDBACK", command=back_feed, pady=4,bg="#dcdcdc", padx=20).place(x=50, y=190)
det_feed_entry = Entry(send_feed_frame, textvariable=det_feed)
det_feed_entry.place(x=300, y=190, height=30)
det_feed_entry.insert(0, "ENTER FEEDBACK ID")
Button(send_feed_frame, text="REFRESH RESPONDS", command=res_feed, pady=4,bg="#e0e68a", padx=20).place(x=170, y=230)
ffrm = Frame(send_feed_frame, width=500, height=380, borderwidth=8, relief=SUNKEN)



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


# mainloop and trigger 
print(set_login())
root.mainloop()