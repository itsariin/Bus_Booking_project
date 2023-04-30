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
t2 = Label(root, text='Add Bus Route Details', bg='gray20', fg='green3', font='Arial 22 bold')
t2.grid(row=2, column=0, columnspan=20, padx=w // 3, pady=20)


import sqlite3

con = sqlite3.connect('PYthonBusProj.db')
cur = con.cursor()



def addnew():
    '''routef.delete(0, END)
    snf.delete(0, END)
    staion_id_f.delete(0, END)'''


    #cur.execute("""select rid from route""".format(c.get))

    cur.execute("""insert into route(rid,stid,station_name)values({},{},"{}")""".format(routef.get(),snf.get(),staion_id_f.get()))
    con.commit()

    op1 = Label(root, text='{} {} {} '.format(routef.get(), snf.get(), staion_id_f.get()),font='Arial 12')
    op1.grid(row=6, columnspan=13)
    showinfo('Operator Entry Updated', 'Bus Route Added successfully')


def checking():
    cur.execute("SELECT * FROM route")
    f=cur.fetchall()
    print(f)

Routeid = Label(root, text='Route ID', font='Arial 14')
station_name = Label(root, text='Station Name', font='Arial 14')
Station_id = Label(root, text='Station ID', font='Arial 14')

routef = Entry(root)
snf = Entry(root)
staion_id_f = Entry(root)



addb = Button(root, text='Add Route', bg='SpringGreen2', font='Arial 14', command=addnew)
eb = Button(root, text='Delete Route', bg='SpringGreen2',fg='Red', font='Arial 14')


#check_db = Button(root, text='Check', bg='SpringGreen2', font='Arial 14', command=checking)
#check_db.grid(row=10, column=11)

def takehome():
    root.destroy()
    import Home_page

home = Button(root, image=img1, bg='light green', command=takehome)

Routeid.grid(row=5, column=3)
routef.grid(row=5, column=4)
station_name.grid(row=5, column=5)
snf.grid(row=5, column=6)
Station_id.grid(row=5, column=7)
staion_id_f.grid(row=5, column=8)
addb.grid(row=5, column=11)
eb.grid(row=5, column=12)
home.grid(row=8, column=9,pady=20)

root.mainloop()