import config_file
from request_module import request
from tkinter import *
import tkinter.ttk

headers = config_file.headers_ukraine
html = request(config_file.url_ukraine, headers)

# general information about coronavirus in Ukraine
period_of_time = html.find("table", class_="line").find("caption").text
all_infected = html.find("td", class_="bg-grey larger").text
all_deaths = html.find_all("td", class_="bg-grey")[3].text
all_recovered = html.find_all("td", class_="bg-grey")[5].text
all_now_ill = html.find_all("td", class_="bg-grey")[7].text



# show information
def general_data_ukr(all_infected_people=None, deaths=None,
                     recovered=None, now_ill=None, total_vaccinated=None):

    time_period = f' {period_of_time}\n'
    all_infected_people = f'Infected: {all_infected_people}\n'
    deaths = f'Deaths: {deaths}\n'
    recovered = f'Recovered: {recovered}\n'
    now_ill = f'Now ill: {now_ill}\n'
    total_vaccinated_region_ukr = f'Total vaccinated people: {total_vaccinated}\n'
    # send information to tkinter
    print(time_period, all_infected_people, deaths, recovered, now_ill,total_vaccinated_region_ukr)
    Field_Ukraine.insert(1.0,())


#Crete Window_Ukraine
Window_Ukraine = Tk()
Window_Ukraine.geometry(config_file.first_window_size)
Window_Ukraine.title('Ukraine')
Window_Ukraine.iconbitmap('Coronavirus-300x300.ico')
Window_Ukraine.resizable(width=False, height=False)

canvas_width = 1005
canvas_height = 1000
canvas = Canvas(Window_Ukraine,
                width=canvas_width,
                height=canvas_height)

photo = PhotoImage(file='Imagecovid (1).png')
canvas.create_image(370, 200, image=photo)
canvas.create_text(150, 100, text=("Select\nthe region of Ukraine:"), fill="White",
                   font=('Arial', 23))

canvas.pack()

#Combobox
Combobox_Ukraine_second_window = tkinter.ttk.Combobox(Window_Ukraine, width=20,
                                                      height=20,state='readonly')
# Combobox_Ukraine_second_window['values'] = top_10
Combobox_Ukraine_second_window.place(x=14, y=140)
Combobox_Ukraine_second_window.bind('<<ComboboxSelected>>', general_data_ukr)

#Button_Back_First_window
Button_Ukraine_second_window = Button(Window_Ukraine, text='<<',
                                     font=('Arial', 14), width=5, height=1)
Button_Ukraine_second_window.place(x=1, y=2)

Field_Ukraine = Text(Window_Ukraine, width=40, height=10, bg='Light gray')
Field_Ukraine.place(x=360, y=14)


if __name__ == "__main__":
    general_data_ukr(all_infected,all_deaths,all_recovered,all_now_ill)

Window_Ukraine.mainloop()
