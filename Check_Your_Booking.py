from tkinter import *
from tkinter.messagebox import *

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (w, h))

frame1 = Frame(root,relief='groove',bd=5)
frame1.grid(row=4, column=4, columnspan=12,pady=20)

import sqlite3

con = sqlite3.connect('PYthonBusProj.db')
cur = con.cursor()

def getvals():
    if len(mobf.get())==10:
        cur.execute("SELECT * FROM bookinghistory where mobile={}".format(int(mobf.get())))
        f = cur.fetchall()
        print(f)
        passe = 'Passenger Name:' + str(f[0][0])
        gender = 'gender:' + str(f[0][8])
        nofs = 'No. of Seats:' + str(f[0][3])
        mob = 'Phone:' + str(f[0][1])
        age = 'Age:' + str(f[0][2])
        Fare = 'Fare:' + str(f[0][10])
        refno = 'Booking No.:' + str(f[0][8])
        oper = 'Bus Detail:' + str(f[0][11])
        travd = 'Travel Date:' + str(f[0][9])
        bookd = 'Booking Date:' + str(f[0][6])
        desti = 'Destination:' + str(f[0][5])
        bp = 'Boarding Point:' + str(f[0][4])
        Label(frame1, text=passe, fg='grey5', font='Arial 15 bold').grid(row=4, column=0)
        Label(frame1, text=nofs, fg='grey5', font='Arial 15 bold').grid(row=5, column=0)
        Label(frame1, text=age, fg='grey5', font='Arial 15 bold').grid(row=6, column=0)
        Label(frame1, text=refno, fg='grey5', font='Arial 15 bold').grid(row=7, column=0)
        Label(frame1, text=travd, fg='grey5', font='Arial 15 bold').grid(row=8, column=0)
        Label(frame1, text=bp, fg='grey5', font='Arial 15 bold').grid(row=9, column=0)
        Label(frame1, text=gender, fg='grey5', font='Arial 15 bold').grid(row=4, column=2)
        Label(frame1, text=mob, fg='grey5', font='Arial 15 bold').grid(row=5, column=2)
        Label(frame1, text=Fare, fg='grey5', font='Arial 15 bold').grid(row=6, column=2)
        Label(frame1, text=oper, fg='grey5', font='Arial 15 bold').grid(row=7, column=2)
        Label(frame1, text=bookd, fg='grey5', font='Arial 15 bold').grid(row=8, column=2)
        Label(frame1, text=desti, fg='grey5', font='Arial 15 bold').grid(row=9, column=2)

        Label(frame1, text='* Total amount Rs to be paid at the time of boarding the bus', fg='grey5',
              font='Arial 15').grid(row=11, columnspan=20, column=0)

    else:

        showerror('phoneno', 'mobile number not valid')

img = PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
img1 = PhotoImage(file="/Users/arinjain/Desktop/GUI/home.png")
bus = Label(root, image=img)
bus.grid(row=0, column=0, columnspan=20, padx=w // 3)
t1 = Label(root, text='Online Bus Booking System', bg='light blue', fg='Red', font='Arial 32 bold')
t1.grid(row=1, column=0, columnspan=20, padx=w // 3)
t2 = Label(root, text='Check Your Booking', bg='SpringGreen2', fg='green4', font='Arial 22 bold')
t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)

mob = Label(root, text='Enter Your mobile number :', font='Arial 12')
mobf = Entry(root)

# Tkinter variable for storing entries
#mobf = StringVar()

#Entries for our form


def checkbook():
    op1 = Label(root, text='Ticket Here', font='Arial 12')
    op1.grid(row=4, columnspan=20, padx=w // 3, )


checkb = Button(root, text='Check Booking', font='Arial 14', command=getvals)

#, command=checkbook

mob.grid(row=3, column=8, sticky=E)  # sticky=W or E
mobf.grid(row=3, column=9, sticky=EW, padx=5)
checkb.grid(row=3, column=10, sticky=W)

root.mainloop()
