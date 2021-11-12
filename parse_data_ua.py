import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36 '
}
all_covid_info_ukr = []


# request to url
def request(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    get_region_list(soup)
    region_value(soup)
    get_sorting_value(soup)
    get_data(soup)


# get the list of region in Ukraine
def get_region_list(html_text):
    region_of_ukraine = html_text.find("div", class_="compact-table expand-table").find("table").find_all("tr")
    for element in region_of_ukraine[1:-1]:
        print(element.find("a").text)


# get the value "Регіон" from table of information
def region_value(html_text):
    region = html_text.find("span", class_="sortspan").text
    print(region)


# get the values "Всього інфіковано, Смертельні випадки,
# Видужали, Наразі хворіють"
# from table of information
def get_sorting_value(html_text):
    sort_info = html_text.find_all("a", class_="sorthref arrowright arrow-down")
    # print(sort_info)
    for value in sort_info[0:4]:
        for text in value.stripped_strings:
            print(text)


def get_data(html_text):
    table_body = html_text.find("div", class_="compact-table expand-table")
    rows = table_body.find_all('tr')
    # print(rows)
    for row in rows:
        # print(row)
        cols = row.find_all('td')
        data = [ele.text.strip() for ele in cols]
        all_covid_info_ukr.append(data)
    print(all_covid_info_ukr)


        # for info in cols:
        #     print(info)
            # info.replace('\\xad', '')
        # print(cols)
    #     data.append([ele for ele in cols if ele])  # Get rid of empty values
    # print(table_body)
# replace('\\xad', '')

def get_article_urls(html_text):
    with open('index.html', 'w') as file:
        file.write(response.text)


def main():
    request(url='https://index.minfin.com.ua/ua/reference/coronavirus/ukraine/')


if __name__ == "__main__":
    main()
