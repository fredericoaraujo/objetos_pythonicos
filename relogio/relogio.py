from tkinter import Label
from time import strftime


def tac():
    relogio['text'] = strftime('%H:%M:%S')
    relogio.after(100, tac)


relogio = Label()
relogio['font'] = 'Helvetica 80 bold'
relogio.pack()
tac()
relogio.mainloop()
