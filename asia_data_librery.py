import covid19cases as covid

sorted_data = {}


def data_request():
    asia_data = covid.get_continent_cases("Asia")
    sorted_data['Total Cases'] = asia_data['TotalCases']
    sorted_data['Total Deaths'] = asia_data['TotalDeaths']
    sorted_data['Total Recovered'] = asia_data['TotalRecovered']
    sorted_data['Active Cases'] = asia_data['ActiveCases']
    sorted_data['Continent'] = asia_data['Continent']
    sorted_data['Last  Updated'] = asia_data['LastUpdated']
    return sorted_data


if __name__ == "__main__":
    result = data_request()
    for key in result:
        print(f'{key}: {result[key]}')
