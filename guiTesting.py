from tkinter import *
from PIL import Image, ImageTk
import os

source_folder = r"D:\DCIM\100MEDIA"

UI = Tk()

UI.title("AlgaeGuard v1")
UI.geometry("600x500")

lbl = Label(UI, text = "AlgaeGuard v1 gives you the ability to ensure enviromental safety from the comfort of your home")
lbl.grid()

def imgShow(path):
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(UI, image = img)
    panel.grid(column=3, row=0)


def clicked():
    lbl.configure(text = "Analyzing...")
    import HAB_Detect
    lbl.configure(text = "Images Analyzed")
    y1=4

    pabLabel = Label(UI, text = "\nPossible algae blooms:\n")
    pabLabel.grid(column=0, row=3)

    with open('pab.txt') as pabRead:
        for line in pabRead:
            newString, s, t = line.partition('[')
            file_name = r"C:\Users\25milanbm\Desktop\HAB_Detect\\" + newString
            pabButton = Button(UI, text = line, command=imgShow(file_name))
            pabButton.grid(column = 0, row = y1)
            y1=y1+1
    
    y2=y1+1

    newerLabel = Label(UI, text = "\nLikely algae free: \n")
    newerLabel.grid(column=0, row=y2)

    y2=y2+1

    with open('npab.txt') as npabRead:
        for line in npabRead:
            newString, s, t = line.partition('[')
            file_name = r"C:\Users\25milanbm\Desktop\HAB_Detect\\" + newString
            npabButton = Button(UI, text = line, command=imgShow(file_name))
            npabButton.grid(column = 0, row = y2)
            y2=y2+1


btn = Button(UI, text = "Click to analyze photos" , fg = "blue", command=clicked)
btn.grid(column=0, row=1)

UI.mainloop()