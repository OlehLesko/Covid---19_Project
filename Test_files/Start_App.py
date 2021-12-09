from PIL import Image as im
from PIL import ImageTk as imtk

from tkinter import *
from screeninfo import get_monitors
import config_file
import Europe_window
import Ukraine_window
import Asia_window

# ----------------

Monitor = get_monitors()

a = Monitor[0]

w = int(a.width)
h = int(a.height)

image_width = int(w / 100 * 27)
image_height = int(h / 100 * 46)


# ------------


# Creating general window of program
def create_general_window():
    first_window = Tk()
    first_window.iconbitmap('Images/icon.ico')
    # first_window.resizable(width=False, height=False)
    # ---------
    # Monitor = get_monitors()
    #
    # a = Monitor[0]
    #
    # interface_width = int(a.width)
    # interface_height = int(a.height)

    # ---------
    # print(interface_width, interface_height)

    # print(image_width, image_height)

    # w = first_window.winfo_screenwidth()
    # h = first_window.winfo_screenheight()

    canvas = Canvas(first_window,
                    width=w,
                    height=h)

    canvas.pack(fill="both", expand=True)
    first_window.state("zoomed")
    first_window.title(config_file.first_window_title)

    image_1 = im.open("Images/Image_of_main_window.png")

    # with Image.open('Images/Image_of_window_Ukraine, Europe, Asia.png') as im6:
    #     pass
    # im6.load()

    print(w, h)
    # Resize the Image using resize method
    resized_image = image_1.resize((w, h), im.ANTIALIAS)
    # new_image = ImageTk.PhotoImage(resized_image)

    photo = imtk.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=NW, image=photo)

    canvas.create_text(300, 150, text="Covid-19", fill="White", font=('Arial', 80))
    canvas.create_text(375, 320, text="Find out the information:", fill="White", font=('Arial', 40))

    canvas.create_text(1180, 25, text="Contact center of the MOZ:", fill="White", font=('Arial', 18))

    canvas.create_text(1242, 53, text="0 800 60 20 19", fill="White", font=('Arial', 18))


    def euro_open():
        first_window.destroy()
        Europe_window.europe_function()

    button_europe = Button(canvas,
                           text='Europe',
                           bg='White', fg='Black',
                           font=('Arial', 20),
                           width=11, height=2, command=euro_open)
    button_europe.place(x=120, y=500)

    def ukraine_open():
        first_window.destroy()
        Ukraine_window.Ukraine_function()

    button_ukraine = Button(canvas,
                            text='Ukraine',
                            bg='White', fg='Black',
                            font=('Arial', 20),
                            width=11, height=2, command=ukraine_open)
    button_ukraine.place(x=320, y=500)

    def asia_open():
        first_window.destroy()
        Asia_window.asia_function()

    button_asia = Button(canvas,
                         text='Asia',
                         bg='White', fg='Black',
                         font=('Arial', 20),
                         width=11, height=2, command=asia_open)
    button_asia.place(x=image_width, y=image_height)

    first_window.mainloop()


if __name__ == "__main__":
    create_general_window()
