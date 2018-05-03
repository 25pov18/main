import requests
import lxml
from bs4 import BeautifulSoup
url1 = 'https://rosreestr.ru/wps/portal/online_request'
#response = requests.get(url1)

#print(response.content)

url = requests.get(url1)
soup = BeautifulSoup(url.content,"lxml")
timers = soup.find_all('td' and 'a')
#h = timers

for timer in timers:
    link = timer.get('href')
    print(link)
