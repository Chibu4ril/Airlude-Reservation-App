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
#
# # class BookTicket:
# #     def __init__(self):
# #         self.print('Here we start')
# #
# #     def create(self, fname):
# #         self.print('new')
# #         return
# #
# # createTicket = BookTicket.create()
# #
#
num = range(0,100)
leftWindow = []
rightWindow = []
for i in num:
    if i % 3 == 0:
        leftWindow.append(i)
        # perform action for left window

        rightWindow.append(i + 2)
        # perform action for left window


print(leftWindow)
print(rightWindow)

