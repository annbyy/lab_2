import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'accept':'*/*', 'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'}
url = 'https://www.gismeteo.ru/diary/4976/2023/9'

request_session = requests.Session()
request = request_session.get(url, headers=headers)

soup = BeautifulSoup(request.content, 'lxml')
table = soup.find('table')
