import Main_window
from config_file import *
from request_module import request
from get_general_vaccinated_data_asia import total_vaccinated
from tkinter import *
from PIL import Image as im
from PIL import ImageTk as imtk

def asia_function():
    asia_window = Tk()
    asia_window.state(first_window_size)
    asia_window.title('Asia')
    asia_window.iconbitmap('Images/icon.ico')

    w = asia_window.winfo_screenwidth()
    h = asia_window.winfo_screenheight()

    canvas = Canvas(asia_window,
                    width=w,
                    height=h)

    canvas.pack(fill="both", expand=True)
    asia_window.state("zoomed")
    asia_window.title('ASIA')

    image_1 = im.open("Images/Virus_E_U_A.png")

    resized_image = image_1.resize((w, h), im.ANTIALIAS)

    photo = imtk.PhotoImage(resized_image)
    canvas.create_image(0, 0, anchor=NW, image=photo)

    asia_text = Label(canvas, text="The state of\n       covid-19 in Asia", bg="#d7d5d8", font=('Arial', 56))
    asia_text.place(relx=0, rely=0.15)

    info_text = Text(asia_window, width=33, height=11, bg='#d7d5d8', font=(None, 20))
    info_text.place(relx=0.18, rely=0.36)
    canvas.pack()

    headers = headers_asia
    html = request(url_asia, headers)

    all_infected = f' Infected: {html.find("td", class_="bg-total larger").text}\n'
    deaths = f'Deaths: {html.find_all("td", class_="bg-total")[3].text}\n'
    recovered = f'Recovered: {html.find_all("td", class_="bg-total")[5].text}\n'
    now_ill = f'Now ill: {html.find_all("td", class_="bg-total")[7].text}\n'
    total_vaccinated_people = f'Total vaccinated people: {total_vaccinated()}'

    info_text.insert(1.0, f"\n{all_infected}\n\n {deaths} \n {recovered} \n {now_ill} \n {total_vaccinated_people}")
    info_text['state'] = 'disabled'

    def return_to_first_window():
        asia_window.destroy()
        Main_window.create_general_window()

    return_to_main = Button(asia_window, text='<<',
                            font=('Arial', 14), width=5, height=1, command=return_to_first_window)
    return_to_main.place(x=2, y=2)

    asia_window.mainloop()


if __name__ == "__main__":
    asia_function()