import config_file
from request_module import request
from general_info_ukr import general_data_ukr

headers = config_file.headers_ukraine


def region_data_ukr():
    input_text = input("Enter text:")
    html = request(config_file.url_ukraine, headers)
    all_info = html.find_all('table')[1].find_all('td')
    for i in all_info:
        if i.string == input_text:
            all_infected = i.parent.find("td", class_="blank larger").text
            all_deaths = i.parent.find_all("td", class_="blank")[2].text
            all_recovered = i.parent.find_all("td", class_="blank")[4].text
            all_now_ill = i.parent.find_all("td", class_="blank")[6].text
            general_data_ukr(all_infected, all_deaths, all_recovered, all_now_ill)


if __name__ == "__main__":
    region_data_ukr()
