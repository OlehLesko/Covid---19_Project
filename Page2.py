from tkinter import *
from PIL import Image, ImageTk
from django.conf.locale import tk

import config_file


# Creating general window of program
def create_general_window():
    first_window = Tk()

    canvas_width = 1005
    canvas_height = 1000
    canvas = Canvas(first_window,
               width=canvas_width,
               height=canvas_height)
    canvas.pack()
    first_window.geometry(config_file.first_window_size)
    first_window.title(config_file.first_window_title)
    # first_window['bg'] = config_file.first_window_background

    # img = (Image.open('covid19 title.png'))
    # resize_image = img.resize((300, 205), Image.ANTIALIAS)
    # new_img = ImageTk.PhotoImage(resize_image)
    photo = PhotoImage(file='covid19 title.png')
    canvas.create_image(370, 200, image=photo)


# --------------
    # w = Label(first_window, image=photo)
    # w.place(x=-2, y=20)

# ----------
    # c.create_text(50, 50, text="whatever", fill="blue")
    canvas.create_text(50, 50, text="Covid-19", fill="grey", font="Verdana 19")

    #Labels
    # Text_first_window = Label(first_window,
    #                           text='Covid-19',
    #                           bg='Blue', fg='White',
    #                           font=('Arial', 35),
    #                           width=10, height=1)

    # c = tk.Canvas(root)
    # c.pack()
    # c.create_image(x, y, img)
    # c.create_text(x, y, "My Text")









    # first_window.wm_attributes("-transparentcolor", 'Blue')
    # Text_first_window.
    # Text_first_window.place(x=205, y=110)

    Label_Phone_Number = Label(first_window,
                               text = 'Гаряча лінія: '
                                      '0 800 60 20 19',

                               fg='Black', font=('Arial', 15),
                               width=70, height=1, anchor="w", justify="left")

    Label_Phone_Number.place(x=0, y=0)



    #Buttons
    Button_Europe_first_window = Button(canvas,
                                        text='Europe',
                                        bg='Black', fg='White',
                                        font=('Arial', 13),
                                        width=17, height=2)
    Button_Europe_first_window.place(x=20, y=220)
    Button_Ukraine_first_window = Button(canvas,
                                         text='Ukraine',
                                         bg='Black', fg='White',
                                         font=('Arial', 13),
                                         width=19, height=2)
    Button_Ukraine_first_window.place(x=212, y=220)

    Button_Asia_first_window = Button(canvas,
                                      text='Asia',
                                      bg='Black', fg='White',
                                      font=('Arial', 13),
                                      width=17, height=2)
    Button_Asia_first_window.place(x=420, y=220)

    first_window.mainloop()


if __name__ == "__main__":
    create_general_window()
