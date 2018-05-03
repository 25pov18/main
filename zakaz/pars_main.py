import requests
from bs4 import BeautifulSoup
import math
import re

cookies1 = {
    '__utmz': '224553113.1522510920.6.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'JSESSIONID_8': '0000wXG2p8QDByr_wFOV3SPWvu0:19a92ngnb',
    '__utma': '224553113.898432000.1522485708.1522522790.1522562659.8',
    '__utmc': '224553113',
    '_ym_uid': '1522562659405127688',
    '_ym_isad': '2',
    '_ym_visorc_18809125': 'w',
    '__utmt': '1',
    '__utmb': '224553113.28.9.1522564172432',
}
headers1 = {
    'Origin': 'https://rosreestr.ru',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://rosreestr.ru/wps/portal/p/cc_ib_portal_services/online_request/!ut/p/z1/pZBLD4IwEIR_iwfPu8tD9NioQYPxBSrtpWlIgyRQEFH_vtS7cnBvm5lvZ7IgIAVh1LPIVVfURpX9zsVEhgdvSXOPovBAAbI1i8ilEDHx4fLTsCMQ__C9wfL4ZRj2vPgZMXcGDLbiUAjvSwYSacWIeU60WyQzZEcXz5ut4yASxPZGVpuurctSt8DHGGvVZleW2UdatTZlYbRs9e2h7528f2TZqFwD96GpTikW-6qavkZvrGQl5w!!/p0/IZ7_01HA1A42KODT90AR30VLN22001=CZ6_GQ4E1C41KGQ170AIAK131G00T5=MEcontroller!QCPSearchAction==/?online_request_search_page=3',
    'Connection': 'keep-alive',
}

# data1 = [
#     ('search_action', 'true'),
#     ('subject', ''),
#     ('region', ''),
#     ('settlement', '146204501000'),
#     ('cad_num', ''),
#     ('start_position', '59'),
#     ('obj_num', ''),
#     ('old_number', ''),
#     ('search_type', 'ADDRESS'),
#     ('subject_id', '146000000000'),
#     ('region_id', '146204000000'),
#     ('settlement_type', 'set4'),
#     ('settlement_id', '146204501000'),
#     ('street_type', 'str1'),
#     ('street', 'Дмитриева'),
#     ('house', '24'),
#     ('building', ''),
#     ('structure', ''),
#     ('apartment', ''),
#     ('right_reg', ''),
#     ('encumbrance_reg', ''),
#
# ]



list = []
def print_links(soup,url1):

    rows = soup.select('[id^="js_oTr"]')
    for kil, row in enumerate(rows):
        link = row.find('a').get('href')
        street = row.find('a').text
        number1 = row.findAll('td')[1].text
        number2 = row.findAll('td')[2].text
        #print(number1)
        link_url = url1.url+link.replace('®', '&reg')
        #print(link_url)
        #------------------------------ переход в нутрь---------
        r = requests.post(link_url)
        soup1 = BeautifulSoup(r.text, "html.parser")
        try:
            p = soup1.findAll('b')[4].text                       # площадь
        except:
            p = "нет"
        try:
             pravo = soup1.select("#r_enc td")[3].text           # прво
        except:
             pravo = "нет права"
        try:
            tip = soup1.findAll('b')[11].text                  # назначение
        except:
            tip = " отсутствуе"
        kil+=1
        #print("страница #",total, "итерация # ", kil, tip, pravo, p)
        kadastr = re.sub("^\s+|\n|\r|\s+$", '', number1)
        usl_nom = re.sub("^\s+|\n|\r|\s+$", '', number2)
        v3 = re.sub("^\s+|\n|\r|\s+$", '', p)
        pravo1 = re.sub("^\s+|\n|\t|\r|\xa0|\s+$", '', pravo).replace(' ', '')
        naz = re.sub("^\s+|\n|\r|\s+$", '', tip)

        list.append({'kadastr': kadastr, 'usl_nom': usl_nom, 'v3':v3, 'pravo':pravo1, 'naz':naz})



        print(number1)
    return list

def get_total_pages(data,headers,cookies):

    url = 'https://rosreestr.ru/wps/portal/p/cc_ib_portal_services/online_request/!ut/p/z1/pZDBDoJADES_xYPntoCix40aNBgRQYW9bDZkgySwIKD-vqx38WBvzczrTAocEuBaPotc9kWtZTnsKZ8LL3Q2tHLI90Jyke2YTzZ5iPEMrqOGgID_ww8Gw-OXYTjwfDRiZf0wmIq_QtKhpCuQtoyYY_nBOl4iO9l42R8sC5EgMjeyWvdtXZaqhXSKkZJtdmOZeaRRa10WWolW3R-q60X3kUUjcwWpDU11TrA4VtXiNXkDGi_nHw!!/p0/IZ7_01HA1A42KODT90AR30VLN22001=CZ6_GQ4E1C41KGQ170AIAK131G00T5=MEcontroller!QCPSearchAction==/'

    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    soup1 = BeautifulSoup(response.text, "html.parser")
    ob = soup1.select("#pg_stats b")[0]
    kol = re.sub("^\s+|\n|\t|\r|\xa0|\s+$", '',  ob.text).replace(' ', '')


    link =  math.ceil(int(ob.text)/20)# количество страниц
    print("количество страниц",link)
    print('всего найдено объектов', kol)
    for inde in range(1,int(link)+1):  # сколько страниц

      print(inde, "страница")
      params = (('online_request_search_page', inde),)
      response1 = requests.post(url, headers=headers, cookies=cookies, data=data, params=params)
      soup = BeautifulSoup(response1.text, "html.parser")
      a1 =  print_links(soup,response)



    return [kol,a1]


def main(data1):
    list1=[]
    list.clear()
    #print(data1)
    k1 = get_total_pages(data1, headers1, cookies1)

    print()
    #print(k1)
    #k=0
    # for s1, s in  enumerate(list, 1):
    #     k+=1
    #     #print(s1, s)
    #     list1.append(s)

    return k1

    # if  int(k1) == int(k):
    #     print("======= УСПЕШНО ======")
    # else:
    #     print("ошибка  !!!! записей № ",k1,  "внесено ",k)
    #

# if __name__ == '__main__':
#     main()

