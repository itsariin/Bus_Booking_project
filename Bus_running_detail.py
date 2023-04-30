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
t2 = Label(root, text='Add Bus Running Details', bg='gray20', fg='green3', font='Arial 22 bold')
t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)


def datecorrect():
    olddate = datef.get()
    newdate = olddate[6:] + '-' + olddate[3:5] + '-' + olddate[:2]
    return newdate

import sqlite3

con = sqlite3.connect('PYthonBusProj.db')
cur = con.cursor()


Busid = Label(root, text='Bus ID', font='Arial 14')
date = Label(root, text='Running Date', font='Arial 14')
avail = Label(root, text='Seat Available', font='Arial 14')

bidf = Entry(root)
datef = Entry(root)
availf = Entry(root)


def addnew():
    date = 0
    date = cur.fetchall()
    date = datecorrect()
    cur.execute("""insert into runs(runs_busID,runs_date,seat_available)values({},'{}',{})""".format(bidf.get(), date,
                                                                                        availf.get()))
    con.commit()


    op1 = Label(root, text='{} {} {} '.format(bidf.get(), datef.get(), availf.get()),
                font='Arial 12')
    op1.grid(row=6, columnspan=13)
    showinfo('Operator Entry Updated', 'Bus Running Record updated successfully')


def checking():
    cur.execute("SELECT * FROM runs")
    f=cur.fetchall()
    print(f)

addb = Button(root, text='Add Run', bg='SpringGreen2', font='Arial 14', command=addnew)
eb = Button(root, text='Delete Run', bg='SpringGreen2',fg='Red', font='Arial 14')

#check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
#check_db.grid(row=10, column=11)

def takehome():
    root.destroy()
    import Home_page

home = Button(root, image=img1, bg='light green', command=takehome)

Busid.grid(row=5, column=3)
bidf.grid(row=5, column=4)
date.grid(row=5, column=5)
datef.grid(row=5, column=6)
avail.grid(row=5, column=7)
availf.grid(row=5, column=8)
addb.grid(row=5, column=9)
eb.grid(row=5, column=10)
home.grid(row=8, column=9,pady=20)

root.mainloop()