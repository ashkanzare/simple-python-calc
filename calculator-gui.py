from tkinter import *
from main import calc


root = Tk()
root.geometry('320x335+600-300')
root.config(bg='#2b91bf')
root.resizable(0, 0)

entry = ''


def write(x):
    calc_entry.insert(END, str(x))


def add():
    global entry

    calc_entry.insert(END, ' + ')


def sub():
    global entry
    calc_entry.insert(END, ' - ')


def product():
    global entry
    calc_entry.insert(END, ' * ')


def divison():
    global entry

    calc_entry.insert(END, ' / ')


def equal():
    try:
        global entry
        entry = f'{calc_entry.get()}'
        entry = entry.replace(' ', '')
        calc_entry.delete(0, END)
        calc_entry.insert(END, '  ')
        calc_entry.insert(END, calc(entry))
    except:
        calc_entry.delete(0, END)
        calc_entry.insert(END, 'error')


def ac():
    calc_entry.delete(0, END)
    calc_entry.insert(END, '  ')


def delete():
    calc_entry.delete(calc_entry.index(INSERT) - 1)

def delete_error(event):
    if str(event.widget) not in ['.!button11', '.!button12', '.!button16', '.!button17', '.!button18', '.!button19'] and \
            calc_entry.get() == '0.0':
        calc_entry.delete(0, END)
    if calc_entry.get() == 'error' or calc_entry.get() == '  ':
        calc_entry.delete(0, END)
        calc_entry.insert(END, '0.0')





calc_entry = Entry(root, justify='right', width=24, font=('digital-7', 20))
calc_entry.grid(row=0, column=0, columnspan=4, pady=2, ipady=10, padx=1)
calc_entry.insert(END, '0.0')
calc_entry.bind("<Key>", lambda e: "break")


buttons = [Button(root, text=i, font=('digital-7', 15), width=8, height=2, borderwidth=1,
                  command=lambda k=i: write(k), bg='#74c4e7') for i in range(0, 10)]

button_rp = Button(root, text='(', font=('digital-7', 15), width=8, height=2, borderwidth=1,
                   command=lambda: write(' ( '), bg='#2b91bf')
button_lp = Button(root, text=')', font=('digital-7', 15), width=8, height=2, borderwidth=1,
                   command=lambda: write(' ) '), bg='#2b91bf')
button_clear = Button(root, text='AC', font=('digital-7', 15), width=8, height=2, borderwidth=1, command=ac,
                      bg='#2b91bf')
button_delete = Button(root, text='C', font=('digital-7', 15), width=8, height=2, borderwidth=1, command=delete,
                       bg='#2b91bf')
button_dot = Button(root, text='•', font=('digital-7', 15), width=8, height=2, borderwidth=1,
                    command=lambda: write('.'), bg='#2b91bf')
button_sum = Button(root, text='+', font=('digital-7', 15), width=8, height=2, borderwidth=1, command=add,
                    bg='#2b91bf')
button_sub = Button(root, text='-', font=('digital-7', 15), width=8, height=2, borderwidth=1, command=sub,
                    bg='#2b91bf')
button_pro = Button(root, text='*', font=('digital-7', 15), width=8, height=2, borderwidth=1, command=product,
                    bg='#2b91bf')
button_div = Button(root, text='/', font=('digital-7', 15), width=8, height=2, borderwidth=1, command=divison,
                    bg='#2b91bf')
button_equal = Button(root, text='=', font=('digital-7', 15), width=8, height=2, borderwidth=1, command=equal,
                      bg='#2b91bf')

all_buttons = [button_rp, button_lp, button_delete, button_dot, button_sum, button_sub, button_pro, button_div] + buttons
for button in all_buttons:
    button.bind("<Button-1>", delete_error)
    button.bind("<FocusIn>", delete_error)


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
