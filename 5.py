from tkinter import *
from PIL import ImageTk, Image
from screeninfo import get_monitors

root = Tk()
root.geometry("800x500")

Monitor = get_monitors()

a = Monitor[0]

w = int(a.width)
h = int(a.height)

# Define image
bg1 = Image.open("Images/image of main window.png")
resized_bg = bg1.resize((w, h), Image.ANTIALIAS)
new_bg = ImageTk.PhotoImage(resized_bg)



# Create a canvas
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=new_bg, anchor="nw")

my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50), fill="white")

if '<Configure>':
    F = get_monitors()

    G = Monitor[0]

    K = int(a.width)
    L = int(a.height)

    resized_bg2 = bg1.resize((K, L), Image.ANTIALIAS)
    new_bg2 = ImageTk.PhotoImage(resized_bg2)
    my_canvas.create_image(0, 0, image=new_bg2, anchor="nw")

    print('Hi')

# add some buttons
button1 = Button(root, text="Start")
button2 = Button(root, text="Reset Scores")
button3 = Button(root, text="Exit")

button1_window = my_canvas.create_window(10, 10, anchor="nw", window=button1)
button2_window = my_canvas.create_window(100, 10, anchor="nw", window=button2)
button3_window = my_canvas.create_window(230, 10, anchor="nw", window=button3)


# def resizer(r):
#     global bg1, resizer_bg, new_bg
#
#     bg1 = Image.open("Images/image of main window.png")
#
#     resized_bg = bg1.resize((r.width, r.height), Image.ANTIALIAS)
#
#     new_bg = ImageTk.PhotoImage(resized_bg)
#
#     my_canvas.create_image(0,0, image=new_bg, anchor="nw")
#
#     my_canvas.create_text(400, 250, text="Welcome!", font=("Helvetica", 50), fill="white")
#
#
# root.bind('<Configure>', resizer)

root.mainloop()