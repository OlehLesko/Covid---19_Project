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
    image_1 = im.open("Images/image of main window.png")
    resized_image = image_1.resize((2548,1176))
    photo = imtk.PhotoImage(resized_image)

    my_label = Label(root, image=photo)
    my_label.pack(pady=0, padx=0)

    button_europe = Button(root,
                           text='Europe',
                           bg='White', fg='Black',
                           font=('Arial', 20),
                           width=11, height=2)
    button_europe.place(relx=0.30, rely=0.5)


    button_ukraine = Button(root,
                            text='Ukraine',
                            bg='White', fg='Black',
                            font=('Arial', 20),
                            width=11, height=2)
    button_ukraine.place(relx=0.4, rely=0.2)

    button_asia = Button(root,
                         text='Asia',
                         bg='White', fg='Black',
                         font=('Arial', 20),
                         width=11, height=2)
    button_asia.place(relx=0.10, rely=0.20)

    root.mainloop()

if __name__ == "__main__":
    create_general_window()