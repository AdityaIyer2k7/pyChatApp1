from pyNetSocket import *
import tkinter

svr_ip = input("Server IP: ")
PORT = 5050

cli = Client(svr_ip, PORT)

win = tkinter.Tk("Chat app")

(msgs_box := tkinter.Text(win, bd=4, bg="grey", width=60, height=30, state='disabled')).grid(row=0, column=0, columnspan=4)

msg = tkinter.StringVar()
tkinter.Entry(win, textvariable=msg, width=45).grid(row=1, column=0, columnspan=3)

def add_msg(_, __, msg):
    msgs_box.configure(state='normal')
    msgs_box.insert(tkinter.INSERT, "\n"+msg)
    msgs_box.configure(state='disabled')
    print(msg)
def send_msg():
    cli.send(msg.get())
    msg.set("")

tkinter.Button(win, text="Send", command=send_msg).grid(row=1, column=3)

cli.onMessage(add_msg)
cli.connect()

tkinter.mainloop()
