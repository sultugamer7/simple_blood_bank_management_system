# Importing required modules
import sqlite3
import re
import tkinter
from tkinter import *
from tkinter import messagebox

# Parent window as root
root = Tk()
root.attributes("-fullscreen", True)
root.config(bg="#FF3232")
# Title of root window
root.title("Blood Bank Management System")
labelfont = ("times", 30, "bold")
l1 = Label(root, text="BLOOD BANK MANAGEMENT SYSTEM", font=labelfont)
l1.config(bg="#FF3232", fg="#FCFF33")
l1.place(x=15, y=15)

# All definitions


# 1. New donor
def newdonor():
    nd = Toplevel(root, bg="#FCFF33")
    nd.title("Donor's Details Form")
    nd.geometry("680x350")

    ndl1 = Label(nd, text="Number : ", font="helvetica", bg="#FCFF33")
    ndl1.place(x=45, y=10)
    ndl2 = Label(nd, text="Name : ", font="helvetica", bg="#FCFF33")
    ndl2.place(x=58, y=50)
    ndl3 = Label(nd, text="Age : ", font="helvetica", bg="#FCFF33")
    ndl3.place(x=72, y=90)
    ndl4 = Label(nd, text="Gender : ", font="helvetica", bg="#FCFF33")
    ndl4.place(x=50, y=130)
    ndl5 = Label(nd, text="City : ", font="helvetica", bg="#FCFF33")
    ndl5.place(x=75, y=170)
    ndl6 = Label(nd, text=" Blood Group : ", font="helvetica", bg="#FCFF33")
    ndl6.place(x=10, y=210)
    ndl7 = Label(nd, text="Today's Date : ", font="helvetica", bg="#FCFF33")
    ndl7.place(x=10, y=250)

    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("SELECT MAX(ROWID) FROM DonorInfo")
    res = c.fetchone()
    ndal1 = Label(nd, font="helvetica", bg="#FCFF33")
    ndal1.place(x=120, y=10)
    if res[0] == None:
        ndal1.config(text="1")
    else:
        a = int(res[0])
        a += 1
        ndal1.config(text=a)
    ndal2 = Label(nd, text="demo", font="helvetica", bg="#FCFF33")
    ndal2.place(x=120, y=250)
    c.execute("SELECT date('now')")
    res1 = c.fetchone()
    a1 = res1[0]
    ndal2.config(text=a1)

    vfont = ("helvetica", 13, "bold")
    v1 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v1.place(x=270, y=50)
    v2 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v2.place(x=270, y=90)
    v3 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v3.place(x=270, y=130)
    v4 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v4.place(x=270, y=170)
    v5 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v5.place(x=270, y=210)

    def checkname(cn):
        mo1 = re.match(r"^([^0-9]*)$", cn.get())
        if not (cn.get()):
            v1.config(text="Name required!")
        elif not (mo1):
            v1.config(text="Valid name required!")
        else:
            v1.config(text="")

    cn = StringVar()
    cn.trace("w", lambda name, index, mode, cn=cn: checkname(cn))
    nde1 = Entry(nd, bd=3, textvariable=cn)
    nde1.place(x=120, y=53)

    def checkage(ca):
        mo2 = re.match(r"^(\d?[1-9]|[1-9]0)$", ca.get())
        if not (ca.get()):
            v2.config(text="Age required!")
        elif not (mo2):
            v2.config(text="Age must be within 1-99!")
        else:
            v2.config(text="")

    ca = StringVar()
    ca.trace("w", lambda name, index, mode, cn=cn: checkage(ca))
    nde2 = Entry(nd, bd=3, textvariable=ca)
    nde2.place(x=120, y=93)

    def checkcity(cc):
        mo3 = re.match(r"^([^0-9]*)$", cc.get())
        if not (cc.get()):
            v4.config(text="City required!")
        elif not (mo3):
            v4.config(text="Valid city name required!")
        else:
            v4.config(text="")

    cc = StringVar()
    cc.trace("w", lambda name, index, mode, cn=cn: checkcity(cc))
    nde3 = Entry(nd, bd=3, textvariable=cc)
    nde3.place(x=120, y=173)

    def sel1():
        radval1 = str(var1.get())
        ndl8.config(text=radval1)
        if not (ndl8.cget("text") != ""):
            v3.config(text="Gender required!")
        else:
            v3.config(text="")

    var1 = StringVar()
    ndr1 = Radiobutton(
        nd, text="Male", variable=var1, value="Male", command=sel1, bg="#FCFF33"
    )
    ndr1.place(x=120, y=133)
    ndr2 = Radiobutton(
        nd, text="Female", variable=var1, value="Female", command=sel1, bg="#FCFF33"
    )
    ndr2.place(x=180, y=133)
    ndl8 = Label(nd, text="", font="helvetica", bg="#FCFF33")
    var1.set(" ")

    def sel2():
        radval2 = str(var2.get())
        ndl9.config(text=radval2)
        if not (ndl9.cget("text") != ""):
            v5.config(text="Blood Group required!")
        else:
            v5.config(text="")

    var2 = StringVar()
    ndr3 = Radiobutton(
        nd, text="A", variable=var2, value="A", command=sel2, bg="#FCFF33"
    )
    ndr3.place(x=120, y=213)
    ndr4 = Radiobutton(
        nd, text="B", variable=var2, value="B", command=sel2, bg="#FCFF33"
    )
    ndr4.place(x=155, y=213)
    ndr5 = Radiobutton(
        nd, text="AB", variable=var2, value="AB", command=sel2, bg="#FCFF33"
    )
    ndr5.place(x=190, y=213)
    ndr1 = Radiobutton(
        nd, text="O", variable=var2, value="O", command=sel2, bg="#FCFF33"
    )
    ndr1.place(x=230, y=213)
    var2.set(" ")
    ndl9 = Label(nd, text="", font="helvetica", bg="#FCFF33")

    def sub():
        a = str(nde1.get())
        b = str(nde2.get())
        f = str(nde3.get())
        d = str(ndl8.cget("text"))
        e = str(ndl9.cget("text"))
        mo1 = re.match(r"^([^0-9]*)$", a)
        mo2 = re.match(r"^(\d?[1-9]|[1-9]0)$", b)
        mo3 = re.match(r"^([^0-9]*)$", f)
        if (
            not (
                nde1.get()
                and nde2.get()
                and nde3.get()
                and ndl8.cget("text") != ""
                and ndl9.cget("text") != ""
            )
        ) or (not (mo1 and mo2 and mo3)):
            if not (nde1.get()):
                v1.config(text="Name required!")
            elif not (mo1):
                v1.config(text="Valid name required!")
            else:
                v1.config(text="")
            if not (nde2.get()):
                v2.config(text="Age required!")
            elif not (mo2):
                v2.config(text="Age must be within 1-99!")
            else:
                v2.config(text="")
            if not (nde3.get()):
                v4.config(text="City required!")
            elif not (mo3):
                v4.config(text="Valid city required!!")
            else:
                v4.config(text="")
            if not (ndl8.cget("text") != ""):
                v3.config(text="Gender required!")
            else:
                v3.config(text="")
            if not (ndl9.cget("text") != ""):
                v5.config(text="Blood Group required!")
            else:
                v5.config(text="")
        else:
            v1.config(text="")
            v2.config(text="")
            v3.config(text="")
            v4.config(text="")
            v5.config(text="")
            answer = messagebox.askquestion(
                "Submit", "Are you sure?", icon="warning", parent=nd
            )
            if answer == "yes":
                conn = sqlite3.connect("test.db")
                c = conn.cursor()
                sql = (
                    "INSERT INTO DonorInfo(dname,age,dgender,dcity,dbldgrp,date) VALUES('"
                    + a
                    + "',"
                    + b
                    + ",'"
                    + d
                    + "','"
                    + f
                    + "','"
                    + e
                    + "',date('now'))"
                )
                try:
                    c.execute(sql)
                    messagebox.showinfo("Success", "Donor's details added!", parent=nd)
                    c.execute("SELECT packet FROM bgpstock WHERE bldgrp='" + e + "'")
                    res = c.fetchone()
                    q = res[0]
                    q += 1
                    q = str(q)
                    c.execute(
                        "UPDATE bgpstock SET packet=" + q + " WHERE bldgrp='" + e + "'"
                    )
                    nd.destroy()
                except:
                    messagebox.showerror("Error", "Unable to add details!", parent=nd)
                finally:
                    conn.commit()
                    c.close()
                    conn.close()

    ndb1 = Button(
        nd,
        text="SUBMIT",
        font="helvetica",
        height=1,
        width=15,
        command=sub,
        bg="#FF3232",
        fg="#FCFF33",
    )
    ndb1.place(x=40, y=290)

    def cancel():
        nd.destroy()

    ndb2 = Button(
        nd,
        text="CANCEL",
        font="helvetica",
        height=1,
        width=15,
        command=cancel,
        bg="#FF3232",
        fg="#FCFF33",
    )
    ndb2.place(x=200, y=290)

    canvas = Canvas(nd, width=170, height=300)
    canvas.place(x=480, y=23)
    canvas.create_image(87, 151, image=img2)


