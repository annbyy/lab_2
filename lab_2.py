import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

headers = {'accept':'*/*', 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'}
url = 'https://www.gismeteo.ru/diary/4980/2023/10'

request_session = requests.Session()
request = request_session.get(url, headers=headers)

soup = BeautifulSoup(request.content, 'lxml')
table = soup.find('table')
data = table.find_all('td')
count = table.find_all('tr')

data_header = ["Число", "Температура", "Давление", "Ветер"]
data_rows = []

for i in range(len(count)-2):
    data_rows.append(["{} октября".format(data[i*11].text), "{}°С".format(data[i*11+1].text), "{}мм рт ст".format(data[i*11+2].text), "ветер {}".format(data[i*11+5].text)])

filename = 'Weather_Data.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(data_header)
    csvwriter.writerows(data_rows)
file.close()