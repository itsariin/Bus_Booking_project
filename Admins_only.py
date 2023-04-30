from tkinter import *
root = Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

root.title('Seat Booking Page')
bus=PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
Label(root, image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=1,columnspan=10,padx=w//3)


def newop():
    root.destroy()
    import Add_Bus_Operator


def newbus():
    root.destroy()
    import Add_Bus_Detail


def newroute():
    root.destroy()
    import Add_Bus_Route

def newrun():
    root.destroy()
    import Bus_running_detail

seat_booking = Button(root, text = 'New Operator',font=("Arial", 25,),bg= "pale green", fg= "gray5",command=newop).grid(row=3,column=3,pady=70)
check  = Button(root, text = 'New Bus',font=("Arial", 25),bg= "coral", fg= "gray5",command=newbus).grid(row=3,column=5,pady=70)
Add_detail = Button(root, text = 'New Route',font=("Arial", 25),bg= "steel blue", fg= "gray5",command=newroute).grid(row=3,column=7,pady=70)
#admins_only = Label(root, text='For Admin Only',font=("Arial", 20), fg= "red2").grid(row=4,column=7)
Newrun= Button(root, text = 'New Run',font=("Arial", 25),bg= "RosyBrown3", fg= "gray5",command=newrun).grid(row=3,column=9,sticky='w',pady=70)

root.mainloop()