# 2. Donors List
def dlist():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = "SELECT * FROM DonorInfo"
    c.execute(sql)
    result = c.fetchall()
    if not (result):
        messagebox.showerror("Error", "Donor's list is empty!", parent=root)
    else:
        dl = Toplevel(root, bg="#FCFF33")
        dl.title("Donors List")
        dlf1 = LabelFrame(dl, text="Number", font="helvetica", bg="#FCFF33")
        dlf1.grid(row=1, column=1, pady=5)
        dlf2 = LabelFrame(dl, text="Name", font="helvetica", bg="#FCFF33")
        dlf2.grid(row=1, column=2, pady=5)
        dlf3 = LabelFrame(dl, text="Age", font="helvetica", bg="#FCFF33")
        dlf3.grid(row=1, column=3, pady=5)
        dlf4 = LabelFrame(dl, text="Gender", font="helvetica", bg="#FCFF33")
        dlf4.grid(row=1, column=4, pady=5)
        dlf5 = LabelFrame(dl, text="City", font="helvetica", bg="#FCFF33")
        dlf5.grid(row=1, column=5, pady=5)
        dlf6 = LabelFrame(dl, text="Blood Group", font="helvetica", bg="#FCFF33")
        dlf6.grid(row=1, column=6, pady=5)
        dlf7 = LabelFrame(dl, text="Donated Date", font="helvetica", bg="#FCFF33")
        dlf7.grid(row=1, column=7, pady=5)
        try:
            for row in result:
                v1 = row[0]
                v2 = row[1]
                v3 = row[2]
                v4 = row[3]
                v5 = row[4]
                v6 = row[5]
                v7 = row[6]
                dl1 = Label(dlf1, text=v1, font="helvetica", bg="#FCFF33")
                dl1.pack()
                dl2 = Label(dlf2, text=v2, font="helvetica", bg="#FCFF33")
                dl2.pack()
                dl3 = Label(dlf3, text=v3, font="helvetica", bg="#FCFF33")
                dl3.pack()
                dl4 = Label(dlf4, text=v4, font="helvetica", bg="#FCFF33")
                dl4.pack()
                dl5 = Label(dlf5, text=v5, font="helvetica", bg="#FCFF33")
                dl5.pack()
                dl6 = Label(dlf6, text=v6, font="helvetica", bg="#FCFF33")
                dl6.pack()
                dl7 = Label(dlf7, text=v7, font="helvetica", bg="#FCFF33")
                dl7.pack()
        except:
            messagebox.showerror(
                "Error", "Unable to show donor's information!", parent=dl
            )
    conn.commit()
    c.close()
    conn.close()


