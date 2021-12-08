from tkinter import *
from tkinter import ttk
from PIL import Image as im
from PIL import ImageTk as imtk

root = Tk()
root.geometry("400x300")

image_1 = im.open("Images/image of main window.png")
resized_image = image_1.resize((1670,800))
photo = imtk.PhotoImage(resized_image)

my_label = Label(root, image=photo)
my_label.pack(pady=0, padx=0)

button_europe = Button(root,
                       text='Europe',
                       bg='White', fg='Black',
                       font=('Arial', 20),
                       width=11, height=2)
button_europe.place(x=30, y=100)


root.mainloop()