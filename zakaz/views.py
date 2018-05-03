from django.shortcuts import render,get_object_or_404
from zakaz.models import zakaz, adres
import requests
from bs4 import BeautifulSoup
from .pars_main import main
import re
import math





def index(request):
    list = []
    url = 'https://rosreestr.ru/wps/portal/online_request'
    response = requests.post(url)
    soup1 = BeautifulSoup(response.text, "html.parser")
    adres = soup1.select("#subjectId  option")
    for a in adres:
        dat = a.text
        num = a.get('value')
        list.append({'num':num,'dat': dat})
    return render(request,'index.html',{'name': list} )


def show(request): # обработка запроса данных


    print(request.method)
    if request.method == "POST":

        data = [
            ('search_action', 'true'),
            ('subject', ''),
            ('region', ''),
            ('settlement', '146204501000'),
            ('cad_num', ''),
            ('start_position', '59'),
            ('obj_num', ''),
            ('old_number', ''),
            ('search_type', 'ADDRESS'),
            ('subject_id', request.POST.get('subject_id', '')),
            ('region_id', request.POST.get('region_id', '')),
            ('settlement_type', 'set4'),
            ('settlement_id', request.POST.get('settlement_id', '')),
            ('street_type', 'str1'),
            ('street', request.POST.get('street', '')),
            ('house', request.POST.get('house', '')),
            ('building', ''),
            ('structure', ''),
            ('apartment', ''),
            ('right_reg', ''),
            ('encumbrance_reg', ''),
        ]


        rol, numk = main(data)

        print("sdfgsdfg",rol)
        print("sdfgsdfg", numk)
    else:
        return credits('/')

    return render(request,'homPage.html',{'kad': numk,"kol": rol, "adres":request.POST.get('street', '')+"_"+request.POST.get('house', '') })

def zaksz1(request): # запись в базу
    num = []
    zob =0
    if request.method == "POST":
        a = request.POST
        for y in a:
            if y !="csrfmiddlewaretoken" and y !="adres" and  y !="vsego_ob":
                num.append(request.POST.get(y, ''))
                zob+=1
            if y =="adres":
                 adres =  request.POST.get(y, '')
            if y =="vsego_ob":
                      vsego =request.POST.get(y, '')


        print(adres,vsego,zob)# адресс/ общее количество/ выделено номеров





    else:

        return credits('/')

    return render(request,'zakaz.html', {'kol':num})

def reg(request): # парсер региона просто звебался
    num1 =[]
    if request.method == "POST":
       reg = request.POST.get('reg', '')

       params = (
           ('parentId', reg),
       )
       response = requests.get('https://rosreestr.ru/wps/PA_RRORSrviceExtended/Servlet/ChildsRegionController',
                               params=params)
       soup1 = BeautifulSoup(response.content, "html.parser")
       for a in soup1:
           io = a.replace(' ', '').split()
           # print(io)
       for sp in range(len(io)):
           num1.append({'num': re.sub("\D", '', io[sp]), 'dat': re.sub("\d|;", '', io[sp])})
    return render(request, 'reg.html',{'val':num1,'reg':reg } )

def siti(request):



    return render(request, 'siti.html')