import config_file
from request_module import request
from get_general_vaccinated_data_asia import total_vaccinated

headers = config_file.headers_asia
html = request(config_file.url_asia, headers)


# general data for Asia
def general_information():
    all_infected = f' Infected: {html.find("td", class_="bg-total larger").text}\n'
    deaths = f'Deaths: {html.find_all("td", class_="bg-total")[3].text}\n'
    recovered = f'Recovered: {html.find_all("td", class_="bg-total")[5].text}\n'
    now_ill = f'Now ill: {html.find_all("td", class_="bg-total")[7].text}\n'
    total_vaccinated_people = f'Total vaccinated people: {total_vaccinated()}'
    print(all_infected, deaths, recovered, now_ill, total_vaccinated_people)


if __name__ == "__main__":
    general_information()
