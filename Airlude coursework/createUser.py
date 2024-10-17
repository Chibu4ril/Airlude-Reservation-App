# print('Hi there! Seems you are new here. Create an account to manage your bookings. ')
# fname = input('First name: ')
# lname = input('Last name: ')
# email = input('Enter your email address: ')
#
#
# def newUser(fname, lname):
#     fullName = fname + ' ' + lname
#     print(fullName)
#
#
# newUser(fname, lname)
#
#
#

from tkinter import ttk
import tkinter

root = tkinter.Tk()

style = ttk.Style()
style.layout("TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "left", "expand": 1})]
           })]
       })]
   }),
])

mbtn = ttk.Menubutton(text='Text')
mbtn.pack()
root.mainloop()