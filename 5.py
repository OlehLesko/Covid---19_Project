from tkinter import *
from PIL import ImageTk, Image
from screeninfo import get_monitors
import ctypes

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
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screensize)

    guuf = Image.open("Images/image of main window.png")
    bxhdhgfx = guuf.resize((user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)), Image.ANTIALIAS)
    bfcgufcu2 = ImageTk.PhotoImage(bxhdhgfx)
    my_canvas.create_image(root, 0, 0, image=bfcgufcu2, anchor="nw")

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