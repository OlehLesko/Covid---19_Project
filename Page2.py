from tkinter import *
import config


# Creating general window of program
def create_general_window():
    first_window = Tk()
    first_window.geometry(config.first_window_size)
    first_window.title(config.first_window_title)
    first_window['bg'] = config.first_window_background


    #Labels
    Text_first_window = Label(first_window,
                              text='Covid-19',
                              bg='Blue', fg='White',
                              font=('Arial', 35),
                              width=10, height=1)
    Text_first_window.place(x=170, y=110)

    Label_Phone_Number = Label(first_window,
                               text = 'Гаряча лінія: '
                                      '0 800 60 20 19',

                               fg='Black', font=('Arial', 15),
                               width=70, height=1)

    Label_Phone_Number.place(x=0, y=0)



    #Buttons
    Button_Europe_first_window = Button(first_window,
                                        text='Europe',
                                        bg='Black', fg='White',
                                        font=('Arial', 13),
                                        width=17, height=2)
    Button_Europe_first_window.place(x=20, y=220)
    Button_Ukraine_first_window = Button(first_window,
                                         text='Ukraine',
                                         bg='Black', fg='White',
                                         font=('Arial', 13),
                                         width=19, height=2)
    Button_Ukraine_first_window.place(x=212, y=220)
    Button_Asia_first_window = Button(first_window,
                                      text='Asia',
                                      bg='Black', fg='White',
                                      font=('Arial', 13),
                                      width=17, height=2)
    Button_Asia_first_window.place(x=420, y=220)

    first_window.mainloop()


if __name__ == "__main__":
    create_general_window()
