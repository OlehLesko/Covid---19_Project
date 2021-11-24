from subprocess import call
from tkinter import *
from django.conf.locale import tk

import config_file


# Creating general window of program
def create_general_window():
    first_window = Tk()
    first_window.iconbitmap('Coronavirus-300x300.ico')

    canvas_width = 1005
    canvas_height = 1000
    canvas = Canvas(first_window,
                    width=canvas_width,
                    height=canvas_height)
    canvas.pack()
    first_window.geometry(config_file.first_window_size)
    first_window.title(config_file.first_window_title)

    photo = PhotoImage(file='covid19 title.png')
    canvas.create_image(370, 200, image=photo)

    canvas.create_text(470, 80, text="Covid-19", fill="White", font=('Arial', 42))
    canvas.create_text(515, 180, text="Find out the information:", fill="White", font=('Arial', 20))

    Label_Phone_Number = Label(first_window,
                               text='Гаряча лінія: '
                                    '0 800 60 20 19',

                               fg='Black', font=('Arial', 14),
                               width=70, height=1, anchor="w", justify="left")

    Label_Phone_Number.place(x=0, y=0)

    def Open():
        first_window.destroy()
        call(["python", "Europe_window_all.py"])

    Button_Europe_first_window = Button(canvas,
                                        text='Europe',
                                        bg='White', fg='Black',
                                        font=('Arial', 14),
                                        width=11, height=2, command=Open)
    Button_Europe_first_window.place(x=360, y=240)

    def Open2():
        pass

    Button_Ukraine_first_window = Button(canvas,
                                         text='Ukraine',
                                         bg='White', fg='Black',
                                         font=('Arial', 14),
                                         width=11, height=2, command=Open2)
    Button_Ukraine_first_window.place(x=495, y=240)

    def Open3():
        first_window.destroy()
        call(["python", "asia_data.py"])

    Button_Asia_first_window = Button(canvas,
                                      text='Asia',
                                      bg='White', fg='Black',
                                      font=('Arial', 14),
                                      width=11, height=2, command=Open3)
    Button_Asia_first_window.place(x=630, y=240)

    first_window.mainloop()


if __name__ == "__main__":
    create_general_window()
