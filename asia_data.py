import config_file
from request_module import request

headers = config_file.headers_asia
html = request(config_file.url_asia, headers)


def parsing_data():
    all_infected = f' Всього захворіло: {html.find("td", class_="bg-total larger").text}\n'
    deaths = f'Померло: {html.find_all("td", class_="bg-total")[3].text}\n'
    recovered = f'Вилікувались: {html.find_all("td", class_="bg-total")[5].text}\n'
    now_ill = f'Продовжують хворіти: {html.find_all("td", class_="bg-total")[7].text}\n'
    print(all_infected, deaths, recovered, now_ill)


if __name__ == "__main__":
    parsing_data()
