from tkinter import*
import sys
def command1(event):
    if entry1.get() == 'saikiran' and entry2.get() == 'padala' or entry1.get() == 'shashank' and entry2.get() == 'munna':
        sai.deiconify()
        top.destroy()


def command2():
    top.destroy()
    sai.destroy()
    sys.exit()

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
button2 = Button(top,text='Cancel', command=lambda:command2())

entry2.bind('<Return>', command1)

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






