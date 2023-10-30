from tkinter import *

count =0


def click():
    global count
    count +=1
    print(count, "You clicked on the button!")

window = Tk()
#photoB = PhotoImage(file='pngtree.jpg')
button = Button(window, 
                text = 'click me!',
                command = click,
                font = ("Comic Sans", 25),
                fg = "#00FF00",
                bg = "black",
                activeforeground= "#00FF00",
                activebackground="black",
                state = ACTIVE,
#                image = photoB,
                compound='bottom'
                )
button.pack()


window.mainloop()
