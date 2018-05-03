
import requests
from bs4 import BeautifulSoup

sub = "146000000000" # московская область
raion = "146204000000" # Балашиха
siti =  "set4"# город
street = "Дмитриева"
dom = "26"



def ger_html(htm):
    r = requests.get(htm)
    #print(r.text)
    return r.text


def parse(html):
    soup = BeautifulSoup(html,"html.parser")
    tds = soup.find('select', name_='subject_id')
   # print(soup)
    #print(tb)

def main():
    url = 'https://rosreestr.ru/wps/portal/online_request/'
    parse(ger_html(url))

if __name__ == '__main__':
    main()