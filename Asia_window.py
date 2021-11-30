import Start_App
import config_file
from request_module import request
from get_general_vaccinated_data_asia import total_vaccinated
from tkinter import *

def Asia_function():
    root = Tk()
    root.geometry(config_file.first_window_size)
    root.title('Asia')
    root.iconbitmap('Images/icon.ico')
    root.resizable(width=False, height=False)


    canvas = Canvas(root,
                    width=config_file.canvas_width,
                    height=config_file.canvas_height)
    photo = PhotoImage(file='Images/second_win_image.png')

    canvas.create_image(370, 200, image=photo)
    canvas.create_text(190, 110, text="The state of\ncovid-19 in Asia", fill="White", font=('Arial', 36))
    info_text = Text(root, width=31, height=16, bg='light gray', font=(None, 13))
    info_text.place(x=460, y=50)
    canvas.pack()

    headers = config_file.headers_asia
    html = request(config_file.url_asia, headers)

    all_infected = f' Infected: {html.find("td", class_="bg-total larger").text}\n'
    deaths = f'Deaths: {html.find_all("td", class_="bg-total")[3].text}\n'
    recovered = f'Recovered: {html.find_all("td", class_="bg-total")[5].text}\n'
    now_ill = f'Now ill: {html.find_all("td", class_="bg-total")[7].text}\n'
    total_vaccinated_people = f'Total vaccinated people: {total_vaccinated()}'

    info_text.insert(1.0, f"\n{all_infected}\n\n {deaths} \n\n {recovered} \n\n {now_ill} \n\n {total_vaccinated_people}")
    info_text['state'] = 'disabled'


    def return_to_first_window():
        root.destroy()
        Start_App.create_general_window()


    return_to_main = Button(root, text='Main',
                            font=('Arial', 14), width=5, height=1, command=return_to_first_window)
    return_to_main.place(x=1, y=2)

    root.mainloop()
