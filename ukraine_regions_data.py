import config_file
from request_module import request
from general_info_ukr import general_data_ukr
from get_vactinated_by_ukr_region import total_vaccinated_region_ukr

headers = config_file.headers_ukraine
html = request(config_file.url_ukraine, headers)
list_region = []


# get list of Ukraine region
def get_region_list():
    region_of_ukraine = html.find("div", class_="compact-table expand-table").find("table").find_all("tr")
    for element in region_of_ukraine[1:-1]:
        print(element.find("a").text)
        list_region.append(element.find("a").text)
    return list_region


# get data from each region of Ukraine
def region_data_ukr():
    input_text = input("Enter text:")
    all_info = html.find_all('table')[1].find_all('td')
    for i in all_info:
        if i.string == input_text:
            all_infected = i.parent.find("td", class_="blank larger").text
            all_deaths = i.parent.find_all("td", class_="blank")[2].text
            all_recovered = i.parent.find_all("td", class_="blank")[4].text
            all_now_ill = i.parent.find_all("td", class_="blank")[6].text
            total_vaccinated = total_vaccinated_region_ukr(i.string)
            general_data_ukr(all_infected, all_deaths, all_recovered, all_now_ill, total_vaccinated)


if __name__ == "__main__":
    region_list_all = get_region_list()
    region_data_ukr()
    print(region_list_all)
    print(region_list_all[2])
