from tkinter import *
from functools import partial
import tkinter.messagebox as mess
from main import utils

# https://pythonexamples.org/python-tkinter-login-form/
def check_values(n_bit, list_num, checked): 
    try:
        n_bit = int(n_bit.get())
        list_num = list(map(int, list_num.get().split(',')))
        print(n_bit)
        print(list_num)
        print(checked.get())
        mess.showinfo('Solution', utils(n_bit, list_num, checked.get()))

    except ValueError as e:
        mess.showinfo('Error', e)
    return



root = Tk()
root.geometry('800x600')
root.title('GUI')


label1_1 = Label(root, text="Number of bit.", fg='black', bg='white')
n_bit = StringVar()
entry_1 = Entry(root, textvariable=n_bit)

label1_2 = Label(root, text="List of number.", fg='black', bg='white')
list_num = StringVar()
entry_2 = Entry(root, textvariable=list_num)

label1_1.grid(row=0)
label1_2.grid(row=1)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

checked = IntVar()
c1 = Checkbutton(root, text='Sum', variable=checked)
c1.grid(columnspan=2, sticky=W)

check_values = partial(check_values, n_bit, list_num, checked)
label2_1 = Button(root, text="Submit.", command=check_values)
label2_1.grid(row=2, column=1)
# c2 = Checkbutton(root, text='Multiply')
# c2.grid(columnspan=2, sticky=W)
# label.pack(side='bottom') 



root.mainloop()