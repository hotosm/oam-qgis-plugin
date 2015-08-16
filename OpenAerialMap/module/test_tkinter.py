from Tkinter import Frame, Message

class HelloTkWindow(Frame):

    def __init__(self, master, title, msg):
        Frame.__init__(self, master)
        self.msg = msg
        self.master.title(title)
        self.createWidgets()

    def createWidgets(self):
        self.msgWigt = Message(self.master, text=self.msg, width=300)
        self.msgWigt.pack({"side": "left"})
