
import requests
from bs4 import BeautifulSoup
import re

num1=[]
params = (
        ('parentId', '146000000000'),
    )
response = requests.get('https://rosreestr.ru/wps/PA_RRORSrviceExtended/Servlet/ChildsRegionController',
                         params=params)
soup1 = BeautifulSoup(response.content, "html.parser")
for a in soup1:
          io = a.replace(' ', '').split()
          #print(io)

for sp in range(len(io)):
    num1.append({'num': re.sub("\D", '', io[sp]), 'dat': re.sub("\d|;", '', io[sp])})

print(num1)





