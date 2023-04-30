from tkinter import *
root = Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
root.title('Add New Details')
bus=PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
Label(root, image=bus).grid(row=0,column=0,columnspan=20,padx=w//2.5)
Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=0,columnspan=20,padx=w//3)
Label(root,text = "Add New Detail to Database",font=("Arial", 20,"bold"), fg= "green4").grid(row=2,column=0,columnspan=20,pady=20)


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


New_operator = Button(root,text="New Operator",font=("Arial", 15,),bg= "pale green", fg= "gray5",command=newop)
New_operator.grid(row=3,column=8,pady=20)
New_Bus = Button(root,text="New Bus",font=("Arial", 15,),bg= "coral", fg= "gray5",command=newbus)
New_Bus.grid(row=3,column=9,pady=20)
New_Route = Button(root,text="New Route",font=("Arial", 15,),bg= "steel blue", fg= "gray5",command=newroute)
New_Route.grid(row=3,column=10,pady=20)
New_Run = Button(root,text="New Run",font=("Arial", 15,),bg= "RosyBrown3", fg= "gray5",command=newrun)
New_Run.grid(row=3,column=11,pady=20)
root.mainloop()