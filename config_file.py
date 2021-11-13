# We can use this file for setting different parameters
# We can write some changes and it will influence on our project
first_window_size = '600x400'
first_window_title = 'Covid-19'
first_window_background = 'Blue'

# Asia
headers_asia = {'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

url_asia = 'https://index.minfin.com.ua/ua/reference/coronavirus/geography/asia/'
# Ukraine
headers_ukraine = {'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

url_ukraine = 'https://index.minfin.com.ua/ua/reference/coronavirus/geography/asia/'
#
# def request(url):
#     s = requests.Session()
#     if url == url_ukraine:
#         r = s.get(url=url, headers=headers_ukraine)
#         check_status(r)
#     else:
#         r=s.get(url=url,headers=headers_asia)
#         check_status(r)
#
# def check_status(r):
#     if r.status_code == 200:
#         data = r.text
#         soup = BS(data,"lxml")
#         if url == url_ukraine:
#             pass
#         else:
#             pd_asia(soup)
#     else:
#         print('Error')
# def parsing_data(html):
#     all_infected = f' Всього захворіло: {html.find("td",class_="bg-total larger").text}\n'
#     deaths = f'Померло: {html.find_all("td", class_="bg-total")[3].text}\n'
#     recovered = f'Вилікувались: {html.find_all("td", class_="bg-total")[5].text}\n'
#     now_ill = f'Продовжують хворіти: {html.find_all("td", class_="bg-total")[7].text}\n'
#     print (all_infected, deaths, recovered, now_ill)







#
# if __name__ == "__main__":
#     request(url='https://index.minfin.com.ua/ua/reference/coronavirus/geography/asia/')


