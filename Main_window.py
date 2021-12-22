from PIL import Image as im
from PIL import ImageTk as imt
from tkinter import *
from screeninfo import get_monitors
import config_file
import Europe_window
import Ukraine_window
import Asia_window
import webbrowser

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
                    width=w,height=h)

    canvas.pack(fill="both", expand=True)
    first_window.state("zoomed")
    first_window.title(config_file.first_window_title)

    image_1 = im.open("Images/Virus_Main.png")

    resized_image = image_1.resize((w, h), im.ANTIALIAS)

    photo = imt.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    # d7d5d8
    covid = Label(canvas, text='Covid-19', bg='#d7d5d8', bd=0, width=8, height=1, font=(None, 82))
    covid.place(relx=0.01, rely=0.25, )

    def site():
        webbrowser.open('https://liki24.com/uk/', new=2)

    button_ap = Button(canvas, text='Online\n      pharmacy', bg="#d7d5d8", relief=GROOVE, fg='black', font=(None, 16),
                       command=site)
    button_ap.place(relx=0.62, rely=0)

    number = Label(canvas, text="Contact center of the MOZ:\n 0 800 60 20 19", bg='#d7d5d8', font=(None, 18))
    number.pack(anchor='e')

    find_text = Label(canvas, text="Find out the information:", bg='#d7d5d8', font=(None, 28))
    find_text.place(relx=0.035, rely=0.52)

    def euro_open():
        first_window.destroy()
        Europe_window.europe_function()

    button_europe = Button(canvas,
                           text='Europe',
                           bg='White', fg='Black', command=euro_open, width=12, height=2, font=(None, 20))
    button_europe.pack(side=LEFT, padx=30, pady=80, anchor="s")

    def ukraine_open():
        first_window.destroy()
        Ukraine_window.ukraine_function()

    button_ukraine = Button(canvas,
                            text='Ukraine',
                            bg='White', fg='Black', command=ukraine_open, width=12, height=2, font=(None, 20))
    button_ukraine.pack(side=LEFT, pady=80, anchor="s")

    def asia_open():
        first_window.destroy()
        Asia_window.asia_function()

    button_asia = Button(canvas,
                         text='Asia',
                         bg='White', fg='Black', command=asia_open, width=12, height=2, font=(None, 20))
    button_asia.pack(side=LEFT, padx=30, pady=80, anchor="s")

    def resize(e):
        size = e.width


        if size > 1200:
            covid.config(font=(None, 82))
            button_ap.config(font=(None, 17))
            button_ap.place(relx=0.62, rely=0)

        elif size > 960:
            covid.config(font=(None, 80))
            button_ap.config(font=(None, 15))
            button_ap.place(relx=0.54, rely=0)

            find_text.config(font=(None, 28))
            number.config(font=(None, 18))

            button_europe.config(width=12, height=2, font=(None, 20))
            button_ukraine.config(width=12, height=2, font=(None, 20))
            button_asia.config(width=12, height=2, font=(None, 20))
        elif size > 790:
            covid.config(font=(None, 76))
            button_ap.config(font=(None, 14))
            button_ap.place(relx=0.45, rely=0)

            number.config(font=(None, 16))
            button_europe.config(width=10, height=2, font=(None, 19))
            button_ukraine.config(width=10, height=2, font=(None, 19))
            button_asia.config(width=10, height=2, font=(None, 19))
        else:
            covid.config(font=(None, 72))
            button_ap.config(font=(None, 13))
            button_ap.place(relx=0.3, rely=0)

            find_text.config(font=(None, 24))
            number.config(font=(None, 14))
            button_europe.config(width=8, height=2, font=(None, 18))
            button_ukraine.config(width=8, height=2, font=(None, 18))
            button_asia.config(width=8, height=2, font=(None, 18))

    canvas.bind('<Configure>', resize)
    first_window.mainloop()

if __name__ == "__main__":
    create_general_window()
