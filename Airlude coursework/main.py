from tkinter import *
from tkinter.ttk import *

# Initializing the main frame window with a Title bar
root = Tk()
root.title('Welcome to Airlude - Your best flight reservation app!')

frameSize = Frame(root, padding=)


frame = Frame(root, padding=10)

frame.grid()

Label(frame, text="Hello World!").grid(column=0, row=0)

Button(frame, text="Quit", command=root.destroy).grid(column=0, row=1)

root.mainloop()

