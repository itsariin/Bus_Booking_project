from tkinter import *
root = Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

root.title('lets try with the bus')
#root.geometry('1000x600')
bus=PhotoImage(file="/Users/arinjain/Desktop/GUI/bus.png")
#Label(root, image=bus).pack()
Label(root, image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)

root.mainloop()