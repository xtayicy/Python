from Tkinter import *
import tkSimpleDialog as dl
import tkMessageBox as mb

#root = Tk()
#print(root)
#w = Label(root,text = "JDais' work")
#print(w)
#w.pack()

#mb.showinfo("welcome", "welcome to JDaisy's world!")
#guess = dl.askinteger("Number", "enter a number")
#print(guess)
#mb.showinfo("output:", "this is output message")

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

#    def createWidgets(self):
#        self.helloLabel = Label(self, text='Hello, world!')
#        self.helloLabel.pack()
#        self.quitButton = Button(self, text='Quit', command=self.quit)
#        self.quitButton.pack()
        
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        mb.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()
