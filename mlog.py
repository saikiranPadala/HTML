from tkinter import*
import tkinter.messagebox as mb

def command1():
    if entry1.get() == 'saikiran' and entry2.get() == 'padala' or entry1.get() == 'shashank' and entry2.get() == 'munna':
        mb.showinfo("Login", 'Login successfull')
    else:
         mb.showinfo("Login", 'Login failed')

sai = Tk()
top = Toplevel()

top.geometry('300x260')
top.title('LOGIN SCREEN')
top.configure(background='white')
photo = Label(top, bg='white')
lbl1 = Label(top, text='Username:', font=('Helvetica', 10))
entry1 = Entry(top)
lbl2 = Label(top, text='Password:', font=('Helvetica', 10))
entry2 = Entry(top, show="*")
button2 = Button(top,text='Login', command=lambda:command1())

lbl = Label(top, text='SAI Login screen 2020', font=('Arial,9'))

photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl.pack()

sai.title('Main Screen')
sai.configure(background='white')
sai.geometry('855x650')

sai.withdraw()
sai.mainloop()

