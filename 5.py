from tkinter import *
from PIL import ImageTk, Image

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

bg1 = Image.open("Images/1.png")

new_bg = ImageTk.PhotoImage(bg1)
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)


def resizer(r):
    global bg1, new_bg
    resized_bg = bg1.resize((r.width, r.height))
    new_bg = ImageTk.PhotoImage(resized_bg)

    my_canvas.create_image(0, 0, image=new_bg, anchor="nw")
    my_canvas.create_text(300, 150, text="Covid-19", fill="White", font=('Arial', 80))
    my_canvas.create_text(375, 320, text="Find out the information:", fill="White", font=('Arial', 40))

    my_canvas.create_text(1180, 25, text="Contact center of the MOZ:", fill="White", font=('Arial', 18))

    my_canvas.create_text(1242, 53, text="0 800 60 20 19", fill="White", font=('Arial', 18))


root.bind('<Configure>', resizer)

root.mainloop()
