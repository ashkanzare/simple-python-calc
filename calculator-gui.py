from tkinter import *

root = Tk()
root.geometry('315x245+200-50')
root.config(bg='#61659d')

entry = 0

def write(x):
    calc_entry.insert(END, str(x))

def add():
    global entry
    entry = float(calc_entry.get()), '+'
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')

def sub():
    global entry
    entry = float(calc_entry.get()), '-'
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')

def product():
    global entry
    entry = float(calc_entry.get()), '*'
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')

def divison():
    global entry
    entry = float(calc_entry.get()), '/'
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')

def equal():
    if entry[-1] == '+':
        value = entry[0] + float(calc_entry.get())
    elif entry[-1] == '-':
        value = entry[0] - float(calc_entry.get())
    elif entry[-1] == '*':
        value = entry[0] * float(calc_entry.get())
    elif entry[-1] == '/':
        value = entry[0] / float(calc_entry.get())
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')
    calc_entry.insert(END, value)


calc_entry = Entry(root, justify='left', width=40, font=('Arial', 10))
calc_entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=10, padx=5)
calc_entry.insert(END, '  ')

button_1 = Button(root, text=1, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(1), bg='#878cd7')
button_2 = Button(root, text=2, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(2), bg='#878cd7')
button_3 = Button(root, text=3, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(3), bg='#878cd7')

button_4 = Button(root, text=4, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(4), bg='#878cd7')
button_5 = Button(root, text=5, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(5), bg='#878cd7')
button_6 = Button(root, text=6, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(6), bg='#878cd7')

button_7 = Button(root, text=7, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(7), bg='#878cd7')
button_8 = Button(root, text=8, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(8), bg='#878cd7')
button_9 = Button(root, text=9, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(9), bg='#878cd7')

button_0 = Button(root, text=0, font=('Arial', 12), width=8, height=2, borderwidth=1, command=lambda: write(0), bg='#878cd7')
button_dot = Button(root, text='●', font=('Arial', 5), width=8, height=2, borderwidth=0, command=lambda: write('.'), bg='#61659d')

button_sum = Button(root, text='+', font=('Arial', 12), width=8, height=2, borderwidth=1, command=add, bg='#61659d')
button_sub = Button(root, text='-', font=('Arial', 12), width=8, height=2, borderwidth=1, command=sub, bg='#61659d')
button_pro = Button(root, text='*', font=('Arial', 12), width=8, height=2, borderwidth=1, command=product, bg='#61659d')
button_div = Button(root, text='/', font=('Arial', 12), width=8, height=2, borderwidth=1, command=divison, bg='#61659d')
button_equal = Button(root, text='=', font=('Arial', 12), width=8, height=2, borderwidth=1, command=equal, bg='#61659d')


button_1.grid(row=1, column=0, padx=0)
button_2.grid(row=1, column=1, padx=0)
button_3.grid(row=1, column=2, padx=0)
button_sum.grid(row=1, column=3, padx=0)

button_4.grid(row=2, column=0, padx=0)
button_5.grid(row=2, column=1, padx=0)
button_6.grid(row=2, column=2, padx=0)
button_sub.grid(row=2, column=3, padx=0)

button_7.grid(row=3, column=0, padx=0)
button_8.grid(row=3, column=1, padx=0)
button_9.grid(row=3, column=2, padx=0)
button_pro.grid(row=3, column=3, padx=0)

button_dot.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_div.grid(row=4, column=3)

root.mainloop()