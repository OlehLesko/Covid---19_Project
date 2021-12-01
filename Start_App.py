
from subprocess import call
from tkinter import *
from screeninfo import get_monitors
import config_file
import Europe_window
import Ukraine_window
import Asia_window



# Creating general window of program
def create_general_window():
    first_window = Tk()
    first_window.iconbitmap('Images/icon.ico')
    first_window.resizable(width=False, height=False)

    # for m in get_monitors():
    Monitor = get_monitors()


    a = Monitor[0]

    interface_width = int(a.width)
    interface_height = int(a.height)
    print(interface_width, interface_height)

    image_width = int(interface_width / 100 * 34)
    image_height = int(interface_height / 100 * 43)

    print(image_width, image_height)


    canvas = Canvas(first_window,
                    width=interface_width,
                    height=interface_height)

    canvas.pack(fill="both", expand=True)
    first_window.state("zoomed")
    first_window.title(config_file.first_window_title)

    photo = PhotoImage(file='Images/image of main window.png')
    canvas.create_image(image_width, image_height, image=photo)

    canvas.create_text(300, 150, text="Covid-19", fill="White", font=('Arial', 80))
    canvas.create_text(375, 320, text="Find out the information:", fill="White", font=('Arial', 40))

    canvas.create_text(1180, 25, text="Contact center of the MOZ:", fill="White", font=('Arial', 18))

    canvas.create_text(1242, 53, text="0 800 60 20 19", fill="White", font=('Arial', 18))
    # pharm = Button(canvas, text = 'Buy medicine on the website', fg='white',font=(None, 18))
    # pharm.place(x=20, y=20)

    # label_phone_number = Label(first_window,
    #                            text='Hotline: '
    #                                 '0 800 60 20 19',
    #
    #                            fg='Black', font=('Arial', 13),
    #                            width=220, height=2, anchor="w", justify="left")
    #
    # label_phone_number.place(x=0, y=0)

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

