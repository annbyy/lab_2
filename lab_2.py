import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'accept':'*/*', 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'}
url = 'https://www.gismeteo.ru/diary/4980/2023/10'

request_session = requests.Session()
request = request_session.get(url, headers=headers)

soup = BeautifulSoup(request.content, 'lxml')
table = soup.find('table')

dates = table.find_all('td', {'class':'first'})
temps = table.find_all('td', {'class':'first_in_group positive'})
winds = table.find_all('span')

for i in range(len(dates)):
    print(dates[i].text, temps[i*2].text, winds[i*2].text, temps[i*2+1].text, winds[i*2+1].text)