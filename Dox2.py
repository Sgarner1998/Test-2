from bs4 import BeautifulSoup
import requests

url2 = 'https://tools.keycdn.com/geo'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}

page2 = requests.get(url2, headers=headers)
soup2 = BeautifulSoup(page2.text, 'html.parser')

IP =  soup2.find(string='IP address').find_next('dd').text
ZIP = soup2.find(string='Postal code').find_next('dd').text
CITY = soup2.find(string='City').find_next('dd').text


url = 'https://www.google.com/search?q=' + CITY + 'weather'

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

temp = soup.find('span', id='wob_tm').text
unit = soup.find('div', class_='vk_bk wob-unit').find('span', class_='wob_t').text
wind = soup.find('span', id='wob_ws').text

print('Your IP Address: ' + IP + '\n' + 'Zip Code: ' + ZIP + '\n' + 'Current Temperature: ' + temp + unit + '\n' + 'Wind Speed: ' + wind)

