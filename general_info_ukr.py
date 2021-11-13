import config_file
from request_module import request

headers = config_file.headers_ukraine
html = request(config_file.url_ukraine, headers)
period_of_time = html.find("table", class_="line").find("caption").text
all_infected = html.find("td", class_="bg-grey larger").text
all_deaths = html.find_all("td", class_="bg-grey")[3].text
all_recovered = html.find_all("td", class_="bg-grey")[5].text
all_now_ill = html.find_all("td", class_="bg-grey")[7].text


def general_data_ukr(all_infected_people=None, deaths=None,
                     recovered=None, now_ill=None):
    time_period = f' {period_of_time}\n'
    all_infected_people = f'Всього захворіло: {all_infected_people}\n'
    deaths = f'Померло: {deaths}\n'
    recovered = f'Вилікувались: {recovered}\n'
    now_ill = f'Продовжують хворіти: {now_ill}\n'
    # send information to tkinter
    print(time_period, all_infected_people, deaths, recovered, now_ill)


if __name__ == "__main__":
    general_data_ukr(all_infected,all_deaths,all_recovered,all_now_ill)
