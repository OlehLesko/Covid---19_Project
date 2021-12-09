from tkinter import *
from tkinter import ttk
from PIL import Image as im
from PIL import ImageTk as imtk
from screeninfo import get_monitors

Monitor = get_monitors()

a = Monitor[0]

w = int(a.width)
h = int(a.height)

def create_general_window():
    root = Tk()

    fon_image = im.open("Images/Image_of_main_window.png")
    resized_image = fon_image.resize((2548, 1176))
    fon_photo = imtk.PhotoImage(resized_image)


    label_photo = Label(root, image=fon_photo)
    label_photo.pack(pady=0, padx=0)

    label_covid19 = Label(root, text='Covid-19',
                              font=('Arial', 85),
                              width=7, height=1,
                              bg='Black', fg='White')
    label_covid19.place(relx=0.01, rely=0.14)

    label_find_out_the_information = Label(root,
                                               text="Find out the information:",
                                               font=('Arial', 35),
                                               width=19, height=1,
                                               bg='Black', fg='White')
    label_find_out_the_information.place(relx=0.01, rely=0.37)

    label_contact_center_of_the_MOZ = Label(root,
                                                text="Contact center of the MOZ:",
                                                font=('Arial', 20),
                                                width=21, height=1,
                                                bg='Black', fg='White')
    label_contact_center_of_the_MOZ.place(relx=0.77, rely=0.0009)

    label_number_contact_center = Label(root,
                                            text="0 800 60 20 19",
                                            font=('Arial', 20),
                                            width=21, height=1,
                                            bg='Black', fg='White')
    label_number_contact_center.place(relx=0.81, rely=0.058)

    button_europe = Button(root,
                           text='Europe',
                           bg='White', fg='Black',
                           font=('Arial', 20),
                           width=11, height=2)
    button_europe.place(relx=0.065, rely=0.62)


    button_ukraine = Button(root,
                            text='Ukraine',
                            bg='White', fg='Black',
                            font=('Arial', 20),
                            width=11, height=2)
    button_ukraine.place(relx=0.205, rely=0.62)

    button_asia = Button(root,
                         text='Asia',
                         bg='White', fg='Black',
                         font=('Arial', 20),
                         width=11, height=2)
    button_asia.place(relx=0.345, rely=0.62)

    # root.wm_attributes('-transparent', 'black')

    root.mainloop()

if __name__ == "__main__":
    create_general_window()