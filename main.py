from tkinter import *

UI = Tk()

UI.title("AlgaeGuard v1")
UI.geometry("600x500")

lbl = Label(UI, text = "AlgaeGuard v1 gives you the ability to ensure enviromental safety from the comfort of your home")
lbl.grid()

def clicked():
    lbl.configure(text = "Analyzing...")
    import HAB_Detect
    lbl.configure(text = "Images Analyzed")

    p = open('pab.txt')
    n = open('npab.txt')
    pab = p.read()
    npab = n.read()

    msg = Label(UI, text = "\nPossible algae blooms:\n" + pab)  
    msg.grid(column=0, row=2)
    msg = Label(UI, text = "Likely algae free:\n" + npab) 
    msg.grid(column=0, row=3)


btn = Button(UI, text = "Click to analyze photos" , fg = "blue", command=clicked)
btn.grid(column=0, row=1)

UI.mainloop()