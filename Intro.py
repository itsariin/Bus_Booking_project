from tkinter import *
root = Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

root.title('lets try with the bus')
#root.geometry('1000x600')
bus=PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
#Label(root, image=bus).pack()
#def change_color():
   #Label.config(bg= "gray51", fg= "white")

Label(root, image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
Label(root, text="Online Bus Booking System",font=("Arial", 30,"bold"),bg= "sky blue", fg= "red2").grid(row=1,column=1,columnspan=10,padx=w//3)
name = Label(root,text = "Name : Arin Jain",font=("Arial, 20"),fg="medium blue").grid(row=5,column=5,padx=5,pady=40)
Enrollment = Label(root,text = "Er : 211B392",font=("Arial, 20"),fg="medium blue").grid(row=7,column=5,padx=5,pady=10)
Mobile = Label(root,text = "Mobile : 6375244746",font=("Arial, 20"),fg="medium blue").grid(row=9,column=5,padx=5,pady=40)
submitted = Label(root, text="Submitted to : Dr. Mahesh Kumar",font=("Arial", 25,"bold"),bg= "sky blue", fg= "red2").grid(row=11,column=5,padx=w//3)
Project = Label(root,text = "Project Based Learning",font=("Arial, 20"),fg="red2").grid(row=13,column=5,padx=5,)

#name = Label(root,text="Name : Arin Jain").grid(row=3,column=3)
def close(e=0):
    root.destroy()
    import Home_page
root.bind('<KeyPress>',close)
root.mainloop()
