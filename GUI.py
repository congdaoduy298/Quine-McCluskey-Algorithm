from tkinter import *
from functools import partial
import tkinter.messagebox as mess
from main import utils
import re 



def show_result(result):
    top = Tk()
    top.title('Solution')
    height = re.findall(r'\n', result)
    # print(len(height))
    text = Text(top, height=len(height), width=60)

    text.config(state='normal')
    text.insert(INSERT, result)
    text.config(state='disable')

    text.pack()
    top.mainloop()
    
# https://pythonexamples.org/python-tkinter-login-form/
def check_values(n_bit, list_num, checked): 
    try:
        n_bit = int(n_bit.get())
        if ',' in list_num.get():
            list_num = list(map(int, list_num.get().split(',')))
        else :
            list_num = list(map(int, list_num.get().split()))

        print(n_bit)
        print(list_num)
        print(checked.get())
        # mess.showinfo('Solution', utils(n_bit, list_num, checked.get()))
        show_result(utils(n_bit, list_num, checked.get()))

    except ValueError as e:
        mess.showerror('Error', e)
    return

def showHelp():
    print("Ha ha you are a joke :))")

    mess.showinfo('Idea', 'Number of bit = the number of variables you want.\
        \n\nList of number = List of integer separated by spaces or commas.\
        \n\nSum: if it is selected returns sum of product (SOP),\
        otherwise returns product of sum (POS) ')

root = Tk()
root.geometry('800x600')
root.title('Quine McCluskey Algorithm')


label1_1 = Label(root, text="Number of bit.", fg='black')
n_bit = StringVar()
entry_1 = Entry(root, textvariable=n_bit)

label1_2 = Label(root, text="List of number.", fg='black')
list_num = StringVar()
entry_2 = Entry(root, textvariable=list_num, width=100)

label1_1.grid(row=0)
label1_2.grid(row=1)

entry_1.grid(row=0, column=1, sticky=W)
entry_2.grid(row=1, column=1, sticky=W)

checked = IntVar()
c1 = Checkbutton(root, text='Sum', variable=checked)
c1.grid(columnspan=2, sticky=W)

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='Variables...', command=showHelp)

check_values = partial(check_values, n_bit, list_num, checked)
label2_1 = Button(root, text="Submit.", command=check_values)
label2_1.grid(row=2, column=1)

root.mainloop()