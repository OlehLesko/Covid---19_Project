import config_file
from tkinter import *
import tkinter.ttk
from covid.api import CovId19Data
from get_vaccinated_by_countries_EU import vaccinated



api = CovId19Data(force=True)

Country_Europea_Top10 = ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'Romania', 'Netherlands', 'Belgium', 'Greece',
                         'Portugal']

second_window = Tk()
second_window.geometry(config_file.first_window_size)
second_window.title('Europe')
second_window.iconbitmap('Coronavirus-300x300.ico')
second_window.resizable(width=False, height=False)


canvas_width = 1005
canvas_height = 1000
canvas = Canvas(second_window,
                width=canvas_width,
                height=canvas_height)

photo = PhotoImage(file='Imagecovid (1).png')
canvas.create_image(370, 200, image=photo)
canvas.create_text(130, 80, text="Select a country:", fill="White",
                   font=('Arial', 23))

canvas.pack()


def insert_Text_Europe(event):
    Get = Combobox_Europe_second_window.get()
    ListInsert_libery_inText = api.filter_by_country(Get)

    B1 = api.filter_by_country(Get)['label']
    B2 = api.filter_by_country(Get)['last_updated']
    B3 = api.filter_by_country(Get)['confirmed']
    B4 = api.filter_by_country(Get)['lat']
    B5 = api.filter_by_country(Get)['long']
    B6 = api.filter_by_country(Get)['recovered']
    B7 = api.filter_by_country(Get)['deaths']

    Getstr1 = Field_Europe.insert(1.0, (
        f'Country: {B1} \nlast update : {B2[:10]}  \n  \nConfirmed : {B3}  '
        f'\nlat : {B4}  \nlong : {B5}  \nRecovered : {B6}  \nDeaths : {B7} '))


    Field_Europe['state'] = 'disabled'


Combobox_Europe_second_window = tkinter.ttk.Combobox(second_window,
                                                     values=Country_Europea_Top10, width=35,
                                                     height=15,state='readonly')

Combobox_Europe_second_window['values'] = Country_Europea_Top10
Combobox_Europe_second_window.place(x=14, y=105)
Combobox_Europe_second_window.bind('<<ComboboxSelected>>', insert_Text_Europe)


Button_Europe_second_window = Button(second_window, text='<<',
                                     font=('Arial', 14), width=5, height=1)
Button_Europe_second_window.place(x=1, y=2)

Field_Europe = Text(second_window, width=40, height=10, bg='Light gray')
Field_Europe.place(x=360, y=14)




second_window.mainloop()
