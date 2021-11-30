from subprocess import call
from tkinter import *
import config_file
import Europe_window
import Ukraine_window
import Asia_window
# import pyautogui
# res = pyautogui.size()
# print(res)

# Creating general window of program
def create_general_window():
    first_window = Tk()
    first_window.iconbitmap('Images/icon.ico')
    first_window.resizable(width=True, height=True)
    # canvas_width = 2000
    # canvas_height = 2000

    w = first_window.winfo_screenwidth()
    h = first_window.winfo_screenheight()

    canvas = Canvas(first_window,
                    width=w,
                    height=h)
    canvas.pack(fill="both", expand=True)
    first_window.state("zoomed")
    # first_window.geometry(f'{config_file.canvas_width}x{config_file.canvas_height}')
    first_window.title(config_file.first_window_title)

    photo = PhotoImage(file='Images/image of main window.png')
    canvas.create_image(600, 300, image=photo)

    canvas.create_text(300, 150, text="Covid-19", fill="White", font=('Arial', 80))
    canvas.create_text(375, 320, text="Find out the information:", fill="White", font=('Arial', 40))

    label_phone_number = Label(first_window,
                               text='Hotline: '
                                    '0 800 60 20 19',

                               fg='Black', bg='white', font=('Arial', 13),
                               width=220, height=1, anchor="w", justify="left")

    label_phone_number.place(x=0, y=0)

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
    button_asia.place(x=520, y=500)

    first_window.mainloop()


if __name__ == "__main__":
    create_general_window()
