import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'accept':'*/*', 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'}
url = 'https://www.gismeteo.ru/diary/4980/2023/10'

request_session = requests.Session()
request = request_session.get(url, headers=headers)

soup = BeautifulSoup(request.content, 'lxml')
table = soup.find('table')
data = table.find_all('td')
count = table.find_all('tr')


for i in range(len(count)-2):
    print("{} октября: день - {}°С, {}мм рт ст, ветер {}; вечер - {}°С, {}мм рт ст, ветер {};".format(data[i*11].text, data[i*11+1].text, data[i*11+2].text, data[i*11+5].text, data[i*11+6].text, data[i*11+7].text, data[i*11+10].text))