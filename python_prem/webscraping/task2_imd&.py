import requests
from bs4 import BeautifulSoup as soupUse 

def year_movie():
  page=requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
  soup=soupUse(page.content,'lxml')
  y=input('enter  year :')
  for r in  soup.find_all('td' ,class_="titleColumn"):
     name=r.a.text  
     year=r.span.text[1:5]
     if  y==year:
      print('\tname:',name,'year :',year)


def movi():
  url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'
  page=requests.get(url)
  soup=soupUse(page.content,'lxml')
  li=[em  for em  in  soup.find_all('td', class_="titleColumn")]
  l,c=[],1
  for ele in  li:
    print(c,ele.a.text)
    l.append(ele.a.text)
    c+=1
  c=int(input('e_ter  _   :'))
  movie_name=l[c-1]
  soup2=soupUse(page.content,'lxml')
  li2=[em  for em  in  soup.find_all('td', class_="titleColumn")]
  url2='https://www.imdb.com'
  for ele2  in  li2:
    if  ele2.a.text==movie_name:
      links=soup2.find_all('td',class_="titleColumn")
      url3=url2+links[c-1].a.attrs['href']
  page3=requests.get(url3)
  soup3=soupUse(page3.content,'lxml')
  print(soup3.title.text[0:len(soup3.title.text)-6])
  l=soup3.find('li', class_="ipc-metadata-list__item").text
  print(l[0:8],':',l[8:])

while True:
  print('\n 1) top_250  movies  data\n 2) year_w_movies_list')
  c=input('\nenter_:')
  if  c=='1':
    movi()
  elif  c=='2':
    year_movie()
  else:
    break