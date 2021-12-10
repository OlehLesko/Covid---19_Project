from PIL import Image as im
from PIL import ImageTk as imtk

from tkinter import *
from screeninfo import get_monitors
import config_file
import Europe_window
import Ukraine_window
import Asia_window

Monitor = get_monitors()

a = Monitor[0]

w = int(a.width)
h = int(a.height)

image_width = int(w / 100 * 27)
image_height = int(h / 100 * 46)


def create_general_window():
    first_window = Tk()
    first_window.iconbitmap('Images/icon.ico')
    first_window.minsize(500, 450)

    canvas = Canvas(first_window,
                    width=w,
                    height=h)

    canvas.pack(fill="both", expand=True)
    first_window.state("zoomed")
    first_window.title(config_file.first_window_title)

    image_1 = im.open("Images/Virus_Main.png")

    resized_image = image_1.resize((w, h), im.ANTIALIAS)

    photo = imtk.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=NW, image=photo)

    covid = Label(canvas, text='Covid-19', bg='#d7d5d8', font=(None, 80))
    covid.place(relx=0.01, rely=0.3,)

    button_onl = Button(canvas, text='Online')
    button_onl.place(relx=0.001, rely=0.01)

    number = Label(canvas, text="Contact center of the MOZ:\n 0 800 60 20 19", bg='#d7d5d8')
    number.pack(anchor='e')

    find_text = Label(canvas, text="Find out the information:", bg='#d7d5d8', font=(None, 28))
    find_text.place(relx=0.03, rely=0.6)

    def euro_open():
        first_window.destroy()
        Europe_window.europe_function()

    button_europe = Button(canvas,
                           text='Europe',
                           bg='White', fg='Black',
                            command=euro_open)
    button_europe.pack(side=LEFT, padx=30, pady=40, anchor="s")

    def ukraine_open():
        first_window.destroy()
        Ukraine_window.Ukraine_function()

    button_ukraine = Button(canvas,
                            text='Ukraine',
                            bg='White', fg='Black',
                             command=ukraine_open)
    button_ukraine.pack(side=LEFT, pady=40, anchor="s")

    def asia_open():
        first_window.destroy()
        Asia_window.asia_function()

    button_asia = Button(canvas,
                         text='Asia',
                         bg='White', fg='Black',
                        command=asia_open)
    button_asia.pack(side=LEFT, padx=30, pady=40, anchor="s")
    def resize(e):
        size = e.width
        ysize = e.height
        print(size)
        if size > 970:
            number.config(font=(None, 18))
            button_europe.config(width=12,height=2,font=(None,20))
            button_ukraine.config(width=12,height=2,font=(None,20))
            button_asia.config(width=12,height=2,font=(None,20))
        elif size > 800:
            number.config(font=(None, 16))
            button_europe.config(width=10, height=2, font=(None, 19))
            button_ukraine.config(width=10, height=2, font=(None, 19))
            button_asia.config(width=10, height=2, font=(None, 19))
        else:
            number.config(font=(None, 14))
            button_europe.config(width=8, height=2, font=(None, 18))
            button_ukraine.config(width=8, height=2, font=(None, 18))
            button_asia.config(width=8, height=2, font=(None, 18))

    canvas.bind('<Configure>', resize)

    first_window.mainloop()


if __name__ == "__main__":
    create_general_window()
