from cgi import print_arguments
from os import listdir
import  requests,json
from bs4 import BeautifulSoup as soupUse 

'''url = 'https://www.imdb.com/india/top-rated-indian-movies/'
print('loaging....')
p = requests.get(url)
s = soupUse(p.content,'lxml')
def scrape_top_list():
  li=[em  for em  in  s.find_all('td', class_="titleColumn")]
  
  l,c,ple=[],1,0
  for ele in  li:
    d={}
    d['position']=c
    d['name']=ele.a.text
    d['year']=int(ele.span.text[1:5])
    d['link']='https://www.imdb.com'+ele.find('a').attrs['href']
    l.append(d)
    c+=1

  dl=listdir()
  if  'movieData.json' not  in  dl:
    with  open('movieData.json','w')as  file:
      json.dump(l,file,indent=3)

  li2=[em for em  in  s.find_all('td', class_="ratingColumn imdbRating")]

  with  open('movieData.json')as  f:dic=json.load(f)

  for e in  li2:
    r,d=e.strong.text,{}
    d['ratig']=r
    dic[ple].update(d)
    ple+=1

  with  open('movieData.json','w')as  file:json.dump(dic,file,indent=3)
'''

def group_by_year():
  with  open('movieData.json')as  f:dic=json.load(f)
  li=[movie['year'] for movie in  dic]
  more={}
  for l in  li:
    for m in  dic:
      if  l==m['year']:
        if l not in more:
          more[l]=[m]
        else:
            more[l].append(m)
  print(more)
  for k,v  in  more.items():
    print(k,v)
    print()
  ope=open('dic_data.json','w')
  json.dump(more,ope,indent=2)
group_by_year()