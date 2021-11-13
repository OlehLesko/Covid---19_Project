import requests
from bs4 import BeautifulSoup as BS
import config_file as conf

headers = conf.headers_asia


def request(url):
    s = requests.Session()
    r = s.get(url=url, headers=headers)
    data = r.text
    soup = BS(data, "lxml")
    parsing_data(soup)


def parsing_data(html):
    all_infected = f' Всього захворіло: {html.find("td", class_="bg-total larger").text}\n'
    deaths = f'Померло: {html.find_all("td", class_="bg-total")[3].text}\n'
    recovered = f'Вилікувались: {html.find_all("td", class_="bg-total")[5].text}\n'
    now_ill = f'Продовжують хворіти: {html.find_all("td", class_="bg-total")[7].text}\n'
    print(all_infected, deaths, recovered, now_ill)


if __name__ == "__main__":
    request(url=conf.url_asia)
