
from tkinter import *
from tkinter import ttk
from init_client import socketClient
import socket

class View():

    def __init__(self):

        # Get resource
        self.name = socket.gethostname()
        self.address = socket.gethostbyname(socket.gethostname())
        # Connection
        self.connection = socketClient(self.name, self.address, self)
        # Instance view
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()

        # Init Config and view
        self.configureView()
        self.buildView()
        self.root.mainloop()

    def buildView(self):

        self.btnSend = Button(self.root, text='Send', command=self.sendMessage)
        self.btnSend.place(x=235, y=370)
        self.btnExit = Button(self.root, text="Exit", command=self.root.destroy)
        self.btnExit.place(x=195, y=370)

        self.textArea = Text(self.root, height=20, width=67, bg=self.rgbtohex(44, 59, 63), fg="white", state='disabled')
        self.textArea.place(x=10, y=10)
        self.inputSend = Entry(self.root, width=51, bg=self.rgbtohex(44, 59, 63), fg="white")
        self.inputSend.place(x=13, y=323)

        self.labelAlias = Label(self.root, width=6, text='Alias :', fg="white", bg=self.rgbtohex(27, 29, 30))
        self.labelAlias.place(x=500, y=10)
        self.inputAlias = Entry(self.root, width=9, bg=self.rgbtohex(44, 59, 63), fg="white")
        self.inputAlias.place(x=500, y=30)

        self.btnUpdateConnection = Button(self.root, text='Update', command=self.listConnection, width=10)
        self.btnUpdateConnection.place(x=500, y=65)

    def configureView(self):
        width = 750
        height = 400
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2)-(width/2)
        y = (hs/2)-(height/2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.configure(bg=self.rgbtohex(27, 29, 30))
        self.root.title("Message")

    #ENVIAR MENSAJE A TODOS O DESTINATARIOS
    def sendMessage(self):
        self.textArea.configure(state='normal')
        aliasText = self.inputAlias.get()

        if(aliasText == ""):
            aliasText = "Anonymus"

        aliasText += " :\n"
        self.textArea.insert(END, aliasText + self.inputSend.get() + "\n")
        self.textArea.configure(state='disabled')
        self.connection.sendMessage(self.name, self.address, self.inputAlias.get(), self.inputSend.get(), "Alls")

    #LISTA CONEXIONES DISPONIBLES
    def listConnection(self):
        print("List connection")
        listObject = {
            'id': 'All',
            'ip': 'All',
            'name': 'All'
        }
        print(listObject)

    #RETORNA FORMATO RGB PARA COLOREAR LA VIEW
    def rgbtohex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

def main():
    view = View()
    return 0

if __name__ == '__main__':
    main()
