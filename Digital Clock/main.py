import tkinter as tk # to create graphical model interface(GUI, button, images)
from time import strftime # forward current time and date

root = tk.Tk() # create root window to display elements
root.title("Digital Clock") # create title of this window

def time(): # use time function to update current time and date
    string = strftime("%H:%M:%S %p \n %D") # strftime forwards current time date to string
    label.config(text=string) # show the time and date in written form
    label.after(1000,time) # time function will update per second and show current date and time

label = tk.Label(root, font=('calibri', 50, 'bold'), background='#282C34', foreground='#ABB2BF') # to create design
label.pack(anchor='center') # pack method is used to arrange object in window

time()

root.mainloop()