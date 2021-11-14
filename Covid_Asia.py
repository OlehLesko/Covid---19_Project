import covid19cases as covid
import openpyxl

api = covid.get_global_cases()
Asia = covid.get_continent_cases("Asia")
print(Asia)

book = openpyxl.Workbook()
Excel_file = book.active

A1 = Excel_file['A1'] = u'Інформація по Азії'
A1.encode('cp1125')
A2 = Excel_file['A2'] = u'Всього випадків'
A2.encode('cp1125')
A3 = Excel_file['A3'] = u'Загальна кількість смертей'
A3.encode('cp1125')
A4 = Excel_file['A4'] = u'Число одуживших'
A4.encode('cp1125')

B1 = Excel_file['B1'] = covid.get_continent_cases("Asia")['TotalCases']
B2 = Excel_file['B2'] = covid.get_continent_cases("Asia")['TotalDeaths']
B3 = Excel_file['B3'] = covid.get_continent_cases("Asia")['TotalRecovered']

print(
    f'{A1}  \n{A2} — {B1}  \n{A3} — {B2}  \n{A4} — {B3}')

book.save("Europe_book.xlsx")
book.close()
