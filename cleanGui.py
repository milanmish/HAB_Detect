import tkinter
import tkinter.messagebox
import customtkinter
import time
from PIL import Image, ImageTk, ImageEnhance
from functools import partial

self = customtkinter.CTk()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

image_objects = []
current_image = None
brightness_slider = None

def show_brightness_slider():
    global brightness_slider
    self.brightnessSlider = customtkinter.CTkSlider(self.imgFrame, from_=0.1, to=2, number_of_steps=50)
    self.brightnessSlider.set(1.05)
    self.brightnessSlider.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky="ew")

def update_brightness(event):
    global current_image
    if current_image is not None:
        brightened_image = ImageEnhance.Brightness(current_image).enhance(float(self.brightnessSlider.get()))
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

    brightness = self.brightnessSlider.get()
    enhancer = ImageEnhance.Brightness(resized_image)
    brightened_image = enhancer.enhance(brightness)
    img = ImageTk.PhotoImage(brightened_image)

    image_label.config(image=img)
    image_label.image = img
    current_image = brightened_image

    image_objects.append(img)

def show_image_buttons():
    self.configure(text="")
    y1 = 2

    pabLabel = customtkinter.CTkLabel(self.sidebar_frame, text="Possible algae blooms:")
    pabLabel.grid(column=0, row=1, pady=5)

    with open('pab.txt') as pabRead:
        for line in pabRead:
            file_name, s, t = line.partition('[')
            print(file_name)
            pabButton = customtkinter.CTkButton(self.sidebar_frame, text=line, command=partial(imgShow, file_name))
            pabButton.grid(column=0, row=y1, pady=5)
            y1 += 1

    y2 = y1 + 1
    newerLabel = customtkinter.CTkLabel(self.sidebar_frame, text="Likely algae free:")
    newerLabel.grid(column=0, row=y2, pady=5)

    y2 += 1

    with open('npab.txt') as npabRead:
        for line in npabRead:
            file_name, s, t = line.partition('[')
            npabButton = customtkinter.CTkButton(self.sidebar_frame, text=line, command=partial(imgShow, file_name))
            npabButton.grid(column=0, row=y2, pady=5)
            y2 += 1

def imgCheckClicked():
    self.imgLbl.configure(text="Images Analyzed")
    import HAB_Detect

# configure window
self.title("AlgaeGuard v1")
self.geometry(f"{1100}x{580}")
              
# configure grid layout (4x4)
self.grid_columnconfigure(1, weight=1)
self.grid_columnconfigure((2, 3), weight=0)
self.grid_rowconfigure((0, 1, 2), weight=1)

# create sidebar frame with widgets
self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
self.sidebar_frame.grid_rowconfigure(4, weight=1)

self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)

self.imgFrame = customtkinter.CTkFrame(self, width=250, height = 300)
self.imgFrame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

image_label = customtkinter.CTkLabel(self.imgFrame)
image_label.grid(row=0, column=0)

self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="AlgaeGuard v1", font=customtkinter.CTkFont(size=20, weight="bold"))
self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
self.imgLbl = customtkinter.CTkLabel(self.sidebar_frame, text = "CtKLabel", font=customtkinter.CTkFont(size=12, weight="normal"))
self.imgLbl.grid(row = 2, column=0, padx=20, pady=5)

self.imgCheck = customtkinter.CTkButton(self.sidebar_frame, text = "Click to Analyze Photos", font=customtkinter.CTkFont(size=12, weight="normal"), command=imgCheckClicked)
self.imgCheck.grid(row=1, column=0, padx=20, pady=10)

show_brightness_slider()

self.mainloop()