# 3. Search Donor
def searchdonor():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = "SELECT * FROM DonorInfo"
    c.execute(sql)
    result = c.fetchall()
    if not (result):
        messagebox.showerror("Error", "Donor's list is empty!", parent=root)
    else:
        sd = Toplevel(root, bg="black")
        sd.title("Search Donor")
        sd.geometry("680x325")
        canvas = Canvas(sd, width=300, height=300)
        canvas.place(x=10, y=10)
        canvas.create_image(153, 153, image=img4)

        labelfont = ("times", 30, "bold")
        l1 = Label(
            sd, text="Search Donor By : ", font=labelfont, bg="black", fg="white"
        )
        l1.place(x=330, y=10)

        def sel():
            radval = str(var1.get())
            if radval == "dno":
                dno = Toplevel(sd, bg="black")
                dno.title("Search Donor By : Donor Number")
                dno.geometry("535x100")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dno.destroy()

                dno.protocol("WM_DELETE_WINDOW", delwin)
                dnol1 = Label(
                    dno,
                    text="Enter Donor Number  : ",
                    font="helvetica",
                    fg="white",
                    bg="black",
                )
                dnol1.place(x=10, y=10)
                v = Label(dno, font="helvetica", fg="red", bg="black")
                v.place(x=320, y=10)

                def checknum(cn):
                    mo1 = re.match(r"^[0-9]*$", cn.get())
                    if not (cn.get()):
                        v.config(text="Donor Number required!")
                    elif not (mo1):
                        v.config(text="Enter a valid Donor Number!")
                    else:
                        v.config(text="")

                cn = StringVar()
                cn.trace("w", lambda name, index, mode, cn=cn: checknum(cn))
                dnoe1 = Entry(dno, bd=3, textvariable=cn)
                dnoe1.place(x=180, y=10)

                def search():
                    a = str(dnoe1.get())
                    mo1 = re.match(r"^[0-9]*$", a)
                    if not (dnoe1.get()) or not (mo1):
                        if not (dnoe1.get()):
                            v.config(text="Donor's Number required!")
                        elif not (mo1):
                            v.config(text="Enter a valid Donor Number!")
                        else:
                            v.config(text="")
                    else:
                        v.config(text="")
                        answer = messagebox.askquestion(
                            "Search", "Are you sure?", icon="warning", parent=dno
                        )
                        if answer == "yes":
                            conn = sqlite3.connect("test.db")
                            c = conn.cursor()
                            sql = "SELECT * FROM DonorInfo WHERE dno=" + a
                            try:
                                c.execute(sql)
                                result = c.fetchall()
                                if not (result):
                                    messagebox.showerror(
                                        "Error",
                                        "Donor having Donor Number : "
                                        + a
                                        + " is not in the Donors List!",
                                        parent=dno,
                                    )
                                else:
                                    dl = Toplevel(root, bg="black")
                                    dl.title("Donor Found : Donor Number - " + a)
                                    dno.destroy()

                                    def delwin():
                                        sd.deiconify()
                                        dl.destroy()

                                    dl.protocol("WM_DELETE_WINDOW", delwin)
                                    dlf1 = LabelFrame(
                                        dl,
                                        text="Number",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf1.grid(row=1, column=1, pady=5)
                                    dlf2 = LabelFrame(
                                        dl,
                                        text="Name",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf2.grid(row=1, column=2, pady=5)
                                    dlf3 = LabelFrame(
                                        dl,
                                        text="Age",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf3.grid(row=1, column=3, pady=5)
                                    dlf4 = LabelFrame(
                                        dl,
                                        text="Gender",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf4.grid(row=1, column=4, pady=5)
                                    dlf5 = LabelFrame(
                                        dl,
                                        text="City",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf5.grid(row=1, column=5, pady=5)
                                    dlf6 = LabelFrame(
                                        dl,
                                        text="Blood Group",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf6.grid(row=1, column=6, pady=5)
                                    dlf7 = LabelFrame(
                                        dl,
                                        text="Donated Date",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf7.grid(row=1, column=7, pady=5)
                                    try:
                                        for row in result:
                                            v1 = row[0]
                                            v2 = row[1]
                                            v3 = row[2]
                                            v4 = row[3]
                                            v5 = row[4]
                                            v6 = row[5]
                                            v7 = row[6]
                                            dl1 = Label(
                                                dlf1,
                                                text=v1,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl1.pack()
                                            dl2 = Label(
                                                dlf2,
                                                text=v2,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl2.pack()
                                            dl3 = Label(
                                                dlf3,
                                                text=v3,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl3.pack()
                                            dl4 = Label(
                                                dlf4,
                                                text=v4,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl4.pack()
                                            dl5 = Label(
                                                dlf5,
                                                text=v5,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl5.pack()
                                            dl6 = Label(
                                                dlf6,
                                                text=v6,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl6.pack()
                                            dl7 = Label(
                                                dlf7,
                                                text=v7,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl7.pack()
                                    except:
                                        messagebox.showerror(
                                            "Error",
                                            "Unable to show donor's information!",
                                            parent=dl,
                                        )
                            finally:
                                conn.commit()
                                c.close()
                                conn.close()

                def canc():
                    dno.destroy()
                    sd.deiconify()

                dnob1 = Button(
                    dno,
                    text="SEARCH",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=search,
                    bg="white",
                    fg="black",
                )
                dnob1.place(x=140, y=50)
                dnob2 = Button(
                    dno,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=canc,
                    bg="white",
                    fg="black",
                )
                dnob2.place(x=300, y=50)

            if radval == "dname":
                dname = Toplevel(sd, bg="black")
                dname.title("Search Donor By : Name")
                dname.geometry("535x100")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dname.destroy()

                dname.protocol("WM_DELETE_WINDOW", delwin)
                dnamel1 = Label(
                    dname,
                    text="Enter Donor's Name  : ",
                    font="helvetica",
                    fg="white",
                    bg="black",
                )
                dnamel1.place(x=10, y=10)
                v = Label(dname, font="helvetica", fg="red", bg="black")
                v.place(x=320, y=10)

                def checknum(cn):
                    mo1 = re.match(r"^([^0-9]*)$", cn.get())
                    if not (cn.get()):
                        v.config(text="Donor's Name required!")
                    elif not (mo1):
                        v.config(text="Enter a valid name!")
                    else:
                        v.config(text="")

                cn = StringVar()
                cn.trace("w", lambda name, index, mode, cn=cn: checknum(cn))
                dnamee1 = Entry(dname, bd=3, textvariable=cn)
                dnamee1.place(x=180, y=10)

                def search():
                    a = str(dnamee1.get())
                    mo1 = re.match(r"^([^0-9]*)$", a)
                    if not (dnamee1.get()) or not (mo1):
                        if not (dnamee1.get()):
                            v.config(text="Donor's Name required!")
                        elif not (mo1):
                            v.config(text="Enter a valid name!")
                        else:
                            v.config(text="")
                    else:
                        v.config(text="")
                        answer = messagebox.askquestion(
                            "Search", "Are you sure?", icon="warning", parent=dname
                        )
                        if answer == "yes":
                            conn = sqlite3.connect("test.db")
                            c = conn.cursor()
                            sql = "SELECT * FROM DonorInfo WHERE dname='" + a + "'"
                            try:
                                c.execute(sql)
                                result = c.fetchall()
                                if not (result):
                                    messagebox.showerror(
                                        "Error",
                                        "Donor having name : "
                                        + a
                                        + " is not in the Donors List",
                                        parent=dname,
                                    )
                                else:
                                    dl = Toplevel(root, bg="black")
                                    dl.title("Donor Found : Donor Name - " + a)
                                    dname.destroy()

                                    def delwin():
                                        sd.deiconify()
                                        dl.destroy()

                                    dl.protocol("WM_DELETE_WINDOW", delwin)
                                    dlf1 = LabelFrame(
                                        dl,
                                        text="Number",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf1.grid(row=1, column=1, pady=5)
                                    dlf2 = LabelFrame(
                                        dl,
                                        text="Name",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf2.grid(row=1, column=2, pady=5)
                                    dlf3 = LabelFrame(
                                        dl,
                                        text="Age",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf3.grid(row=1, column=3, pady=5)
                                    dlf4 = LabelFrame(
                                        dl,
                                        text="Gender",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf4.grid(row=1, column=4, pady=5)
                                    dlf5 = LabelFrame(
                                        dl,
                                        text="City",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf5.grid(row=1, column=5, pady=5)
                                    dlf6 = LabelFrame(
                                        dl,
                                        text="Blood Group",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf6.grid(row=1, column=6, pady=5)
                                    dlf7 = LabelFrame(
                                        dl,
                                        text="Donated Date",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf7.grid(row=1, column=7, pady=5)
                                    try:
                                        for row in result:
                                            v1 = row[0]
                                            v2 = row[1]
                                            v3 = row[2]
                                            v4 = row[3]
                                            v5 = row[4]
                                            v6 = row[5]
                                            v7 = row[6]
                                            dl1 = Label(
                                                dlf1,
                                                text=v1,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl1.pack()
                                            dl2 = Label(
                                                dlf2,
                                                text=v2,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl2.pack()
                                            dl3 = Label(
                                                dlf3,
                                                text=v3,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl3.pack()
                                            dl4 = Label(
                                                dlf4,
                                                text=v4,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl4.pack()
                                            dl5 = Label(
                                                dlf5,
                                                text=v5,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl5.pack()
                                            dl6 = Label(
                                                dlf6,
                                                text=v6,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl6.pack()
                                            dl7 = Label(
                                                dlf7,
                                                text=v7,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl7.pack()
                                    except:
                                        messagebox.showerror(
                                            "Error",
                                            "Unable to show donor's information!",
                                            parent=dl,
                                        )
                            finally:
                                conn.commit()
                                c.close()
                                conn.close()

                def canc():
                    dname.destroy()
                    sd.deiconify()

                dnameb1 = Button(
                    dname,
                    text="SEARCH",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=search,
                    bg="white",
                    fg="black",
                )
                dnameb1.place(x=140, y=50)
                dnameb2 = Button(
                    dname,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=canc,
                    bg="white",
                    fg="black",
                )
                dnameb2.place(x=300, y=50)

            if radval == "dage":
                dage = Toplevel(sd, bg="black")
                dage.title("Search Donor By : Donor's Age")
                dage.geometry("535x100")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dage.destroy()

                dage.protocol("WM_DELETE_WINDOW", delwin)
                dagel1 = Label(
                    dage,
                    text="Enter Donor's Age   : ",
                    font="helvetica",
                    fg="white",
                    bg="black",
                )
                dagel1.place(x=10, y=10)
                v = Label(dage, font="helvetica", fg="red", bg="black")
                v.place(x=320, y=10)

                def checknum(cn):
                    mo1 = re.match(r"^(\d?[1-9]|[1-9]0)$", cn.get())
                    if not (cn.get()):
                        v.config(text="Donor's age required!")
                    elif not (mo1):
                        v.config(text="Enter a valid age!")
                    else:
                        v.config(text="")

                cn = StringVar()
                cn.trace("w", lambda name, index, mode, cn=cn: checknum(cn))
                dagee1 = Entry(dage, bd=3, textvariable=cn)
                dagee1.place(x=180, y=10)

                def search():
                    a = str(dagee1.get())
                    mo1 = re.match(r"^(\d?[1-9]|[1-9]0)$", a)
                    if not (dagee1.get()) or not (mo1):
                        if not (dagee1.get()):
                            v.config(text="Donor's age required!")
                        elif not (mo1):
                            v.config(text="Enter a valid age!")
                        else:
                            v.config(text="")
                    else:
                        v.config(text="")
                        answer = messagebox.askquestion(
                            "Search", "Are you sure?", icon="warning", parent=dage
                        )
                        if answer == "yes":
                            conn = sqlite3.connect("test.db")
                            c = conn.cursor()
                            sql = "SELECT * FROM DonorInfo WHERE age=" + a
                            try:
                                c.execute(sql)
                                result = c.fetchall()
                                if not (result):
                                    messagebox.showerror(
                                        "Error",
                                        "Donor having age : "
                                        + a
                                        + " is not in the Donors List",
                                        parent=dage,
                                    )
                                else:
                                    dl = Toplevel(root, bg="black")
                                    dl.title("Donor Found : Donor Age - " + a)
                                    dage.destroy()

                                    def delwin():
                                        sd.deiconify()
                                        dl.destroy()

                                    dl.protocol("WM_DELETE_WINDOW", delwin)
                                    dlf1 = LabelFrame(
                                        dl,
                                        text="Number",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf1.grid(row=1, column=1, pady=5)
                                    dlf2 = LabelFrame(
                                        dl,
                                        text="Name",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf2.grid(row=1, column=2, pady=5)
                                    dlf3 = LabelFrame(
                                        dl,
                                        text="Age",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf3.grid(row=1, column=3, pady=5)
                                    dlf4 = LabelFrame(
                                        dl,
                                        text="Gender",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf4.grid(row=1, column=4, pady=5)
                                    dlf5 = LabelFrame(
                                        dl,
                                        text="City",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf5.grid(row=1, column=5, pady=5)
                                    dlf6 = LabelFrame(
                                        dl,
                                        text="Blood Group",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf6.grid(row=1, column=6, pady=5)
                                    dlf7 = LabelFrame(
                                        dl,
                                        text="Donated Date",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf7.grid(row=1, column=7, pady=5)
                                    try:
                                        for row in result:
                                            v1 = row[0]
                                            v2 = row[1]
                                            v3 = row[2]
                                            v4 = row[3]
                                            v5 = row[4]
                                            v6 = row[5]
                                            v7 = row[6]
                                            dl1 = Label(
                                                dlf1,
                                                text=v1,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl1.pack()
                                            dl2 = Label(
                                                dlf2,
                                                text=v2,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl2.pack()
                                            dl3 = Label(
                                                dlf3,
                                                text=v3,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl3.pack()
                                            dl4 = Label(
                                                dlf4,
                                                text=v4,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl4.pack()
                                            dl5 = Label(
                                                dlf5,
                                                text=v5,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl5.pack()
                                            dl6 = Label(
                                                dlf6,
                                                text=v6,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl6.pack()
                                            dl7 = Label(
                                                dlf7,
                                                text=v7,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl7.pack()
                                    except:
                                        messagebox.showerror(
                                            "Error",
                                            "Unable to show donor's information!",
                                            parent=dl,
                                        )
                            finally:
                                conn.commit()
                                c.close()
                                conn.close()

                def canc():
                    dage.destroy()
                    sd.deiconify()

                dageb1 = Button(
                    dage,
                    text="SEARCH",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=search,
                    bg="white",
                    fg="black",
                )
                dageb1.place(x=140, y=50)
                dageb2 = Button(
                    dage,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=canc,
                    bg="white",
                    fg="black",
                )
                dageb2.place(x=300, y=50)

            if radval == "dbg":
                dbg = Toplevel(sd, bg="black")
                dbg.title("Search Donor By : Blood Group")
                dbg.geometry("300x250")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dbg.destroy()

                dbg.protocol("WM_DELETE_WINDOW", delwin)

                labelfont = ("times", 15, "bold")
                dbgl1 = Label(
                    dbg,
                    text="Select a Blood Group :",
                    font=labelfont,
                    bg="black",
                    fg="white",
                )
                dbgl1.place(x=10, y=10)

                def dbgsel():
                    dbgradval = str(dbgvar1.get())
                    conn = sqlite3.connect("test.db")
                    c = conn.cursor()
                    sql = "SELECT * FROM DonorInfo WHERE dbldgrp='" + dbgradval + "'"
                    try:
                        c.execute(sql)
                        result = c.fetchall()
                        if not (result):
                            messagebox.showerror(
                                "Error",
                                "Donor having blood group : "
                                + dbgradval
                                + " is not in the Donors List",
                                parent=dbg,
                            )
                        else:
                            dl = Toplevel(root, bg="black")
                            dl.title("Donor Found : Blood Group - " + dbgradval)
                            dbg.iconify()

                            def delwin():
                                dbg.deiconify()
                                dl.destroy()

                            dl.protocol("WM_DELETE_WINDOW", delwin)
                            dlf1 = LabelFrame(
                                dl,
                                text="Number",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf1.grid(row=1, column=1, pady=5)
                            dlf2 = LabelFrame(
                                dl,
                                text="Name",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf2.grid(row=1, column=2, pady=5)
                            dlf3 = LabelFrame(
                                dl, text="Age", font="helvetica", bg="black", fg="white"
                            )
                            dlf3.grid(row=1, column=3, pady=5)
                            dlf4 = LabelFrame(
                                dl,
                                text="Gender",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf4.grid(row=1, column=4, pady=5)
                            dlf5 = LabelFrame(
                                dl,
                                text="City",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf5.grid(row=1, column=5, pady=5)
                            dlf6 = LabelFrame(
                                dl,
                                text="Blood Group",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf6.grid(row=1, column=6, pady=5)
                            dlf7 = LabelFrame(
                                dl,
                                text="Donated Date",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf7.grid(row=1, column=7, pady=5)
                            try:
                                for row in result:
                                    v1 = row[0]
                                    v2 = row[1]
                                    v3 = row[2]
                                    v4 = row[3]
                                    v5 = row[4]
                                    v6 = row[5]
                                    v7 = row[6]
                                    dl1 = Label(
                                        dlf1,
                                        text=v1,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl1.pack()
                                    dl2 = Label(
                                        dlf2,
                                        text=v2,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl2.pack()
                                    dl3 = Label(
                                        dlf3,
                                        text=v3,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl3.pack()
                                    dl4 = Label(
                                        dlf4,
                                        text=v4,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl4.pack()
                                    dl5 = Label(
                                        dlf5,
                                        text=v5,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl5.pack()
                                    dl6 = Label(
                                        dlf6,
                                        text=v6,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl6.pack()
                                    dl7 = Label(
                                        dlf7,
                                        text=v7,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl7.pack()
                            except:
                                messagebox.showerror(
                                    "Error",
                                    "Unable to show donor's information!",
                                    parent=dl,
                                )
                    finally:
                        conn.commit()
                        c.close()
                        conn.close()

                dbgvar1 = StringVar()
                dbgradiofont = ("helvetica", 13, "bold")
                dbgr1 = Radiobutton(
                    dbg,
                    text="A",
                    variable=dbgvar1,
                    value="A",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr1.place(x=10, y=40)
                dbgr2 = Radiobutton(
                    dbg,
                    text="B",
                    variable=dbgvar1,
                    value="B",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr2.place(x=10, y=80)
                dbgr3 = Radiobutton(
                    dbg,
                    text="AB",
                    variable=dbgvar1,
                    value="AB",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr3.place(x=10, y=120)
                dbgr4 = Radiobutton(
                    dbg,
                    text="O",
                    variable=dbgvar1,
                    value="O",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr4.place(x=10, y=160)

                def dbgcanc():
                    dbg.destroy()
                    sd.deiconify()

                dbgb1 = Button(
                    dbg,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=dbgcanc,
                    bg="white",
                    fg="black",
                )
                dbgb1.place(x=10, y=200)
                dbgvar1.set(" ")

        var1 = StringVar()
        radiofont = ("helvetica", 15, "bold")
        r1 = Radiobutton(
            sd,
            text="Donor Number",
            variable=var1,
            value="dno",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r1.place(x=330, y=80)
        r2 = Radiobutton(
            sd,
            text="Name",
            variable=var1,
            value="dname",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r2.place(x=330, y=125)
        r3 = Radiobutton(
            sd,
            text="Age",
            variable=var1,
            value="dage",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r3.place(x=330, y=170)
        r4 = Radiobutton(
            sd,
            text="Blood Group",
            variable=var1,
            value="dbg",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r4.place(x=330, y=215)
        l8 = Label(sd, text="", font="helvetica", bg="#FCFF33")
        var1.set(" ")

        def cancel():
            sd.destroy()

        b1 = Button(
            sd,
            text="CANCEL",
            font="helvetica",
            height=1,
            width=10,
            command=cancel,
            bg="white",
            fg="black",
        )
        b1.place(x=330, y=270)


# 4. Sell Blood Packet
def sbp():
    nd = Toplevel(root, bg="#FCFF33")
    nd.title("Buyer's Details Form")
    nd.geometry("680x350")

    ndl1 = Label(nd, text="Number : ", font="helvetica", bg="#FCFF33")
    ndl1.place(x=45, y=10)
    ndl2 = Label(nd, text="Name : ", font="helvetica", bg="#FCFF33")
    ndl2.place(x=58, y=50)
    ndl3 = Label(nd, text="Age : ", font="helvetica", bg="#FCFF33")
    ndl3.place(x=72, y=90)
    ndl4 = Label(nd, text="Gender : ", font="helvetica", bg="#FCFF33")
    ndl4.place(x=50, y=130)
    ndl5 = Label(nd, text="City : ", font="helvetica", bg="#FCFF33")
    ndl5.place(x=75, y=170)
    ndl6 = Label(nd, text=" Blood Packet : ", font="helvetica", bg="#FCFF33")
    ndl6.place(x=10, y=210)
    ndl7 = Label(nd, text="Today's Date : ", font="helvetica", bg="#FCFF33")
    ndl7.place(x=10, y=250)

    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("SELECT MAX(ROWID) FROM BuyerInfo")
    res = c.fetchone()
    ndal1 = Label(nd, font="helvetica", bg="#FCFF33")
    ndal1.place(x=120, y=10)
    if res[0] == None:
        ndal1.config(text="1")
    else:
        a = int(res[0])
        a += 1
        ndal1.config(text=a)
    ndal2 = Label(nd, text="demo", font="helvetica", bg="#FCFF33")
    ndal2.place(x=120, y=250)
    c.execute("SELECT date('now')")
    res1 = c.fetchone()
    a1 = res1[0]
    ndal2.config(text=a1)

    vfont = ("helvetica", 13, "bold")
    v1 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v1.place(x=270, y=50)
    v2 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v2.place(x=270, y=90)
    v3 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v3.place(x=270, y=130)
    v4 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v4.place(x=270, y=170)
    v5 = Label(nd, font=vfont, fg="#FF3232", bg="#FCFF33")
    v5.place(x=270, y=210)

    def checkname(cn):
        mo1 = re.match(r"^([^0-9]*)$", cn.get())
        if not (cn.get()):
            v1.config(text="Name required!")
        elif not (mo1):
            v1.config(text="Valid name required!")
        else:
            v1.config(text="")

    cn = StringVar()
    cn.trace("w", lambda name, index, mode, cn=cn: checkname(cn))
    nde1 = Entry(nd, bd=3, textvariable=cn)
    nde1.place(x=120, y=53)

    def checkage(ca):
        mo2 = re.match(r"^(\d?[1-9]|[1-9]0)$", ca.get())
        if not (ca.get()):
            v2.config(text="Age required!")
        elif not (mo2):
            v2.config(text="Age must be within 1-99!")
        else:
            v2.config(text="")

    ca = StringVar()
    ca.trace("w", lambda name, index, mode, cn=cn: checkage(ca))
    nde2 = Entry(nd, bd=3, textvariable=ca)
    nde2.place(x=120, y=93)

    def checkcity(cc):
        mo3 = re.match(r"^([^0-9]*)$", cc.get())
        if not (cc.get()):
            v4.config(text="City required!")
        elif not (mo3):
            v4.config(text="Valid city name required!")
        else:
            v4.config(text="")

    cc = StringVar()
    cc.trace("w", lambda name, index, mode, cn=cn: checkcity(cc))
    nde3 = Entry(nd, bd=3, textvariable=cc)
    nde3.place(x=120, y=173)

    def sel1():
        radval1 = str(var1.get())
        ndl8.config(text=radval1)
        if not (ndl8.cget("text") != ""):
            v3.config(text="Gender required!")
        else:
            v3.config(text="")

    var1 = StringVar()
    ndr1 = Radiobutton(
        nd, text="Male", variable=var1, value="Male", command=sel1, bg="#FCFF33"
    )
    ndr1.place(x=120, y=133)
    ndr2 = Radiobutton(
        nd, text="Female", variable=var1, value="Female", command=sel1, bg="#FCFF33"
    )
    ndr2.place(x=180, y=133)
    ndl8 = Label(nd, text="", font="helvetica", bg="#FCFF33")
    var1.set(" ")

    def sel2():
        radval2 = str(var2.get())
        ndl9.config(text=radval2)
        if not (ndl9.cget("text") != ""):
            v5.config(text="Blood Packet required!")
        else:
            v5.config(text="")

    var2 = StringVar()
    ndr3 = Radiobutton(
        nd, text="A", variable=var2, value="A", command=sel2, bg="#FCFF33"
    )
    ndr3.place(x=120, y=213)
    ndr4 = Radiobutton(
        nd, text="B", variable=var2, value="B", command=sel2, bg="#FCFF33"
    )
    ndr4.place(x=155, y=213)
    ndr5 = Radiobutton(
        nd, text="AB", variable=var2, value="AB", command=sel2, bg="#FCFF33"
    )
    ndr5.place(x=190, y=213)
    ndr1 = Radiobutton(
        nd, text="O", variable=var2, value="O", command=sel2, bg="#FCFF33"
    )
    ndr1.place(x=230, y=213)
    var2.set(" ")
    ndl9 = Label(nd, text="", font="helvetica", bg="#FCFF33")

    def sub():
        a = str(nde1.get())
        b = str(nde2.get())
        f = str(nde3.get())
        d = str(ndl8.cget("text"))
        e = str(ndl9.cget("text"))
        mo1 = re.match(r"^([^0-9]*)$", a)
        mo2 = re.match(r"^(\d?[1-9]|[1-9]0)$", b)
        mo3 = re.match(r"^([^0-9]*)$", f)
        if (
            not (
                nde1.get()
                and nde2.get()
                and nde3.get()
                and ndl8.cget("text") != ""
                and ndl9.cget("text") != ""
            )
        ) or (not (mo1 and mo2 and mo3)):
            if not (nde1.get()):
                v1.config(text="Name required!")
            elif not (mo1):
                v1.config(text="Valid name required!")
            else:
                v1.config(text="")
            if not (nde2.get()):
                v2.config(text="Age required!")
            elif not (mo2):
                v2.config(text="Age must be within 1-99!")
            else:
                v2.config(text="")
            if not (nde3.get()):
                v4.config(text="City required!")
            elif not (mo3):
                v4.config(text="Valid city required!!")
            else:
                v4.config(text="")
            if not (ndl8.cget("text") != ""):
                v3.config(text="Gender required!")
            else:
                v3.config(text="")
            if not (ndl9.cget("text") != ""):
                v5.config(text="Blood Packet required!")
            else:
                v5.config(text="")

        else:
            v1.config(text="")
            v2.config(text="")
            v3.config(text="")
            v4.config(text="")
            v5.config(text="")
            answer = messagebox.askquestion(
                "Submit", "Are you sure?", icon="warning", parent=nd
            )
            if answer == "yes":
                conn = sqlite3.connect("test.db")
                c = conn.cursor()
                try:
                    c.execute("SELECT packet FROM bgpstock WHERE bldgrp='" + e + "'")
                    res = c.fetchone()
                    q = res[0]
                    if q == 0:
                        messagebox.showerror(
                            "Error", "Blood packet out of stock!", parent=nd
                        )
                    else:
                        sql = (
                            "INSERT INTO BuyerInfo(bname,age,bgender,bcity,bbldgrp,date) VALUES('"
                            + a
                            + "',"
                            + b
                            + ",'"
                            + d
                            + "','"
                            + f
                            + "','"
                            + e
                            + "',date('now'))"
                        )
                        c.execute(sql)
                        messagebox.showinfo(
                            "Success", "Buyer's details added!", parent=nd
                        )

                        q -= 1
                        q = str(q)
                        c.execute(
                            "UPDATE bgpstock SET packet="
                            + q
                            + " WHERE bldgrp='"
                            + e
                            + "'"
                        )
                        nd.destroy()
                except:
                    messagebox.showerror("Error", "Unable to add details!", parent=nd)
                finally:
                    conn.commit()
                    c.close()
                    conn.close()

    ndb1 = Button(
        nd,
        text="SUBMIT",
        font="helvetica",
        height=1,
        width=15,
        command=sub,
        bg="#FF3232",
        fg="#FCFF33",
    )
    ndb1.place(x=40, y=290)

    def cancel():
        nd.destroy()

    ndb2 = Button(
        nd,
        text="CANCEL",
        font="helvetica",
        height=1,
        width=15,
        command=cancel,
        bg="#FF3232",
        fg="#FCFF33",
    )
    ndb2.place(x=200, y=290)

    canvas = Canvas(nd, width=170, height=300)
    canvas.place(x=480, y=23)
    canvas.create_image(87, 151, image=img2)


# 5. Buyers List
def blist():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = "SELECT * FROM BuyerInfo"
    c.execute(sql)
    result = c.fetchall()
    if not (result):
        messagebox.showerror("Error", "Buyer's list is empty!", parent=root)
    else:
        dl = Toplevel(root, bg="#FCFF33")
        dl.title("Buyers List")
        dlf1 = LabelFrame(dl, text="Number", font="helvetica", bg="#FCFF33")
        dlf1.grid(row=1, column=1, pady=5)
        dlf2 = LabelFrame(dl, text="Name", font="helvetica", bg="#FCFF33")
        dlf2.grid(row=1, column=2, pady=5)
        dlf3 = LabelFrame(dl, text="Age", font="helvetica", bg="#FCFF33")
        dlf3.grid(row=1, column=3, pady=5)
        dlf4 = LabelFrame(dl, text="Gender", font="helvetica", bg="#FCFF33")
        dlf4.grid(row=1, column=4, pady=5)
        dlf5 = LabelFrame(dl, text="City", font="helvetica", bg="#FCFF33")
        dlf5.grid(row=1, column=5, pady=5)
        dlf6 = LabelFrame(dl, text="Blood Packet", font="helvetica", bg="#FCFF33")
        dlf6.grid(row=1, column=6, pady=5)
        dlf7 = LabelFrame(dl, text="Purchase Date", font="helvetica", bg="#FCFF33")
        dlf7.grid(row=1, column=7, pady=5)
        try:
            for row in result:
                v1 = row[0]
                v2 = row[1]
                v3 = row[2]
                v4 = row[3]
                v5 = row[4]
                v6 = row[5]
                v7 = row[6]
                dl1 = Label(dlf1, text=v1, font="helvetica", bg="#FCFF33")
                dl1.pack()
                dl2 = Label(dlf2, text=v2, font="helvetica", bg="#FCFF33")
                dl2.pack()
                dl3 = Label(dlf3, text=v3, font="helvetica", bg="#FCFF33")
                dl3.pack()
                dl4 = Label(dlf4, text=v4, font="helvetica", bg="#FCFF33")
                dl4.pack()
                dl5 = Label(dlf5, text=v5, font="helvetica", bg="#FCFF33")
                dl5.pack()
                dl6 = Label(dlf6, text=v6, font="helvetica", bg="#FCFF33")
                dl6.pack()
                dl7 = Label(dlf7, text=v7, font="helvetica", bg="#FCFF33")
                dl7.pack()
        except:
            messagebox.showerror(
                "Error", "Unable to show buyer's information!", parent=dl
            )
    conn.commit()
    c.close()
    conn.close()


# 6. Search Buyer
def searchbuyer():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = "SELECT * FROM BuyerInfo"
    c.execute(sql)
    result = c.fetchall()
    if not (result):
        messagebox.showerror("Error", "Buyer's list is empty!", parent=root)
    else:
        sd = Toplevel(root, bg="black")
        sd.title("Search Buyer")
        sd.geometry("680x325")
        canvas = Canvas(sd, width=300, height=300)
        canvas.place(x=10, y=10)
        canvas.create_image(153, 153, image=img4)

        labelfont = ("times", 30, "bold")
        l1 = Label(
            sd, text="Search Buyer By : ", font=labelfont, bg="black", fg="white"
        )
        l1.place(x=330, y=10)

        def sel():
            radval = str(var1.get())
            if radval == "dno":
                dno = Toplevel(sd, bg="black")
                dno.title("Search Buyer By : Buyer Number")
                dno.geometry("535x100")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dno.destroy()

                dno.protocol("WM_DELETE_WINDOW", delwin)
                dnol1 = Label(
                    dno,
                    text="Enter Buyer Number  : ",
                    font="helvetica",
                    fg="white",
                    bg="black",
                )
                dnol1.place(x=10, y=10)
                v = Label(dno, font="helvetica", fg="red", bg="black")
                v.place(x=320, y=10)

                def checknum(cn):
                    mo1 = re.match(r"^[0-9]*$", cn.get())
                    if not (cn.get()):
                        v.config(text="Buyer's Number required!")
                    elif not (mo1):
                        v.config(text="Enter a valid Buyer Number!")
                    else:
                        v.config(text="")

                cn = StringVar()
                cn.trace("w", lambda name, index, mode, cn=cn: checknum(cn))
                dnoe1 = Entry(dno, bd=3, textvariable=cn)
                dnoe1.place(x=180, y=10)

                def search():
                    a = str(dnoe1.get())
                    mo1 = re.match(r"^[0-9]*$", a)
                    if not (dnoe1.get()) or not (mo1):
                        if not (dnoe1.get()):
                            v.config(text="Buyer's Number required!")
                        elif not (mo1):
                            v.config(text="Enter a valid Buyer Number!")
                        else:
                            v.config(text="")
                    else:
                        v.config(text="")
                        answer = messagebox.askquestion(
                            "Search", "Are you sure?", icon="warning", parent=dno
                        )
                        if answer == "yes":
                            conn = sqlite3.connect("test.db")
                            c = conn.cursor()
                            sql = "SELECT * FROM BuyerInfo WHERE bno=" + a
                            try:
                                c.execute(sql)
                                result = c.fetchall()
                                if not (result):
                                    messagebox.showerror(
                                        "Error",
                                        "Buyer having Buyer Number : "
                                        + a
                                        + " is not in the Buyers List!",
                                        parent=dno,
                                    )
                                else:
                                    dl = Toplevel(root, bg="black")
                                    dl.title("Buyer Found : Buyer Number - " + a)
                                    dno.destroy()

                                    def delwin():
                                        sd.deiconify()
                                        dl.destroy()

                                    dl.protocol("WM_DELETE_WINDOW", delwin)
                                    dlf1 = LabelFrame(
                                        dl,
                                        text="Number",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf1.grid(row=1, column=1, pady=5)
                                    dlf2 = LabelFrame(
                                        dl,
                                        text="Name",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf2.grid(row=1, column=2, pady=5)
                                    dlf3 = LabelFrame(
                                        dl,
                                        text="Age",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf3.grid(row=1, column=3, pady=5)
                                    dlf4 = LabelFrame(
                                        dl,
                                        text="Gender",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf4.grid(row=1, column=4, pady=5)
                                    dlf5 = LabelFrame(
                                        dl,
                                        text="City",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf5.grid(row=1, column=5, pady=5)
                                    dlf6 = LabelFrame(
                                        dl,
                                        text="Blood Packet",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf6.grid(row=1, column=6, pady=5)
                                    dlf7 = LabelFrame(
                                        dl,
                                        text="Purchase Date",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf7.grid(row=1, column=7, pady=5)
                                    try:
                                        for row in result:
                                            v1 = row[0]
                                            v2 = row[1]
                                            v3 = row[2]
                                            v4 = row[3]
                                            v5 = row[4]
                                            v6 = row[5]
                                            v7 = row[6]
                                            dl1 = Label(
                                                dlf1,
                                                text=v1,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl1.pack()
                                            dl2 = Label(
                                                dlf2,
                                                text=v2,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl2.pack()
                                            dl3 = Label(
                                                dlf3,
                                                text=v3,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl3.pack()
                                            dl4 = Label(
                                                dlf4,
                                                text=v4,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl4.pack()
                                            dl5 = Label(
                                                dlf5,
                                                text=v5,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl5.pack()
                                            dl6 = Label(
                                                dlf6,
                                                text=v6,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl6.pack()
                                            dl7 = Label(
                                                dlf7,
                                                text=v7,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl7.pack()
                                    except:
                                        messagebox.showerror(
                                            "Error",
                                            "Unable to show buyer's information!",
                                            parent=dl,
                                        )
                            finally:
                                conn.commit()
                                c.close()
                                conn.close()

                def canc():
                    dno.destroy()
                    sd.deiconify()

                dnob1 = Button(
                    dno,
                    text="SEARCH",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=search,
                    bg="white",
                    fg="black",
                )
                dnob1.place(x=140, y=50)
                dnob2 = Button(
                    dno,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=canc,
                    bg="white",
                    fg="black",
                )
                dnob2.place(x=300, y=50)

            if radval == "dname":
                dname = Toplevel(sd, bg="black")
                dname.title("Search Buyer By : Name")
                dname.geometry("535x100")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dname.destroy()

                dname.protocol("WM_DELETE_WINDOW", delwin)
                dnamel1 = Label(
                    dname,
                    text="Enter Buyer's Name  : ",
                    font="helvetica",
                    fg="white",
                    bg="black",
                )
                dnamel1.place(x=10, y=10)
                v = Label(dname, font="helvetica", fg="red", bg="black")
                v.place(x=320, y=10)

                def checknum(cn):
                    mo1 = re.match(r"^([^0-9]*)$", cn.get())
                    if not (cn.get()):
                        v.config(text="Buyer's Name required!")
                    elif not (mo1):
                        v.config(text="Enter a valid name!")
                    else:
                        v.config(text="")

                cn = StringVar()
                cn.trace("w", lambda name, index, mode, cn=cn: checknum(cn))
                dnamee1 = Entry(dname, bd=3, textvariable=cn)
                dnamee1.place(x=180, y=10)

                def search():
                    a = str(dnamee1.get())
                    mo1 = re.match(r"^([^0-9]*)$", a)
                    if not (dnamee1.get()) or not (mo1):
                        if not (dnamee1.get()):
                            v.config(text="Buyer's Name required!")
                        elif not (mo1):
                            v.config(text="Enter a valid name!")
                        else:
                            v.config(text="")
                    else:
                        v.config(text="")
                        answer = messagebox.askquestion(
                            "Search", "Are you sure?", icon="warning", parent=dname
                        )
                        if answer == "yes":
                            conn = sqlite3.connect("test.db")
                            c = conn.cursor()
                            sql = "SELECT * FROM BuyerInfo WHERE bname='" + a + "'"
                            try:
                                c.execute(sql)
                                result = c.fetchall()
                                if not (result):
                                    messagebox.showerror(
                                        "Error",
                                        "Buyer having name : "
                                        + a
                                        + " is not in the Buyers List",
                                        parent=dname,
                                    )
                                else:
                                    dl = Toplevel(root, bg="black")
                                    dl.title("Buyer Found : Buyer Name - " + a)
                                    dname.destroy()

                                    def delwin():
                                        sd.deiconify()
                                        dl.destroy()

                                    dl.protocol("WM_DELETE_WINDOW", delwin)
                                    dlf1 = LabelFrame(
                                        dl,
                                        text="Number",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf1.grid(row=1, column=1, pady=5)
                                    dlf2 = LabelFrame(
                                        dl,
                                        text="Name",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf2.grid(row=1, column=2, pady=5)
                                    dlf3 = LabelFrame(
                                        dl,
                                        text="Age",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf3.grid(row=1, column=3, pady=5)
                                    dlf4 = LabelFrame(
                                        dl,
                                        text="Gender",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf4.grid(row=1, column=4, pady=5)
                                    dlf5 = LabelFrame(
                                        dl,
                                        text="City",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf5.grid(row=1, column=5, pady=5)
                                    dlf6 = LabelFrame(
                                        dl,
                                        text="Blood Packet",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf6.grid(row=1, column=6, pady=5)
                                    dlf7 = LabelFrame(
                                        dl,
                                        text="Purchase Date",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf7.grid(row=1, column=7, pady=5)
                                    try:
                                        for row in result:
                                            v1 = row[0]
                                            v2 = row[1]
                                            v3 = row[2]
                                            v4 = row[3]
                                            v5 = row[4]
                                            v6 = row[5]
                                            v7 = row[6]
                                            dl1 = Label(
                                                dlf1,
                                                text=v1,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl1.pack()
                                            dl2 = Label(
                                                dlf2,
                                                text=v2,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl2.pack()
                                            dl3 = Label(
                                                dlf3,
                                                text=v3,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl3.pack()
                                            dl4 = Label(
                                                dlf4,
                                                text=v4,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl4.pack()
                                            dl5 = Label(
                                                dlf5,
                                                text=v5,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl5.pack()
                                            dl6 = Label(
                                                dlf6,
                                                text=v6,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl6.pack()
                                            dl7 = Label(
                                                dlf7,
                                                text=v7,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl7.pack()
                                    except:
                                        messagebox.showerror(
                                            "Error",
                                            "Unable to show buyer's information!",
                                            parent=dl,
                                        )
                            finally:
                                conn.commit()
                                c.close()
                                conn.close()

                def canc():
                    dname.destroy()
                    sd.deiconify()

                dnameb1 = Button(
                    dname,
                    text="SEARCH",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=search,
                    bg="white",
                    fg="black",
                )
                dnameb1.place(x=140, y=50)
                dnameb2 = Button(
                    dname,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=canc,
                    bg="white",
                    fg="black",
                )
                dnameb2.place(x=300, y=50)

            if radval == "dage":
                dage = Toplevel(sd, bg="black")
                dage.title("Search Buyer By : Buyer's Age")
                dage.geometry("535x100")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dage.destroy()

                dage.protocol("WM_DELETE_WINDOW", delwin)
                dagel1 = Label(
                    dage,
                    text="Enter Buyer's Age   : ",
                    font="helvetica",
                    fg="white",
                    bg="black",
                )
                dagel1.place(x=10, y=10)
                v = Label(dage, font="helvetica", fg="red", bg="black")
                v.place(x=320, y=10)

                def checknum(cn):
                    mo1 = re.match(r"^(\d?[1-9]|[1-9]0)$", cn.get())
                    if not (cn.get()):
                        v.config(text="Buyer's age required!")
                    elif not (mo1):
                        v.config(text="Enter a valid age!")
                    else:
                        v.config(text="")

                cn = StringVar()
                cn.trace("w", lambda name, index, mode, cn=cn: checknum(cn))
                dagee1 = Entry(dage, bd=3, textvariable=cn)
                dagee1.place(x=180, y=10)

                def search():
                    a = str(dagee1.get())
                    mo1 = re.match(r"^(\d?[1-9]|[1-9]0)$", a)
                    if not (dagee1.get()) or not (mo1):
                        if not (dagee1.get()):
                            v.config(text="Buyer's age required!")
                        elif not (mo1):
                            v.config(text="Enter a valid age!")
                        else:
                            v.config(text="")
                    else:
                        v.config(text="")
                        answer = messagebox.askquestion(
                            "Search", "Are you sure?", icon="warning", parent=dage
                        )
                        if answer == "yes":
                            conn = sqlite3.connect("test.db")
                            c = conn.cursor()
                            sql = "SELECT * FROM BuyerInfo WHERE age=" + a
                            try:
                                c.execute(sql)
                                result = c.fetchall()
                                if not (result):
                                    messagebox.showerror(
                                        "Error",
                                        "Buyer having age : "
                                        + a
                                        + " is not in the Buyers List",
                                        parent=dage,
                                    )
                                else:
                                    dl = Toplevel(root, bg="black")
                                    dl.title("Buyer Found : Buyer Age - " + a)
                                    dage.destroy()

                                    def delwin():
                                        sd.deiconify()
                                        dl.destroy()

                                    dl.protocol("WM_DELETE_WINDOW", delwin)
                                    dlf1 = LabelFrame(
                                        dl,
                                        text="Number",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf1.grid(row=1, column=1, pady=5)
                                    dlf2 = LabelFrame(
                                        dl,
                                        text="Name",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf2.grid(row=1, column=2, pady=5)
                                    dlf3 = LabelFrame(
                                        dl,
                                        text="Age",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf3.grid(row=1, column=3, pady=5)
                                    dlf4 = LabelFrame(
                                        dl,
                                        text="Gender",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf4.grid(row=1, column=4, pady=5)
                                    dlf5 = LabelFrame(
                                        dl,
                                        text="City",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf5.grid(row=1, column=5, pady=5)
                                    dlf6 = LabelFrame(
                                        dl,
                                        text="Blood Packet",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf6.grid(row=1, column=6, pady=5)
                                    dlf7 = LabelFrame(
                                        dl,
                                        text="Purchase Date",
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dlf7.grid(row=1, column=7, pady=5)
                                    try:
                                        for row in result:
                                            v1 = row[0]
                                            v2 = row[1]
                                            v3 = row[2]
                                            v4 = row[3]
                                            v5 = row[4]
                                            v6 = row[5]
                                            v7 = row[6]
                                            dl1 = Label(
                                                dlf1,
                                                text=v1,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl1.pack()
                                            dl2 = Label(
                                                dlf2,
                                                text=v2,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl2.pack()
                                            dl3 = Label(
                                                dlf3,
                                                text=v3,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl3.pack()
                                            dl4 = Label(
                                                dlf4,
                                                text=v4,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl4.pack()
                                            dl5 = Label(
                                                dlf5,
                                                text=v5,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl5.pack()
                                            dl6 = Label(
                                                dlf6,
                                                text=v6,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl6.pack()
                                            dl7 = Label(
                                                dlf7,
                                                text=v7,
                                                font="helvetica",
                                                bg="black",
                                                fg="white",
                                            )
                                            dl7.pack()
                                    except:
                                        messagebox.showerror(
                                            "Error",
                                            "Unable to show buyer's information!",
                                            parent=dl,
                                        )
                            finally:
                                conn.commit()
                                c.close()
                                conn.close()

                def canc():
                    dage.destroy()
                    sd.deiconify()

                dageb1 = Button(
                    dage,
                    text="SEARCH",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=search,
                    bg="white",
                    fg="black",
                )
                dageb1.place(x=140, y=50)
                dageb2 = Button(
                    dage,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=canc,
                    bg="white",
                    fg="black",
                )
                dageb2.place(x=300, y=50)

            if radval == "dbg":
                dbg = Toplevel(sd, bg="black")
                dbg.title("Search Buyer By : Blood Group")
                dbg.geometry("300x250")
                sd.withdraw()

                def delwin():
                    sd.deiconify()
                    dbg.destroy()

                dbg.protocol("WM_DELETE_WINDOW", delwin)

                labelfont = ("times", 15, "bold")
                dbgl1 = Label(
                    dbg,
                    text="Select a Blood Group :",
                    font=labelfont,
                    bg="black",
                    fg="white",
                )
                dbgl1.place(x=10, y=10)

                def dbgsel():
                    dbgradval = str(dbgvar1.get())
                    conn = sqlite3.connect("test.db")
                    c = conn.cursor()
                    sql = "SELECT * FROM BuyerInfo WHERE bbldgrp='" + dbgradval + "'"
                    try:
                        c.execute(sql)
                        result = c.fetchall()
                        if not (result):
                            messagebox.showerror(
                                "Error",
                                "Buyer having blood group : "
                                + dbgradval
                                + " is not in the Buyers List",
                                parent=dbg,
                            )
                        else:
                            dl = Toplevel(root, bg="black")
                            dl.title("Buyer Found : Blood Group - " + dbgradval)
                            dbg.iconify()

                            def delwin():
                                dbg.deiconify()
                                dl.destroy()

                            dl.protocol("WM_DELETE_WINDOW", delwin)
                            dlf1 = LabelFrame(
                                dl,
                                text="Number",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf1.grid(row=1, column=1, pady=5)
                            dlf2 = LabelFrame(
                                dl,
                                text="Name",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf2.grid(row=1, column=2, pady=5)
                            dlf3 = LabelFrame(
                                dl, text="Age", font="helvetica", bg="black", fg="white"
                            )
                            dlf3.grid(row=1, column=3, pady=5)
                            dlf4 = LabelFrame(
                                dl,
                                text="Gender",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf4.grid(row=1, column=4, pady=5)
                            dlf5 = LabelFrame(
                                dl,
                                text="City",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf5.grid(row=1, column=5, pady=5)
                            dlf6 = LabelFrame(
                                dl,
                                text="Blood Packet",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf6.grid(row=1, column=6, pady=5)
                            dlf7 = LabelFrame(
                                dl,
                                text="Purchase Date",
                                font="helvetica",
                                bg="black",
                                fg="white",
                            )
                            dlf7.grid(row=1, column=7, pady=5)
                            try:
                                for row in result:
                                    v1 = row[0]
                                    v2 = row[1]
                                    v3 = row[2]
                                    v4 = row[3]
                                    v5 = row[4]
                                    v6 = row[5]
                                    v7 = row[6]
                                    dl1 = Label(
                                        dlf1,
                                        text=v1,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl1.pack()
                                    dl2 = Label(
                                        dlf2,
                                        text=v2,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl2.pack()
                                    dl3 = Label(
                                        dlf3,
                                        text=v3,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl3.pack()
                                    dl4 = Label(
                                        dlf4,
                                        text=v4,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl4.pack()
                                    dl5 = Label(
                                        dlf5,
                                        text=v5,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl5.pack()
                                    dl6 = Label(
                                        dlf6,
                                        text=v6,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl6.pack()
                                    dl7 = Label(
                                        dlf7,
                                        text=v7,
                                        font="helvetica",
                                        bg="black",
                                        fg="white",
                                    )
                                    dl7.pack()
                            except:
                                messagebox.showerror(
                                    "Error",
                                    "Unable to show donor's information!",
                                    parent=dl,
                                )
                    finally:
                        conn.commit()
                        c.close()
                        conn.close()

                dbgvar1 = StringVar()
                dbgradiofont = ("helvetica", 13, "bold")
                dbgr1 = Radiobutton(
                    dbg,
                    text="A",
                    variable=dbgvar1,
                    value="A",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr1.place(x=10, y=40)
                dbgr2 = Radiobutton(
                    dbg,
                    text="B",
                    variable=dbgvar1,
                    value="B",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr2.place(x=10, y=80)
                dbgr3 = Radiobutton(
                    dbg,
                    text="AB",
                    variable=dbgvar1,
                    value="AB",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr3.place(x=10, y=120)
                dbgr4 = Radiobutton(
                    dbg,
                    text="O",
                    variable=dbgvar1,
                    value="O",
                    font=dbgradiofont,
                    command=dbgsel,
                    bg="black",
                    fg="white",
                )
                dbgr4.place(x=10, y=160)

                def dbgcanc():
                    dbg.destroy()
                    sd.deiconify()

                dbgb1 = Button(
                    dbg,
                    text="CANCEL",
                    font="helvetica",
                    height=1,
                    width=10,
                    command=dbgcanc,
                    bg="white",
                    fg="black",
                )
                dbgb1.place(x=10, y=200)
                dbgvar1.set(" ")

        var1 = StringVar()
        radiofont = ("helvetica", 15, "bold")
        r1 = Radiobutton(
            sd,
            text="Buyer Number",
            variable=var1,
            value="dno",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r1.place(x=330, y=80)
        r2 = Radiobutton(
            sd,
            text="Name",
            variable=var1,
            value="dname",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r2.place(x=330, y=125)
        r3 = Radiobutton(
            sd,
            text="Age",
            variable=var1,
            value="dage",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r3.place(x=330, y=170)
        r4 = Radiobutton(
            sd,
            text="Blood Group",
            variable=var1,
            value="dbg",
            font=radiofont,
            command=sel,
            bg="black",
            fg="white",
        )
        r4.place(x=330, y=215)
        l8 = Label(sd, text="", font="helvetica", bg="#FCFF33")
        var1.set(" ")

        def cancel():
            sd.destroy()

        b1 = Button(
            sd,
            text="CANCEL",
            font="helvetica",
            height=1,
            width=10,
            command=cancel,
            bg="white",
            fg="black",
        )
        b1.place(x=330, y=270)


# 7. Blood Packets Available
def bpavail():
    bpa = Toplevel(root, bg="#FCFF33")
    bpa.title("Blood Packets Available")
    bpafl = LabelFrame(bpa, text="Blood Group", font="helvetica", bg="#FCFF33")
    bpafl.grid(row=1, column=1, pady=5)
    bpafr = LabelFrame(bpa, text="No. of Packets", font="helvetica", bg="#FCFF33")
    bpafr.grid(row=1, column=2, pady=5)
    bpafi = Frame(bpa, bg="#FCFF33")
    bpafi.grid(row=1, column=3, padx=10, pady=10)
    panel2 = Label(bpafi, image=img3)
    panel2.pack(side="right")
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    sql = "SELECT * FROM bgpstock"
    try:
        c.execute(sql)
        result = c.fetchall()
        for row in result:
            bldgrp = row[0]
            packet = row[1]
            bpal1 = Label(bpafl, text=bldgrp, font="helvetica", bg="#FCFF33")
            bpal1.pack()
            bpal2 = Label(bpafr, text=packet, font="helvetica", bg="#FCFF33")
            bpal2.pack()
    except:
        messagebox.showerror(
            "Error", "Unable to show available blood packets!", parent=bpa
        )
    finally:
        conn.commit()
        c.close()
        conn.close()


# 8. Exit
def exitgui():
    ans = messagebox.askquestion("Exit", "Are you sure?", icon="warning")
    if ans == "yes":
        root.destroy()


fl = Frame(root, bg="#FF3232")
fl.pack(side=LEFT)

b1 = Button(
    fl,
    text="NEW DONOR",
    font="helvetica",
    height=2,
    width=40,
    command=newdonor,
    fg="#FCFF33",
    bg="black",
)
b1.grid(row=0, column=1, padx=100, pady=10)
b2 = Button(
    fl,
    text="DONORS LIST",
    font="helvetica",
    height=2,
    width=40,
    command=dlist,
    fg="#FCFF33",
    bg="black",
)
b2.grid(row=1, column=1, padx=100, pady=10)
b3 = Button(
    fl,
    text="SEARCH DONOR",
    font="helvetica",
    height=2,
    width=40,
    command=searchdonor,
    fg="#FCFF33",
    bg="black",
)
b3.grid(row=2, column=1, padx=100, pady=10)
b4 = Button(
    fl,
    text="NEW BUYER",
    font="helvetica",
    height=2,
    width=40,
    command=sbp,
    fg="#FCFF33",
    bg="black",
)
b4.grid(row=3, column=1, padx=100, pady=10)
b5 = Button(
    fl,
    text="BUYERS LIST",
    font="helvetica",
    height=2,
    width=40,
    command=blist,
    fg="#FCFF33",
    bg="black",
)
b5.grid(row=4, column=1, padx=100, pady=10)
b6 = Button(
    fl,
    text="SEARCH BUYER",
    font="helvetica",
    height=2,
    width=40,
    command=searchbuyer,
    fg="#FCFF33",
    bg="black",
)
b6.grid(row=5, column=1, padx=100, pady=10)
b7 = Button(
    fl,
    text="BLOOD PACKETS IN STOCK",
    font="helvetica",
    height=2,
    width=40,
    command=bpavail,
    fg="#FCFF33",
    bg="black",
)
b7.grid(row=6, column=1, padx=100, pady=10)
b8 = Button(
    fl,
    text="EXIT",
    font="helvetica",
    height=2,
    width=15,
    command=exitgui,
    fg="#FCFF33",
    bg="black",
)
b8.grid(row=7, column=1, padx=100, pady=10)

fr = Frame(root, bg="#FF3232")
fr.pack(side=RIGHT)

path = "BBMS.gif"
img = PhotoImage(file=path)
panel = Label(fr, image=img)
panel.pack(side="bottom", fill="both", expand="yes", padx=10)


path2 = "BBMS2.gif"
img2 = PhotoImage(file=path2)

path3 = "BBMS3.gif"
img3 = PhotoImage(file=path3)

path4 = "BBMS4.gif"
img4 = PhotoImage(file=path4)

root.mainloop()
