from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
from functools import partial

source_folder = r"D:\DCIM\100MEDIA"

UI = Tk()

UI.title("AlgaeGuard v1")
UI.geometry("800x500")

lbl = Label(UI, text="AlgaeGuard v1 gives you the ability to ensure environmental safety from the comfort of your home")
lbl.grid()

image_label = Label(UI)

def imgShow(path, brightness=1.6):
    origin = Image.open(path)
    width = 400
    height = 300
    resized_image = origin.resize((width, height), Image.BILINEAR)

    enhancer = ImageEnhance.Brightness(resized_image)
    brightened_image = enhancer.enhance(brightness)
    img = ImageTk.PhotoImage(brightened_image)


    image_label.config(image=img)
    image_label.image = img
    image_label.place(x=300, y=100)

def clicked():
    lbl.configure(text="Analyzing...")
    import HAB_Detect
    lbl.configure(text="Images Analyzed")
    y1 = 4

    pabLabel = Label(UI, text="\nPossible algae blooms:\n")
    pabLabel.grid(column=0, row=3)

    with open('pab.txt') as pabRead:
        for line in pabRead:
            newString, s, t = line.partition('[')
            file_name = r"C:\Users\25milanbm\Desktop\HAB_Detect\\" + newString
            print(file_name)
            pabButton = Button(UI, text=line, command=partial(imgShow, file_name))
            pabButton.grid(column=0, row=y1)
            y1 = y1 + 1

    y2 = y1 + 1

    newerLabel = Label(UI, text="\nLikely algae free: \n")
    newerLabel.grid(column=0, row=y2)

    y2 = y2 + 1

    with open('npab.txt') as npabRead:
        for line in npabRead:
            newString, s, t = line.partition('[')
            file_name = r"C:\Users\25milanbm\Desktop\HAB_Detect\\" + newString
            npabButton = Button(UI, text=line, command=partial(imgShow, file_name))
            npabButton.grid(column=0, row=y2)
            y2 = y2 + 1

btn = Button(UI, text="Click to analyze photos", fg="blue", command=clicked)
btn.grid(column=0, row=1)

UI.mainloop()