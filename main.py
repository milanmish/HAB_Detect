from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
from functools import partial
import time

source_folder = r"D:\DCIM\100MEDIA"

UI = Tk()
UI.title("AlgaeGuard v1")
UI.geometry("800x500")

lbl = Label(UI, text="AlgaeGuard v1 gives you the ability to ensure environmental safety from the comfort of your home")
lbl.grid(row=0, column=0, columnspan=2)

# Create a Frame for the left-hand side buttons
left_frame = Frame(UI)
left_frame.grid(row=1, column=0, padx=10)

# Create a Frame for the right-hand side content
right_frame = Frame(UI)
right_frame.grid(row=1, column=1, padx=10)

# Create a list to store image objects
image_objects = []
current_image = None  # Initialize the current image variable

# Add a callback to update the brightness when the slider is moved
brightness_slider = Scale(right_frame, from_=0.1, to=2, resolution=0.1, label="Brightness", orient=HORIZONTAL)
brightness_slider.set(1.0)  # Set the default brightness to 1.0

def show_brightness_slider():
    brightness_slider.grid(column=0, row=1)

def imgShow(path):
    global current_image

    origin = Image.open(path)
    width = 400
    height = 300
    resized_image = origin.resize((width, height), Image.BILINEAR)

    # Get the brightness value from the slider
    brightness = brightness_slider.get()
    enhancer = ImageEnhance.Brightness(resized_image)
    brightened_image = enhancer.enhance(brightness)
    img = ImageTk.PhotoImage(brightened_image)

    image_label.config(image=img)
    image_label.image = img
    current_image = brightened_image  # Update the current image for brightness adjustments

    # Store the image object in the list
    image_objects.append(img)
    show_brightness_slider()  # Show the brightness slider after the image is created

def update_brightness(event):
    if current_image is not None:
        # Get the brightness value from the slider and update the displayed image
        brightness = float(brightness_slider.get())
        brightened_image = ImageEnhance.Brightness(current_image).enhance(brightness)
        img = ImageTk.PhotoImage(brightened_image)
        image_label.config(image=img)
        image_label.image = img
        image_objects[-1] = img  # Update the stored image

def show_image_buttons():
    # This function should be called after the initial button click
    lbl.configure(text="")
    y1 = 2

    pabLabel = Label(left_frame, text="Possible algae blooms:")
    pabLabel.grid(column=0, row=1, pady=5)

    with open('pab.txt') as pabRead:
        for line in pabRead:
            newString, s, t = line.partition('[')
            file_name = r"C:\Users\25milanbm\Desktop\HAB_Detect\\" + newString
            pabButton = Button(left_frame, text=line, command=partial(imgShow, file_name))
            pabButton.grid(column=0, row=y1, pady=5)  # Add padding to create space
            y1 += 1

    y2 = y1 + 1
    newerLabel = Label(left_frame, text="Likely algae free:")
    newerLabel.grid(column=0, row=y2, pady=5)  # Add padding to create space

    y2 += 1

    with open('npab.txt') as npabRead:
        for line in npabRead:
            newString, s, t = line.partition('[')
            file_name = r"C:\Users\25milanbm\Desktop\HAB_Detect\\" + newString
            npabButton = Button(left_frame, text=line, command=partial(imgShow, file_name))
            npabButton.grid(column=0, row=y2, pady=5)  # Add padding to create space
            y2 += 1

def clicked():
    lbl.configure(text="Analyzing...")
    import HAB_Detect
    lbl.configure(text="Images Analyzed")
    time.sleep(10)
    show_image_buttons()

image_label = Label(right_frame)
image_label.grid(row=0, column=0)

btn = Button(left_frame, text="Click to analyze photos", fg="blue", command=clicked)
btn.grid(column=0, row=0, pady=10)  # Add padding to create space

UI.mainloop()
