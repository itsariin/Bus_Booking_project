from tkinter import *
root=Tk()

root.title('Arin and Priyavi')
root.geometry('1000x600')

Label(root,text="Enter your name ").pack()
print('Hello Priyavi')

def fun():
    Label(root,text="Welcome "+a.get()).pack()

a=Entry(root)
a.pack()

Button(root,text='ok',command=fun).pack()


root.mainloop()