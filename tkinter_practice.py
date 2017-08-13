from tkinter import *

from PIL import Image, ImageTk

# create a window that you can resize, min/max, delete
# Frame is a class within tkinter module

class Window(Frame):

    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init__window()

    def init__window(self):

        self.master.title('GUI')

        self.pack(fill=BOTH, expand=1)

        # quitButton = Button(self, text='Quit', command=self.client_exit)
        # quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo')
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def showImg(self):
        load = Image.open('cartman.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self, text='Respect my authority')
        text.pack()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
root.geometry('400x300')

#creation of an instance
app = Window(root)

#mainloop
root.mainloop()