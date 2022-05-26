'''#preview-table-text-editor
"""import requests

import  requests
from bs4 import BeautifulSoup as soupUse
url='https://www.vedantu.com/iit-jee/iit-roorkee'
data=requests.get(url)
soup=soupUse(data.text,'html.parser')
res=soup.find('div',class_="review-table-text-editor")
print(res)"""
import requests
from bs4 import BeautifulSoup as soupUse

url='https://www.vedantu.com/iit-jee/iit-colleges-in-india'
data=requests.get(url)
soup=soupUse(data.text,'html.parser')
res=soup.find_all('div',class_="PageListModulesmain_linksWrapper__3CpAQ")
li,c=[],1
for ele in  res:
  print(c,ele.a.text)
  li.append(ele.a.text)
  c+=1
ch=int(input('enter :'))
url='https://www.vedantu.com/iit-jee'

res=li[ch-1]
s=url+f'/{res}'
sl=s.replace(' ','-')
print(sl.lower())
page2=requests.get(sl)
soup=soupUse(page2.content,'lxml')
#print(soup.find_all('div'))
dat=soup.find('div',class_="topicPage_leftSection__2WOwK")
print(dat)'''
'''
import json
import requests
from bs4 import BeautifulSoup as soupUse

li,c=[],1
url='https://www.vedantu.com/iit-jee'
with  open('clg.json')  as  g:
  res=json.load(g)
for ele in  res:
  print(c,ele)
  li.append(ele)
  c+=1
url='https://www.vedantu.com/iit-jee/'
ch=int(input('enter :'))
res=li[ch-1]
s=url+f'/{res}'
sl=s.replace(' ','-').lower()
page2=requests.get(sl)
soup=soupUse(page2.content,'lxml') 
l=soup.find_all('tbody')[0:3]
for ele in  l:
  print(ele.text)'''
'''[
   "IIT Delhi",
   "IIT Guwahati",
   "IIT Roorkee",
   "IIT Ropar",
   "IIT Hyderabad",
   "IIT Goa",
   "IIT Dharwad",
   "IIT Bhubaneswar",
   "IIT Gandhinagar",
   "IIT Jodhpur",
   "IIT Patna",
   "IIT Mandi",
   "IIT Varanasi (BHU)",
   "IIT Tirupati",
   "IIT Dhanbad (ISM)",
   "IIT Bhilai",
   "IIT Kharagpur",
   "IIT Madras",
   "IIT Kanpur",
   "IIT Indore",
   "IIT Palakkad",
   "IIT Bombay"
]'''

li=[{'pre':44},{'giri':54}]
print(li[1].update({'num':2}))
print(li)
