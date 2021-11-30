import config_file
from get_vactinated_by_ukr_region import total_vaccinated_region_ukr
from ukraine_regions_data import get_region_list
# from Europe_window import Europe_function
import Start_App

# import request module
from request_module import request

# import translator and transliterated
from deep_translator import GoogleTranslator
from translitua import translit

# import tkinter
from tkinter import *
import tkinter.ttk
from subprocess import call

def Ukraine_function():
    # use it for request
    headers = config_file.headers_ukraine
    html = request(config_file.url_ukraine, headers)

    # translate ukrainian region in english transliteration
    translate_elements = []
    ukraine_regions = get_region_list()
    for element in ukraine_regions:
        translate_elements.append(translit(element))

    # create tkinter window of Ukraine
    Ukraine_window = Tk()
    Ukraine_window.geometry(config_file.first_window_size)
    Ukraine_window.title('Covid-19 information')
    Ukraine_window.iconbitmap('Images/icon.ico')
    Ukraine_window.resizable(width=False, height=False)

    # create canvas window
    canvas = Canvas(Ukraine_window,
                    width=config_file.canvas_width,
                    height=config_file.canvas_height)
    photo = PhotoImage(file='Images/Imagecovid .png')

    # transparent text_1
    canvas.create_image(370, 200, image=photo)
    canvas.create_text(130, 90, text="Region of Ukraine:", fill="White",
                       font=('Arial', 20))

    # transparent text_2 about current statistic date translated to English
    period_of_time = html.find("table", class_="line").find("caption").text
    period_of_time = GoogleTranslator(source='auto', target='en').translate(period_of_time)
    canvas.create_text(400, 30, fill="black",
                       font=('Arial', 14))
    canvas.pack()


    # show result in the text field about selected region
    def show_result(event):
        Field_Ukraine.delete(1.0, END)
        selected_region = Combobox_Ukraine_second_window.get()
        selected_region = ukraine_regions[translate_elements.index(selected_region)]
        all_info = html.find_all('table')[1].find_all('td')

        # looking for and get information about selected region
        for i in all_info:
            if i.string == selected_region:
                times = period_of_time
                all_infected = i.parent.find("td", class_="blank larger").text
                all_deaths = i.parent.find_all("td", class_="blank")[2].text
                all_recovered = i.parent.find_all("td", class_="blank")[4].text
                all_now_ill = i.parent.find_all("td", class_="blank")[6].text
                total_vaccinated = total_vaccinated_region_ukr(i.string)

                Field_Ukraine.insert(1.0, (
                    f'{times}\n'
                    f'\nConfirmed: {all_infected}\n'
                    f'\nRecovered: {all_recovered}\n'
                    f'\nDeaths: {all_deaths}\n'
                    f'\nNow ill: {all_now_ill}\n'
                    f'\nTotal vaccinated: {total_vaccinated}\n'))


    Combobox_Ukraine_second_window = tkinter.ttk.Combobox(Ukraine_window, values=ukraine_regions, width=45, height=11,
                                                          state='readonly')

    Combobox_Ukraine_second_window['values'] = translate_elements
    Combobox_Ukraine_second_window.place(x=14, y=110)
    Combobox_Ukraine_second_window.bind('<<ComboboxSelected>>', show_result)


    # back to the main window
    def return_to_first_window():
        Ukraine_window.destroy()
        Start_App.create_general_window()


    return_to_main = Button(Ukraine_window, text='Main',
                            font=('Arial', 14), width=5, height=1, command=return_to_first_window)
    return_to_main.place(x=1, y=2)

    Field_Ukraine = Text(Ukraine_window, width=36, height=12, bg='Light gray')
    Field_Ukraine.place(x=400, y=90)

    Ukraine_window.mainloop()
