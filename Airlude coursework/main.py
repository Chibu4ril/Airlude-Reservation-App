# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# frame = ttk.Frame(root, padding=10)
#
# frame.grid()
#
# ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
#
# ttk.Button(frame, text="Quit", command=root.destroy).grid(column=0, row=1)
#
# root.mainloop()

class BookTicket:
    def __init__(self):
        print('Here we start')

    def create(self, fname):
        print('new')
        return

createTicket = BookTicket.create(fname='')