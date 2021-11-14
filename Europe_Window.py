import json
from tkinter import *
import tkinter.ttk
from covid.api import CovId19Data
# from google_trans_new import google_translator
import openpyxl
# import codecs

api = CovId19Data(force=True)

Country_Europea_Top10 = ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'Romania', 'Netherlands', 'Belgium', 'Greece',
                         'Portugal']
second_window = Tk()
second_window.geometry('700x450')
second_window.title('Covid-19 information')
second_window['bg'] = 'Blue'
second_window.resizable(width=False, height=False)


def insert_Text_Europe(event):
    Get = Combobox_Europe_second_window.get()
    ListInsert_libery_inText = api.filter_by_country(Get)

    book = openpyxl.Workbook()
    Excel_file = book.active

    A1 = Excel_file['A1'] = u'Країна'
    A1.encode('cp1125')
    A2 = Excel_file['A2'] = u'Останнє оновлення'
    A2.encode('cp1125')
    A3 = Excel_file['A3'] = u'Усього випадків'
    A3.encode('cp1125')
    A4 = Excel_file['A4'] = u'Невідома'
    A4.encode('cp1125')
    A5 = Excel_file['A5'] = u'Невідома'
    A5.encode('cp1125')
    A6 = Excel_file['A6'] = u'Число одуживших'
    A6.encode('cp1125')
    A7 = Excel_file['A7'] = u'Смертність'
    A7.encode('cp1125')

    B1 = Excel_file['B1'] = api.filter_by_country(Get)['label']
    B2 = Excel_file['B2'] = api.filter_by_country(Get)['last_updated']
    B3 = Excel_file['B3'] = api.filter_by_country(Get)['confirmed']
    B4 = Excel_file['B4'] = api.filter_by_country(Get)['lat']
    B5 = Excel_file['B5'] = api.filter_by_country(Get)['long']
    B6 = Excel_file['B6'] = api.filter_by_country(Get)['recovered']
    B7 = Excel_file['B7'] = api.filter_by_country(Get)['deaths']

    Getstr1 = Field_Europe.insert(1.0, (
        f'{A1} — {B1}  \n{A2} — {B2}  \n{A3} — {B3}  \n{A4} — {B4}  \n{A5} — {B5}  \n{A6} — {B6}  \n{A7} — {B7}'))

    book.save("Europe_book.xlsx")
    book.close()


Text_Europe = Label(second_window, text='Top-10 країн Європи', font=('Arial', 23), bg='Blue', fg='White')
Text_Europe.place(x=10, y=60)
Combobox_Europe_second_window = tkinter.ttk.Combobox(second_window, values=Country_Europea_Top10, width=45, height=11,
                                                     state='readonly')
Combobox_Europe_second_window['values'] = Country_Europea_Top10
Combobox_Europe_second_window.place(x=14, y=110)
Button_Europe_second_window = Button(second_window, text='Home', font=('Arial', 14), width=7, height=1)
Button_Europe_second_window.place(x=5, y=2)
Field_Europe = Text(second_window, width=40, height=10)
Field_Europe.place(x=360, y=14)
Combobox_Europe_second_window.bind('<<ComboboxSelected>>', insert_Text_Europe)

second_window.mainloop()
