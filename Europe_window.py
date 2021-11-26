from subprocess import call

from countrygroups import EUROPEAN_UNION as EU_country
from tkinter import *
import tkinter.ttk
from covid.api import CovId19Data
from get_vaccinated_by_countries_EU import vaccinated
import config_file

api = CovId19Data(force=True)

new_list = []
sorted_dic = {}
top_10_europe = []
top_number = 0
api_all = api.get_all_records_by_country()

# get only europe country
for elem in api_all:
    if api_all[elem]['label'] in EU_country.names:
        new_list.append(api_all[elem]["confirmed"])

# sorted list and get top-10
while top_number < 10:
    new_list.sort(reverse=True)
    for elem in api_all:
        if new_list[top_number] in api_all[elem].values():
            sorted_dic[elem] = api_all[elem]
    top_number += 1


# dictionry of top-10 sorted country
def country_from_sorted_list():
    for country in sorted_dic:
        top_10_europe.append(sorted_dic[country]["label"])
    return top_10_europe


top_10 = country_from_sorted_list()

Europe_window = Tk()
Europe_window.geometry(config_file.first_window_size)
Europe_window.title('Covid-19 information')
Europe_window.iconbitmap('icon.ico')
Europe_window.resizable(width=False, height=False)


canvas_width = 1005
canvas_height = 1000
canvas = Canvas(Europe_window,
                width=canvas_width,
                height=canvas_height)

photo = PhotoImage(file='second_win_image.png')
canvas.create_image(370, 200, image=photo)
canvas.create_text(130, 80, text="Select a country:", fill="White",
                   font=('Arial', 23))

canvas.pack()

def show_result(event):
    Field_Europe.delete(1.0, END)
    get_combobox_country = Combobox_Europe_second_window.get()
    if get_combobox_country in top_10:
        last_updated = sorted_dic[get_combobox_country.lower()]["last_updated"]
        confirmed = sorted_dic[get_combobox_country.lower()]["confirmed"]
        label = sorted_dic[get_combobox_country.lower()]["label"]
        recovered = sorted_dic[get_combobox_country.lower()]["recovered"]
        deaths = sorted_dic[get_combobox_country.lower()]["deaths"]
        total_vaccinated = vaccinated(label)
        Field_Europe.insert(1.0, (f'Country: {label}\n'
                                  f'Last updated: {last_updated}\n \n'
                                  f'Confirmed: {confirmed}\n'
                                  
                                  f'Recovered: {recovered}\n'
                                  f'Deaths: {deaths}\n \n'
                                  f'Total vaccinated: {total_vaccinated}\n'))

        # Field_Europe['state'] = 'disabled'
        if '<<ComboboxSelected>>':
            Field_Europe.delete(1.0, END)
            get_combobox_second = Combobox_Europe_second_window.get()

            label_second = sorted_dic[get_combobox_second.lower()]["label"]
            last_updated_second = sorted_dic[get_combobox_second.lower()]["last_updated"]

            confirmed_second = sorted_dic[get_combobox_second.lower()]["confirmed"]
            recovered_second = sorted_dic[get_combobox_second.lower()]["recovered"]
            deaths_second = sorted_dic[get_combobox_second.lower()]["deaths"]
            total_vaccinated_second = vaccinated(label_second)

            Field_Europe.insert(1.0, (f'Country: {label_second}\n'
                                      f'Last updated: {last_updated_second}\n \n'
                                      f'Confirmed: {confirmed_second}\n'

                                      f'Recovered: {recovered_second}\n'
                                      f'Deaths: {deaths_second}\n \n'
                                      f'Total vaccinated: {total_vaccinated_second}\n'))


Combobox_Europe_second_window = tkinter.ttk.Combobox(Europe_window, values=top_10, width=45, height=11,
                                                     state='readonly')
Combobox_Europe_second_window['values'] = top_10
Combobox_Europe_second_window.place(x=14, y=110)
Combobox_Europe_second_window.bind('<<ComboboxSelected>>', show_result)

def Click2():
    Europe_window.destroy()
    call(["python", "Start_App.py"])

Button_Europe_second_window = Button(Europe_window, text='<<',
                                     font=('Arial', 14), width=5, height=1, command=Click2)
Button_Europe_second_window.place(x=1, y=2)

Field_Europe = Text(Europe_window, width=40, height=10, bg='Light gray')
Field_Europe.place(x=360, y=14)


Europe_window.mainloop()
