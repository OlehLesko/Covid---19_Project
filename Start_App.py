from subprocess import call
from tkinter import *
import config_file


# Creating general window of program
def create_general_window():
    first_window = Tk()
    first_window.iconbitmap('icon.ico')

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

    label_phone_number = Label(first_window,
                               text='Гаряча лінія: '
                                    '0 800 60 20 19',

                               fg='Black', font=('Arial', 14),
                               width=70, height=1, anchor="w", justify="left")

    label_phone_number.place(x=0, y=0)

    def euro_open():
        first_window.destroy()
        # call(["python", "Europe_window.py"])
        import Europe_window

    button_europe = Button(canvas,
                           text='Europe',
                           bg='White', fg='Black',
                           font=('Arial', 14),
                           width=11, height=2, command=euro_open)
    button_europe.place(x=360, y=240)

    def ukraine_open():
        first_window.destroy()
        # call(["python", "Ukraine_window.py"])
        import Ukraine_window

    button_ukraine = Button(canvas,
                            text='Ukraine',
                            bg='White', fg='Black',
                            font=('Arial', 14),
                            width=11, height=2, command=ukraine_open)
    button_ukraine.place(x=495, y=240)

    def asia_open():
        first_window.destroy()
        # call(["python", "Asia_window.py"])
        import Asia_window

    button_asia = Button(canvas,
                         text='Asia',
                         bg='White', fg='Black',
                         font=('Arial', 14),
                         width=11, height=2, command=asia_open)
    button_asia.place(x=630, y=240)

    first_window.mainloop()


if __name__ == "__main__":
    create_general_window()
