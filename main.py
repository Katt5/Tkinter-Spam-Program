from tkinter import *
import pyautogui as pg
from time import sleep

root = Tk()
root.title("Simple Calculator")

#--------------COLOUR--------------

main_colour = "#faf3f2"
second_colour = "#b5aeae"
text_colour = "white"
root.config(bg=main_colour)



#making a text area at the top and setting its place on the screen
e = Entry(root, width=35, borderwidth=2)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

ee = Entry(root, width=35, borderwidth=2)
ee.grid(row=1, column=4, columnspan=3, padx=10, pady=10)

eee = Entry(root, width=35, borderwidth=2)
eee.grid(row=2, column=4, columnspan=3, padx=10, pady=10)
eee.grid(row=3, column=2, columnspan=3, padx=10, pady=10)
#e.insert(0, "")

def start_button():
    #FIND WAY TO CHANGE STRING TO INT IN A WAY THAT FUCKING WORKS
    currentmes = e.get()
    currentnum = ee.get()
    currentnuminter = eee.get()

    X=int(currentnum)
    Y = float(currentnuminter)

    e.delete(0, END)
    ee.delete(0, END)
    eee.delete(0, END)

    sleep(5)
    print(X)
    for i in range(X):
        pg.write(currentmes)
        pg.press('enter')
        sleep(Y)


def exit_button():
    root.destroy()


messagenum_text = Label(root,text = "Number of Messages", font='Helvetica 12 bold')
message_text = Label(root,text = "Message",font='Helvetica 12 bold')
messageinter = Label(root,text = "Message Interval",font='Helvetica 12 bold')
blank_row = Label(root,text = "blank", fg=main_colour, bg=main_colour)
blank_row1 = Label(root,text = "blank", fg=main_colour, bg=main_colour)
start = Button(root, text="Start", padx=50, pady=15,bg=second_colour, command=lambda: start_button())
exit = Button(root, text="Exit", padx=50, pady=15,bg=second_colour, command=lambda: exit_button())


#put buttons on scrn

message_text.grid(row=0,column=0, columnspan=3)
messagenum_text.grid(row=0,column=4, columnspan=3)

start.grid(row=6, column=0)
exit.grid(row=6, column=6)
blank_row.grid(row=4,column=0, columnspan=6)
blank_row1.grid(row=5,column=0, columnspan=6)
messageinter.grid(row=2,column=2, columnspan=3)



root.resizable(True, True)
root.mainloop()