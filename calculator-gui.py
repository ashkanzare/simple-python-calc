from tkinter import *
from main import calc

# todo: covert .1 -> 0.1 | 2( -> 2*( | )2 -> )*2
root = Tk()
root.geometry('315x400+600-300')
root.config(bg='#61659d')

entry = ''


def write(x):
    calc_entry.insert(END, str(x))


def add():
    global entry
    # entry += f'{calc_entry.get()}+'
    # calc_entry.delete(0, END)
    calc_entry.insert(END, ' + ')


def sub():
    global entry
    # calc_entry.delete(0, END)
    calc_entry.insert(END, ' - ')


def product():
    global entry
    # entry += f'{calc_entry.get()}*'
    # calc_entry.delete(0, END)
    calc_entry.insert(END, ' * ')


def divison():
    global entry
    # entry += f'{calc_entry.get()}/'
    # calc_entry.delete(0, END)
    calc_entry.insert(END, ' / ')


def equal():
    global entry
    print(calc_entry.get())
    entry = f'{calc_entry.get()}'
    entry = entry.replace(' ', '')
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')
    print(entry.replace(' ', ''))
    calc_entry.insert(END, calc(entry))


def ac():
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')


def delete():
    calc_entry.delete(calc_entry.index(INSERT) - 1)


calc_entry = Entry(root, justify='left', width=40, font=('Arial', 10))
calc_entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=10, padx=5)
calc_entry.insert(END, '  ')

buttons = [Button(root, text=i, font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1,
                  command=lambda k=i: write(k), bg='#878cd7') for i in range(0, 10)]

button_rp = Button(root, text='(', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1,
                   command=lambda: write('('), bg='#61659d')
button_lp = Button(root, text=')', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1,
                   command=lambda: write(')'), bg='#61659d')
button_clear = Button(root, text='AC', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1, command=ac,
                      bg='#61659d')
button_delete = Button(root, text='C', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1, command=delete,
                       bg='#61659d')
button_dot = Button(root, text='.', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1,
                    command=lambda: write('.'), bg='#61659d')
button_sum = Button(root, text='+', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1, command=add,
                    bg='#61659d')
button_sub = Button(root, text='-', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1, command=sub,
                    bg='#61659d')
button_pro = Button(root, text='*', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1, command=product,
                    bg='#61659d')
button_div = Button(root, text='/', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1, command=divison,
                    bg='#61659d')
button_equal = Button(root, text='=', font=('A Iranian Sans', 15), width=8, height=2, borderwidth=1, command=equal,
                      bg='#61659d')

button_clear.grid(row=1, column=0, padx=0)
button_delete.grid(row=1, column=1, padx=0)
button_rp.grid(row=1, column=2, padx=0)
button_lp.grid(row=1, column=3, padx=0)

buttons[1].grid(row=2, column=0, padx=0)
buttons[2].grid(row=2, column=1, padx=0)
buttons[3].grid(row=2, column=2, padx=0)
button_sum.grid(row=2, column=3, padx=0)

buttons[4].grid(row=3, column=0, padx=0)
buttons[5].grid(row=3, column=1, padx=0)
buttons[6].grid(row=3, column=2, padx=0)
button_sub.grid(row=3, column=3, padx=0)

buttons[7].grid(row=4, column=0, padx=0)
buttons[8].grid(row=4, column=1, padx=0)
buttons[9].grid(row=4, column=2, padx=0)
button_pro.grid(row=4, column=3, padx=0)

button_dot.grid(row=5, column=0)
buttons[0].grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_div.grid(row=5, column=3)

root.mainloop()
