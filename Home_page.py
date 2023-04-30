from tkinter import *
root = Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Seat Booking Page')
bus=PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
Label(root, image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=1,columnspan=10,padx=w//3)


def gobbook():
    root.destroy()
    import Bus_Booking


def checkbooking():
    root.destroy()
    import Check_Your_Booking


def addbusdetail():
    root.destroy()
    import Add_New_detail_Database

seat_booking = Button(root, text = 'Seat Booking',font=("Arial", 25,),bg= "pale green", fg= "gray5",command=gobbook).grid(row=3,column=3,pady=70)
check  = Button(root, text = 'Checked Booked Seat',font=("Arial", 25),bg= "lime green", fg= "gray5",command=checkbooking).grid(row=3,column=5,pady=70)
Add_detail = Button(root, text = 'Add Bus Detail',font=("Arial", 25), fg= "gray5",command=addbusdetail).grid(row=3,column=7,pady=70)
admins_only = Label(root, text='For Admin Only',font=("Arial", 20), fg= "red2").grid(row=4,column=7)
root.mainloop()
