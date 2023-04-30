from tkinter import *
from tkinter.messagebox import *

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

img = PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
img1 = PhotoImage(file="/Users/arinjain/Desktop/GUI/home.png")
bus = Label(root, image=img)
bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
t2 = Label(root, text='Add Bus Operator Details', bg='white smoke', fg='green3', font='Arial 22 bold')
t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)

import sqlite3

con = sqlite3.connect('PYthonBusProj.db')
cur = con.cursor()


def getvals():

    cur.execute("""insert into operator (opid,name,phone,address,email)values({},'{}',{},'{}','{}')""".format(int(float(opf.get())), nf.get(), int(phf.get()), addf.get(), mf.get()))
    con.commit()

    op1 = Label(root, text='{} {} {} {} {}'.format(opf.get(), nf.get(), addf.get(), phf.get(), mf.get()),
                font='Arial 12')
    op1.grid(row=4, columnspan=13)
    showinfo('Operator Entry Updated', 'Operator Record updated successfully')

    print(f"{opf.get(), nf.get(), addf.get(), phf.get(), mf.get()} ")

    with open("operator_detail.txt", "a") as f:
        f.write(f"{opf.get(), nf.get(), addf.get(), phf.get(), mf.get()}\n ")



opid = Label(root, text='Operator ID', font='Arial 14')
name = Label(root, text='Name', font='Arial 14')
add = Label(root, text='Address', font='Arial 14')
ph = Label(root, text='Phone', font='Arial 14')
mail = Label(root, text='Email', font='Arial 14')



# Tkinter variable for storing entries
opf = StringVar()
nf = StringVar()
addf = StringVar()
phf = StringVar()
mf = StringVar()

#Entries for our form

opf = Entry(root, textvariable=opf)
nf = Entry(root, textvariable=nf)
addf = Entry(root, textvariable=addf)
phf = Entry(root, textvariable=phf)
mf = Entry(root, textvariable=mf)


def checking():
    cur.execute("SELECT * FROM operator")
    f=cur.fetchall()
    print(f)


def addnew():
    op1 = Label(root, text='{} {} {} {} {}'.format(opf.get(), nf.get(), addf.get(), phf.get(), mf.get()),
                font='Arial 12')
    op1.grid(row=4, columnspan=13)
    showinfo('Operator Entry Updated', 'Operator Record updated successfully')


addb = Button(root, text='Add', bg='SpringGreen2', font='Arial 14', command=getvals)
eb = Button(root, text='Edit', bg='SpringGreen2', font='Arial 14')

#check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
#check_db.grid(row=10, column=11)

def takehome():
    root.destroy()
    import Home_page

home = Button(root, image=img1, bg='light green', command=takehome)

opid.grid(row=3, column=1)  # stick=W or E
opf.grid(row=3, column=2)
name.grid(row=3, column=3)
nf.grid(row=3, column=4)
add.grid(row=3, column=5)
addf.grid(row=3, column=6)
ph.grid(row=3, column=7)
phf.grid(row=3, column=8)
mail.grid(row=3, column=9)
mf.grid(row=3, column=10)
addb.grid(row=3, column=11)
eb.grid(row=3, column=12)

home.grid(row=5, column=9)

root.mainloop()


