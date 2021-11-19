from countrygroups import EUROPEAN_UNION as EU_country
from tkinter import *
import tkinter.ttk
from covid.api import CovId19Data
from get_vaccinated_by_countries_EU import vaccinated

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

second_window = Tk()
second_window.geometry('700x450')
second_window.title('Covid-19 information')
second_window['bg'] = 'Blue'
second_window.resizable(width=False, height=False)


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
        Field_Europe.insert(1.0, (f'Last_updated: {last_updated}\n'
                                  f'Confirmed: {confirmed}\n'
                                  f'Country: {label}\n'
                                  f'Recovered: {recovered}\n'
                                  f'Deaths: {deaths}\n'
                                  f'Total vaccinated: {total_vaccinated}\n'))


Text_Europe = Label(second_window, text='Top-10 країн Європи', font=('Arial', 23), bg='Blue', fg='White')
Text_Europe.place(x=10, y=60)
Combobox_Europe_second_window = tkinter.ttk.Combobox(second_window, values=top_10, width=45, height=11,
                                                     state='readonly')
Combobox_Europe_second_window['values'] = top_10
Combobox_Europe_second_window.place(x=14, y=110)
Button_Europe_second_window = Button(second_window, text='Home', font=('Arial', 14), width=7, height=1)
Button_Europe_second_window.place(x=5, y=2)
Field_Europe = Text(second_window, width=40, height=10)
Field_Europe.place(x=360, y=14)
Combobox_Europe_second_window.bind('<<ComboboxSelected>>', show_result)

second_window.mainloop()
