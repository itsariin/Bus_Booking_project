from tkinter import *
from tkinter.messagebox import *

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

import sqlite3
con = sqlite3.connect('PYthonBusProj.db')
cur = con.cursor()


img = PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
img1 = PhotoImage(file="/Users/arinjain/Desktop/GUI/home.png")
bus = Label(root, image=img)
bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
t2 = Label(root, text='Add Bus Details', bg='gray20', fg='green3', font='Arial 22 bold')
t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)



def getvals():

    cur.execute("""insert into bus (busID,bus_type,bus_opid,capacity,fare,bus_rid)values({},'{}',{},{},{},{})""".format(busid_f.get(), clicked.get(), opid_f.get(), CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()))
    con.commit()

    op1 = Label(root,text='{} {} {} {} {} {}'.format(busid_f.get(), clicked.get(), CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()),font='Arial 12')


    op1.grid(row=4, columnspan=13)
    showinfo('Operator Entry Updated', 'Bus Details updated successfully')


    print(f"{busid_f.get(),clicked.get(),  CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()} ")

    with open("add_busdetail.txt", "a") as f:
        f.write(f"{busid_f.get(), clicked.get(),  CapacitY_f.get(), farE_f.get(), opid_f.get(),Routeid_f.get()}\n ")



busid = Label(root, text='Bus ID', font='Arial 14')
bustype = Label(root, text='Bus type', font='Arial 14')
CapacitY = Label(root, text='Capacity', font='Arial 14')
farE = Label(root, text='Fare Rs', font='Arial 14')
opid = Label(root, text='Operator ID', font='Arial 14')
Routeid = Label(root, text='Route ID', font='Arial 14')


options = [
        "AC 2x2",
        "AC 3x2",
        "Non AC 2x2",
        "Non AC 3x2",
        "AC-Sleeper 2x1",
        "Non AC-Sleeper 2x1"
    ]
clicked = StringVar()
clicked.set("Bus Type")
drop = OptionMenu(root, clicked, *options)

# Tkinter variable for storing entries
busid_f = StringVar()
Routeid_f = StringVar()
CapacitY_f = StringVar()
farE_f = StringVar()
opid_f = StringVar()

#Entries for our form
busid_f = Entry(root, textvariable=busid_f)
Routeid_f = Entry(root, textvariable=Routeid_f)
CapacitY_f = Entry(root, textvariable=CapacitY_f)
farE_f = Entry(root, textvariable=farE_f)
opid_f = Entry(root, textvariable=opid_f)


def checking():
    cur.execute("SELECT * FROM bus")
    f=cur.fetchall()
    print(f)


def addnew():
    op1 = Label(root, text='{} {} {} {} {}'.format(busid_f.get(),clicked.get(), CapacitY_f.get(), farE_f.get(), opid_f.get(), Routeid_f.get()),
                font='Arial 12')
    op1.grid(row=4, columnspan=13)
    showinfo('Operator Entry Updated', 'Bus Details updated successfully')

addb = Button(root, text='Add Bus', bg='SpringGreen2', font='Arial 14', command=getvals)
eb = Button(root, text='Edit Bus', bg='SpringGreen2', font='Arial 14')
home = Button(root, image=img1, bg='light green')

#check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
#check_db.grid(row=10, column=11)

busid.grid(row=3, column=1)
busid_f.grid(row=3, column=2)
bustype.grid(row=3, column=3)
drop.grid(row=3, column=4)
CapacitY.grid(row=3, column=5)
CapacitY_f.grid(row=3, column=6)
farE.grid(row=3, column=7)
farE_f.grid(row=3, column=8)
opid.grid(row=3, column=9)
opid_f.grid(row=3, column=10)
Routeid.grid(row=3, column=11)
Routeid_f.grid(row=3, column=12)
addb.grid(row=5, column=7)
eb.grid(row=5, column=8)
home.grid(row=5, column=9)

root.mainloop()