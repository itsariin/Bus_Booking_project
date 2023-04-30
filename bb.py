from tkinter import *
import tkinter.messagebox as mb
root = Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
frame_1 = Frame(root)
frame_1.grid(row=6,column=0,columnspan=20)
root.title('Booking of bus')
bus=PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
Label(root, image=bus).grid(row=0,column=0,columnspan=20,padx=w//2.5)
home=PhotoImage(file="/Users/arinjain/Desktop/GUI/home.png")
Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=0,columnspan=20,padx=w//3)
Label(root,text = "Entry Journey Details",font=("Arial", 20,"bold"),bg= "SpringGreen2", fg= "green4").grid(row=2,column=0,columnspan=20,pady=20)
to=Label(root,text="To",font=("Arial", 15,"bold"), fg= "gray5").grid(row=3,column=3,pady=20,sticky='E')
From=Label(root,text="From",font=("Arial", 15,"bold"), fg= "gray5").grid(row=3,column=5,pady=20,sticky='E')
Journey_Date=Label(root,text="Journey Date",font=("Arial", 15,"bold"), fg= "gray5").grid(row=3,column=7,pady=20,sticky='E')
tof=Entry(root)
fromf=Entry(root)
datef=Entry(root)
tof.grid(row=3,column=4,pady=20,sticky='W')
fromf.grid(row=3,column=6,pady=20,sticky='W')
datef.grid(row=3,column=8,pady=20,sticky='W')
v = StringVar(root, "1")


import sqlite3

con = sqlite3.connect('pythonbus.db')
cur = con.cursor()


#def dia():


def call():
    res = mb.askquestion('Fare Confirm',
                         'Total amount to be paid Rs.3000.00')

    if res == 'yes':
        root.destroy()

    else:
        mb.showinfo('Return', 'Your Seat is Not Booked')

# Details Of Passengers
def proceed_1():
    fill_detail = Label(frame_1, text="Fill Passenger Detail To Book The Bus Ticket", font=("Arial", 30, "bold"),bg="sky blue", fg="red2")
    fill_detail.grid(row=6, column=0,columnspan=10,pady=20)
    Name_pas = Label(root, text="Name", font=("Arial", 15, "bold"), fg="gray5")
    Name_pas.grid(row=8, column=3, pady=20, sticky='E')
    a1 = Entry(root)
    a1.grid(row=8, column=4, pady=20, sticky='W')
    Gender_1 = Label(root, text="Gender", font=("Arial", 15, "bold"), fg="gray5")
    Gender_1.grid(row=8, column=5, pady=20, sticky='E')
    options = [
        "Male",
        "Female",
        "Transgender",
        "Prefer not to say"
    ]
    clicked = StringVar()
    clicked.set("Male")
    drop = OptionMenu(root, clicked, *options)
    drop.grid(row=8, column=6, pady=20, sticky='W')
    Num_seat = Label(root, text="No. of Seats", font=("Arial", 15, "bold"), fg="gray5")
    Num_seat.grid(row=8, column=6, pady=20, sticky='E')
    b1 = Entry(root)
    b1.grid(row=8, column=7, pady=20, sticky='W')
    Mob = Label(root, text="Mobile", font=("Arial", 15, "bold"), fg="gray5")
    Mob.grid(row=8, column=7, pady=20, sticky='E')
    c1 = Entry(root)
    c1.grid(row=8, column=8, pady=20, sticky='W')
    Age = Label(root, text="Age", font=("Arial", 15, "bold"), fg="gray5")
    Age.grid(row=8, column=8, pady=20, sticky='E')
    d1 = Entry(root)
    d1.grid(row=8, column=9, pady=20, sticky='W')
    Book_seat = Button(root, text="Book seat", font=("Arial", 15,), background="pale green", fg="gray5",command=call)
    Book_seat.grid(row=8, column=10, pady=20)

#Date Correction
def datecorrect():
    olddate = datef.get()
    newdate = olddate[6:] + '-' + olddate[3:5] + '-' + olddate[:2]
    return newdate

#Journey Detail
def detail():
    select_bus = Label(root, text="Select Bus", font=("Arial", 15), fg="green4")
    select_bus.grid(row=4, column=4, pady=20)
    operatoR = Label(root, text="Operator", font=("Arial", 15), fg="green4")
    operatoR.grid(row=4, column=5, pady=20)
    bus_type = Label(root, text="Bus Type", font=("Arial", 15), fg="green4")
    bus_type.grid(row=4, column=6, pady=20)
    avail = Label(root, text="Available/capacity", font=("Arial", 15), fg="green4")
    avail.grid(row=4, column=7, pady=20)
    fare = Label(root, text="Fare", font=("Arial", 15), fg="green4")
    fare.grid(row=4, column=8, pady=20)
    values = {"Bus 1": "0"}
    for (text, value) in values.items():
        Radiobutton(root, text=text, variable=v,
                    value=value, indicator=0,background="light blue").grid(row=5, column=4, pady=20, sticky='W')


##

    dated = datecorrect()
    cur.execute(
        """select op.name,b.bus_type,r.seat_available,b.capacity,b.fare,b.bus_opid,st.stid as start_st,ed.stid as end_st from operator as op,bus as b,route as st,route as ed,runs as r where r.runs_date='{}' and st.station_name="{}" and ed.station_name="{}" and st.stid< ed.stid and st.rid=ed.rid and b.bus_rid=st.rid and b.bus_opid=op.opid and r.runs_busid=b.busid""".format(
            dated, fromf.get(), tof.get()))
    res = cur.fetchall()
    buses_count = len(res)




    name_operator = Label(root, text="Vatsal", font=("Arial", 15, "italic"), fg="medium blue")
    name_operator.grid(row=5, column=5, pady=20)
    b_type = Label(root, text="AC 2x3", font=("Arial", 15), fg="medium blue")
    b_type.grid(row=5, column=6, pady=20)
    capacity = Label(root, text="23/40", font=("Arial", 15), fg="medium blue")
    capacity.grid(row=5, column=7, pady=20)
    fee = Label(root, text="1499", font=("Arial", 15), fg="medium blue")
    fee.grid(row=5, column=8, pady=20)
    proceed = Button(root, text="Proceed To Book", font=("Arial", 15,), bg="pale green", fg="gray5", command=proceed_1)
    proceed.grid(row=5, column=9, pady=20)





show_bus = Button(root,text="Show Bus",font=("Arial", 15,),bg= "pale green", fg= "gray5",command=detail)
show_bus.grid(row=3,column=9,pady=20)
home_button = Button(root,image=home)
home_button.grid(row=3,column=10,pady=20,sticky='W')


root.mainloop()