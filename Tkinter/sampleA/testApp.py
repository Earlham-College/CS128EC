#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
root = Tk()
root.title("Javier Orduz")
root.geometry("300x300")
app = Frame(root)
app.grid()
message = str("Hola mundo")
lbl = Label(app, text = message)
lbl.grid()
root.mainloop()
