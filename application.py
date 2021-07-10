from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time
import datetime 
from functools import partial
a = datetime.datetime.now()

import sqlite3,sys

def connection():
    try:
        conn=sqlite3.connect("database.db")
    except:
        print("cannot connect to the database")
    return conn    

#connecting to the database
db = connection()
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    root1.destroy()

def error():
    global err
    err = Toplevel(root1)
    err.title("Error")
    err.geometry("200x100")
    Label(err,text="All fields are required..",fg="red",font="bold").pack()
    Label(err,text="").pack()
    Button(err,text="Ok",bg="grey",width=8,height=1,command=error_destroy).pack()

def success():
    global succ
    succ = Toplevel(root1)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text="Registration successful...", fg="green", font="bold").pack()
    Label(succ, text="").pack()
    Button(succ, text="Ok", bg="grey", width=8, height=1, command=succ_destroy).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        mycur.execute("CREATE TABLE IF NOT EXISTS login(ID INTEGER PRIMARY KEY AUTOINCREMENT,USERNAME VARCHAR,PASSWORD VARCHAR)")
        sql = "insert into login (USERNAME,PASSWORD) values(?,?)"
        t = (username_info, password_info)
        mycur.execute(sql, t)
        db.commit()
        with open("login.txt","a+") as f:
            f.write("username: " + username_info)
            f.write("\npassword: " + password_info)
            f.write("\n=====================\n")
            
        Label(root1, text="").pack()
        time.sleep(0.50)
        success()




def po_destroy():
    po.destroy()
def pi_destroy():
    pi.destroy()
def Mp_destroy():
    Mp.destroy()
def Ap_destroy():
    Ap.destroy()
def Ep_destroy():
    Ep.destroy()
def Sd_destroy():
    Sd.destroy()
