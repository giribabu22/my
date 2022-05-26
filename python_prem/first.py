from bs4 import BeautifulSoup
import requests

with open('ew.html') as  f:
  soup=BeautifulSoup(f,'lxml')

res=soup.find('div',class_='m')
print(res)