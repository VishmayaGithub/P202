import socket 
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

# nickname = input("Choose your nickname: ")
client.connect((ip_address,port))
print("Connected to the server")




class GUI:

    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.login = Toplevel()
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=400)

        self.login.title("Login")
        self.pls = Label(self.login,text="Please login to continue",justify=CENTER,font="Helvetica 14 bold")
        self.pls.place(relheight = 0.15,relx=0.2,height=0.07)

        self.labelName = Label(self.login,text="Name: ",font="Helvetica 12")
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)

        self.entryName = Entry(self.login,font="Helvetica 12")
        self.entryName.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.2)
        self.entryName.focus()

        self.submit = Button(self.login,text="Continue",font="Helvetica 13",command=lambda:self.goAhead(self.entryName.get()))
        self.submit.place(relx=0.4,rely=0.55)

        self.Window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name = name
        rcv=Thread(target=self.receive)
        rcv.start()

       
    def receive(self):
        while True:
            try:
                msg=client.recv(2048).decode("utf-8")
                if msg=="NICKNAME":
                    client.send(self.name.encode("utf-8"))
                else:
                    pass
            except:
                print("An error occured!")            
                client.close()
                break

g = GUI()
# def write():
#     while True:
#         msg="{}:{}".format(nickname,input(""))
#         client.send(msg.encode("utf-8"))

# recv_thread = Thread(target=receive)
# recv_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()

