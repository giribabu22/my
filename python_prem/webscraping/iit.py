'''import requests
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
url='https://www.vedantu.com/iit-jee/'
ch=int(input('enter :'))
res=li[ch-1]
s=url+f'/{res}'
sl=s.replace(' ','-').lower()
page2=requests.get(sl)
soup=soupUse(page2.content,'lxml') 
l=soup.find_all('tbody')[0:3]
for ele in  l:
  print()
  print(ele.text)
  print('__________________________ ')'''
  