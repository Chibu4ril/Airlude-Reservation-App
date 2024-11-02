from tkinter import *
from tkinter import ttk
#
root = Tk()
content = ttk.Frame(root, padding=(3, 3, 12, 12))

frame = ttk.Frame(content, width=500, height=400 )

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))
bookTicket = ttk.Button(content, text='Book A Ticket').grid(column=3, row=2, columnspan=4)


updateTicket = ttk.Button(content, text='Book A Ticket').grid(column=6, row=0)
cancelTicket = ttk.Button(content, text='Book A Ticket').grid(column=6, row=1)
viewTickets = ttk.Button(content, text='Book A Ticket').grid(column=6, row=3)


quit = ttk.Button(content, text='Quit', command=root.destroy).grid(column=3, row=3)

root.mainloop()