def registration():
    global root1
    root1 = Toplevel(root)
    root1.title("Registration Portal")
    root1.geometry("300x250")
    global username
    global password
    Label(root1,text="Register your account",bg="grey",fg="black",font="bold",width=300).pack()
    username = StringVar()
    password = StringVar()
    Label(root1,text="").pack()
    Label(root1,text="Username :",font="bold").pack()
    Entry(root1,textvariable=username).pack()
    Label(root1, text="").pack()
    Label(root1, text="Password :").pack()
    Entry(root1, textvariable=password,show="*").pack()
    Label(root1, text="").pack()
    Button(root1,text="Register",bg="red",command=register_user).pack()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Log-In Portal")
    root2.geometry("300x300")
    global username_varify
    global password_varify
    Label(root2, text="Log-In Portal", bg="grey", fg="black", font="bold",width=300).pack()
    username_varify = StringVar()
    password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", font="bold").pack()
    Entry(root2, textvariable=username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :").pack()
    Entry(root2, textvariable=password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="red",command=login_varify).pack()
    Label(root2, text="")
def Admin():
    global root2
    root2 = Toplevel(root)
    root2.title("Admin Portal")
    root2.geometry("300x300")
    global admin_username_varify
    global admin_password_varify
    Label(root2, text="Admin Portal", bg="grey", fg="black", font="bold",width=300).pack()
    admin_username_varify = StringVar()
    admin_password_varify = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Admin Username :", font="bold").pack()
    Entry(root2, textvariable=admin_username_varify).pack()
    Label(root2, text="").pack()
    Label(root2, text="Admin Password :").pack()
    Entry(root2, textvariable=admin_password_varify, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Log-In", bg="red",command=admin_varify).pack()
    Label(root2, text="")

def logg_destroy():
    logg.destroy()
    root2.destroy()
    Mp.destroy()

def fail_destroy():
    fail.destroy()

def failed():
    global fail
    fail = Toplevel(root2)
    fail.title("Invalid")
    fail.geometry("200x100")
    Label(fail, text="Invalid credentials...", fg="red", font="bold").pack()
    Label(fail, text="").pack()
    Button(fail, text="Ok", bg="grey", width=8, height=1, command=fail_destroy).pack()

def getUserId():
    sql = "select id from login where username = ? and password = ?"
    mycur.execute(sql,[(username_varify.get()),(password_varify.get())])
    results = mycur.fetchall()
    return results[0][0]
def addEmpty(user_id):
    sql= 'INSERT INTO details (loginId) VALUES(?)'
    t = (user_id,)
    mycur.execute(sql,t)
    db.commit()
    print("empty data added")
def Punchin(user_id):
    sql= 'UPDATE details SET punchin = ? WHERE id = ?'
    t = (a.strftime('%Y-%m-%d %H:%M:%S'),user_id)
    mycur.execute(sql,t)
    db.commit()
    global pi
    pi = Toplevel(root)
    pi.title("Success")
    pi.geometry("200x100")
    Label(pi, text="Punch successful...", fg="green", font="bold").pack()
    Label(pi, text="").pack()
    Button(pi, text="Ok", bg="grey", width=8, height=1, command=pi_destroy).pack()

def Punchout(id):
    sql= 'UPDATE details SET punchout = ? WHERE id = ?'
    cur_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    t = (cur_date,id)
    mycur.execute(sql,t)
    db.commit()
    global po
    po = Toplevel(root)
    po.title("Success")
    po.geometry("200x100")
    Label(po, text="Punch successful...", fg="green", font="bold").pack()
    Label(po, text="").pack()
    Button(po, text="Ok", bg="grey", width=8, height=1, command=po_destroy).pack()

def getPunchOut(user_id):
    mycur.execute("CREATE TABLE IF NOT EXISTS details(ID INTEGER PRIMARY KEY AUTOINCREMENT,loginId INTEGER,PUNCHIN DATETIME,PUNCHOUT DATETIME ,MORNING TEXT,AFTERNOON TEXT,EVENING TEXT, CONSTRAINT fk_departments FOREIGN KEY (loginId) REFERENCES login(loginId))")
    cur_Date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    sql = "select id from details where Date(punchin) = ? and loginId = ?"
    mycur.execute(sql,(cur_Date,user_id))
    results = mycur.fetchall()
    return results


def getDetailsId(user_id):
    mycur.execute("CREATE TABLE IF NOT EXISTS details(ID INTEGER PRIMARY KEY,loginId INTEGER,PUNCHIN DATETIME,PUNCHOUT DATETIME ,MORNING TEXT,AFTERNOON TEXT,EVENING TEXT, CONSTRAINT fk_departments FOREIGN KEY (loginId) REFERENCES login(loginId))")
    sql = "select id from details where loginId = ?"
    mycur.execute(sql,(user_id,))
    results = mycur.fetchall()
    print(results)
    # try:
    #     print("in try")
    #     result = results[0][0]
    # except Exception as e:
    #     print("in exception")
    #     mycur.execute('SELECT id FROM details ORDER BY id DESC LIMIT 1')
    #     results = mycur.fetchall()
    #     try:
    #         result = results[0][0] + 1
    #     except Exception as e:
    #         result= 0
    # print(result)
    return results
    

def MorningPost(id):
    sql= 'UPDATE details SET morning = ? WHERE id = ?'
    morning_data = morning.get()
    t = (morning_data,id)
    mycur.execute(sql,t)
    db.commit()
    global Mp
    Mp = Toplevel(root)
    Mp.title("Success")
    Mp.geometry("200x100")
    Label(Mp, text="Morning posted successful...", fg="green", font="bold").pack()
    Label(Mp, text="").pack()
    Button(Mp, text="Ok", bg="grey", width=8, height=1, command=Mp_destroy).pack()
def AfternoonPost(id):
    sql= 'UPDATE details SET afternoon = ? WHERE id = ?'
    afternoon_data = afternoon.get()
    t = (afternoon_data,id)
    mycur.execute(sql,t)
    db.commit()
    global Ap
    Ap = Toplevel(root)
    Ap.title("Success")
    Ap.geometry("200x100")
    Label(Ap, text="afternoon posted successful...", fg="green", font="bold").pack()
    Label(Ap, text="").pack()
    Button(Ap, text="Ok", bg="grey", width=8, height=1, command=Ap_destroy).pack()
def EveningPost(id):
    sql= 'UPDATE details SET evening = ? WHERE id = ?'
    evening_data = evening.get()
    t = (evening_data,id)
    mycur.execute(sql,t)
    db.commit()
    global Ep
    Ep = Toplevel(root)
    Ep.title("Success")
    Ep.geometry("200x100")
    Label(Ep, text="evening posted successful...", fg="green", font="bold").pack()
    Label(Ep, text="").pack()
    Button(Ep, text="Ok", bg="grey", width=8, height=1, command=Ep_destroy).pack()

def checkData(id,mode):
    sql = "select "+mode +" from details where id ="+str(id)
    print(sql)
    mycur.execute(sql)
    results = mycur.fetchall()
    return results
def logged():
    global logg
    logg = Toplevel(root)
    logg.title("Welcome")
    logg.geometry("500x500")
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    user_id= getUserId()
    global id
    try:
        id= getDetailsId(user_id)[0][0]
        print(id)
    except Exception as e:
        print(e)
        addEmpty(user_id)
    finally:
        id= getDetailsId(user_id)[0][0]
        print(id)

    Button(logg, text="Punch-in", bg="blue", width=8, height=1,command=partial(Punchin,id)).pack()

    Button(logg, text="Punch-Out", bg="red", width=8, height=1,command=partial(Punchout,id)).pack()
    global morning
    global afternoon
    global evening
    morning = StringVar()
    afternoon = StringVar()
    evening = StringVar()
    Label(logg, text="").pack()
    Label(logg, text="Morning :", font="bold").pack()
    Entry(logg, textvariable=morning).pack()
    Button(logg, text="Submit",height="1",width="15",bg="Yellow",font="bold",command=partial(MorningPost,id)).pack()
    Label(logg, text="").pack()
    Label(logg, text="Afternoon :", font="bold").pack()
    Entry(logg, textvariable=afternoon).pack()
    Button(logg, text="Submit",height="1",width="15",bg="Yellow",font="bold",command=partial(AfternoonPost,id)).pack()
    Label(logg, text="").pack()
    Label(logg, text="Evening :", font="bold").pack()
    Entry(logg, textvariable=evening).pack()
    Button(logg, text="Submit",height="1",width="15",bg="Yellow",font="bold",command=partial(EveningPost,id)).pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()
def AllData():
    sql = "SELECT login.username,details.punchin,details.punchout,details.morning,details.afternoon,details.evening FROM login,details  WHERE login.id=details.loginId "
    mycur.execute(sql)
    results = mycur.fetchall()
    return results

def SaveData():
    results = AllData()
    with open("Data.txt","w+") as f:
        for data in results:
            f.write("=========\n")
            for d in data:
                f.write(str(d)+"\n")
    global Sd
    Sd = Toplevel(root)
    Sd.title("Success")
    Sd.geometry("200x100")
    Label(Sd, text="Data saved successful...", fg="green", font="bold").pack()
    Label(Sd, text="").pack()
    Button(Sd, text="Ok", bg="grey", width=8, height=1, command=Sd_destroy).pack()
def admin_logged():
    global logg
    logg = Toplevel(root)
    logg.title("Welcome to Admin Portal")
    logg.geometry("500x500")
    Label(logg, text="Welcome {} ".format(admin_username_varify.get()), fg="green", font="bold").pack()
    results = AllData()
    s = Scrollbar(logg)
    s.pack(side=RIGHT, fill=Y)
    Button(logg, text="Print data", bg="purple",foreground="white", width=8, height=1, command=SaveData).pack()
    Label(logg, text="").pack()
    t = Text(logg, height=4, width=50)
    t.pack(side=LEFT, fill=Y)
    for data in results:
        d = """
        ================\n
        Employee Name: """ +str(data[0])+"""\n
        PunchIn Time: """ +str(data[1])+"""\n
        PunchOut Time: """ +str(data[2])+"""\n
        Morning: """ +str(data[3])+"""\n
        Afternoon: """ +str(data[4])+"""\n
        Evening: """ +str(data[5])+"""\n

        """
        # Label(logg, text="================".format(admin_username_varify.get()), fg="green", font="bold").pack()
        # Label(logg, text="Employee Name: {}".format(data[0]), fg="Black", font="bold").pack()
        # Label(logg, text="PunchIn Time: {}".format(data[1]), fg="Black", font="bold").pack()
        # Label(logg, text="PunchOut Time: {}".format(data[2]), fg="Black", font="bold").pack()
        # Label(logg, text="Morning: {}".format(data[3]), fg="Black", font="bold").pack()
        # Label(logg, text="Afternoon: {}".format(data[4]), fg="Black", font="bold").pack()
        # Label(logg, text="Evening : {}".format(data[5]), fg="Black", font="bold").pack()
        
        t.insert(END,d)


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from login where username =? and password = ?"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    
    global user_id  
    if results:
        for i in results:
            logged()
            user_id = i[0]
            break
    else:
        failed()
def admin_varify():
    user_varify = admin_username_varify.get()
    pas_varify = admin_password_varify.get()
    sql = "select * from admin where username = ? and password = ?"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    
    global user_id  
    if results:
        for i in results:
            admin_logged()
            user_id = i[0]
            break
    else:
        failed()




def main_screen():
    global root
    root = Tk()
    root.title("Log-IN Portal")
    root.geometry("300x300")
    Label(root,text="Welcome to Log-In Protal",font="bold",bg="grey",fg="black",width=300).pack()
    Label(root,text="").pack()
    Button(root,text="Log-IN",width="8",height="1",bg="red",font="bold",command=login).pack()
    Label(root,text="").pack()
    Button(root, text="Registration",height="1",width="15",bg="red",font="bold",command=registration).pack()
    Label(root,text="").pack()
    Label(root,text="").pack()
    Button(root,text="Admin",width="8",height="1",bg="blue",font="bold",command=Admin).pack()
    Label(root,text="").pack()
main_screen()
root.mainloop()

db.close()