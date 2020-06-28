from tkinter import*
import tkinter.messagebox as mb

class login_system(Frame):

    def command(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if (username == 'SAI' and password == 'Admin'):
            mb.showinfo("Login", 'Login successfull')
        else:
            mb.showinfo("Login", 'Login failed')

    def __init__(self,login):

        super().__init__(login)
        self.login=login
        self.label_username = Label(self,text='Username',font=('Times new roman',15))
        self.label_password = Label(self,text='Password',font=('Times new roman',15))

        self.entry_username = Entry(self)
        self.entry_password = Entry(self)

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.button=Button(self, text='login', command=lambda :self.command)
        self.button.grid(columnspan=2)

        self.pack()

        def login (self):
            username = self.entry_username.get()
            password = self.entry_password.get()

            if(username=='SAI' and password=='Admin'):
                mb.showinfo("Login",'Login successfull')
            else:
                mb.showinfo("Login",'Login failed')

sai = Tk()
login = login_system(sai)
sai.mainloop()
