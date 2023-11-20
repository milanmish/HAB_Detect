from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
from functools import partial
import time

source_folder = r"D:\DCIM\100MEDIA"

UI = Tk()
UI.title("AlgaeGuard v1")
UI.geometry("800x500")

logoFile = PhotoImage(file='ImageCache\AlgaeBird.png')
UI.iconphoto(False, logoFile)

lbl = Label(UI, text="AlgaeGuard v1 gives you the ability to ensure environmental safety from the comfort of your home")
lbl.grid(row=0, column=0, columnspan=2)

left_frame = Frame(UI)
left_frame.grid(row=1, column=0, padx=10)

image_frame = Frame(UI)
image_frame.grid(row=1, column=1, padx=10)

image_objects = []
current_image = None
brightness_slider = None

def show_brightness_slider():
    global brightness_slider
    brightness_slider = Scale(image_frame, from_=0.1, to=2, resolution=0.1, label="Brightness", orient=HORIZONTAL)
    brightness_slider.set(1.0)
    brightness_slider.grid(column=0, row=1)
    brightness_slider.bind("<Motion>", update_brightness)

def update_brightness(event):
    global current_image
    if current_image is not None:
        brightened_image = ImageEnhance.Brightness(current_image).enhance(float(brightness_slider.get()))
        img = ImageTk.PhotoImage(brightened_image)
        image_label.config(image=img)
        image_label.image = img
        image_objects[-1] = img

def imgShow(path):
    global current_image

    origin = Image.open(path)
    width = 400
    height = 300
    resized_image = origin.resize((width, height), Image.BILINEAR)

    if brightness_slider is None:
        show_brightness_slider()

    brightness = brightness_slider.get()
    enhancer = ImageEnhance.Brightness(resized_image)
    brightened_image = enhancer.enhance(brightness)
    img = ImageTk.PhotoImage(brightened_image)

    image_label.config(image=img)
    image_label.image = img
    current_image = brightened_image

    image_objects.append(img)

def show_image_buttons():
    lbl.configure(text="")
    y1 = 2

    pabLabel = Label(left_frame, text="Possible algae blooms:")
    pabLabel.grid(column=0, row=1, pady=5)

    with open('pab.txt') as pabRead:
        for line in pabRead:
            file_name, s, t = line.partition('[')
            print(file_name)
            pabButton = Button(left_frame, text=line, command=partial(imgShow, file_name))
            pabButton.grid(column=0, row=y1, pady=5)
            y1 += 1

    y2 = y1 + 1
    newerLabel = Label(left_frame, text="Likely algae free:")
    newerLabel.grid(column=0, row=y2, pady=5)

    y2 += 1

    with open('npab.txt') as npabRead:
        for line in npabRead:
            file_name, s, t = line.partition('[')
            npabButton = Button(left_frame, text=line, command=partial(imgShow, file_name))
            npabButton.grid(column=0, row=y2, pady=5)
            y2 += 1

def clicked():
    lbl.configure(text="Analyzing...")
    import HAB_Detect
    lbl.configure(text="Images Analyzed")
    time.sleep(10)
    show_image_buttons()

image_label = Label(image_frame)
image_label.grid(row=0, column=0)

btn = Button(left_frame, text="Click to analyze photos", fg="blue", command=clicked)
btn.grid(column=0, row=0, pady=10)

UI.mainloop()