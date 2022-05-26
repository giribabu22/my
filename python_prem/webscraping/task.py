
from asyncore import read
from re import S
from bs4 import  BeautifulSoup  as  soupUse
import requests
url = 'https://www.flipkart.com/nokia-3-4-fjord-blue-64-gb/p/itm73a72497800d0?pid=MOBGY8ZZ5KDN4DG2&lid=LSTMOBGY8ZZ5KDN4DG2J1FSEN&marketplace=FLIPKART&q=nokia+mobiles+smartphones&store=tyy%2F4io&srno=s_1_18&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_na&iid=b8aa78d3-aa29-47c7-9f30-f58391736f55.MOBGY8ZZ5KDN4DG2.SEARCH&ssid=zeaw59bpds0000001653355848254&qH=617a93cf54ff5531'

print('\n\n')

'''url='https://www.flipkart.com/search?q=nokia+mobiles+smartphones&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_na&as-pos=3&as-type=RECENT&suggestionId=nokia+mobiles+smartphones&requestId=17c70c98-c97f-483d-9f46-cdf7e7019214&as-searchtext=noka'

data=requests.get(url)
print(data.status_code)
soup= BeautifulSoup(data.content,'lxml')
for ele in soup.find_all('p'):
  print(ele)
  print()
'''


'''url='https://www.flipkart.com/search?q=nokia+mobiles+smartphones&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_na&as-pos=3&as-type=RECENT&suggestionId=nokia+mobiles+smartphones&requestId=17c70c98-c97f-483d-9f46-cdf7e7019214&as-searchtext=noka'

data=requests.get(url)
soup= BeautifulSoup(data.content,'lxml')
s=[ele  for ele in soup.find_all('p')]
print(len(s))'''


"""# 4. Write a Python program to extract the text in the first paragraph tag of a given html document.

url = 'https://www.flipkart.com/nokia-3-4-fjord-blue-64-gb/p/itm73a72497800d0?pid=MOBGY8ZZ5KDN4DG2&lid=LSTMOBGY8ZZ5KDN4DG2J1FSEN&marketplace=FLIPKART&q=nokia+mobiles+smartphones&store=tyy%2F4io&srno=s_1_18&otracker=AS_Query_OrganicAutoSuggest_3_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_4_na_na_na&iid=b8aa78d3-aa29-47c7-9f30-f58391736f55.MOBGY8ZZ5KDN4DG2.SEARCH&ssid=zeaw59bpds0000001653355848254&qH=617a93cf54ff5531'
dat = requests.get(url)
d= soupUse(dat.content,'lxml')
res=d.find('h1')
print(res.text)
print(len(res.text))"""
'''for ele in  d.find_all('p'):
  print(ele.text)'''

# 6. Write a Python program to find the text of the first <a> tag of a given html text.

# with  open('ew.html') as  page:
#   soup=soupUse(page,'html.parser')
# res=soup.find('a').text
# print(res)
# 7. Write a Python program to find the href of the first <a> tag of a given html document. Go to the editor
# Click me to see the sample solution
"""data=requests.get(url)
soup=soupUse(data.text,'html.parser')
print(soup.find('a').attrs['href'])"""



'''# 8. Write a Python program to extract all the URLs from the webpage python.org that are nested within <li> tags from . Go to the editor
# Click me to see the sample solution
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

urls = []
for h in soup.find_all('li'):
    a = h.find('a')
    urls.append(a.attrs['href'])
print(urls)'''

# 9. Write a Python program to find all the h2 tags and list the first four from the webpage python.org. Go to the editor
# Click me to see the sample solution

"""url = 'https://www.python.org/'
page=requests.get(url)
soup=soupUse(page.text,'lxml')
print(soup.find_all('h2')[0:4])"""

# 10. Write a Python program to find all the link tags and list the first ten from the webpage python.org. Go to the editor
# Click me to see the sample solution
'''url = 'https://www.python.org/'
page=requests.get(url)
soup=soupUse(page.text,'lxml')
print(soup.find_all('link')[0:10])'''

# 11. Write a Python program to a list of all the h1, h2, h3 tags from the webpage python.org. Go to the editor
# Click me to see the sample solution
# url = 'https://www.python.org/'
# page=requests.get(url)
# soup=soupUse(page.text,'lxml')
# for ele in  soup.find_all(['h1','h2','h3']):
#   print(ele.name,' ',ele.text.strip())


# 12. Write a Python program to extract all the text from a given web page. Go to the editor
# Click me to see the sample solution
'''url = 'https://www.python.org/'
page=requests.get(url)
soup=soupUse(page.text,'lxml')
print(soup.get_text())'''
# 13. Write a Python program to print the names of all HTML tags of a given web page going through the document tree. Go to the editor
# Click me to see the sample solution
# url = 'https://www.python.org/'
# page=requests.get(url)
# soup=soupUse(page.text,'lxml')
# for ele in  soup.find_all():
#   print(ele.text)


# 14. Write a Python program to retrieve children of the html tag from a given web page. Go to the editor
# Click me to see the sample solution
'''url = 'https://www.python.org/'
page = requests.get(url)
soup = soupUse(page.text,'lxml')
s=soup.html
li=[c.name for c in s.children if c.name is not None]
print(li)'''



# 15. Write a Python program to retrieve all descendants of the body tag from a given web pimport requests

# from bs4 import BeautifulSoup
# url = 'https://www.python.org/'
# reqs = requests.get(url)
# soup = BeautifulSoup(reqs.text, 'lxml')
# print("\nDescendants of the body tag (https://www.python.org):\n")
# root = soup.html    
# my=[ele.name for ele in root.descendants if ele.name is not None ]
# print(my)
# Click me to see the sample solution


# 16. Write a Python program to retrieve the HTML code of the title, its text, and the HTML code of its parent. Go to the editor
# Click me to see the sample solution
'''url = 'https://www.python.org/'
page=requests.get(url)
soup=soupUse(page.text,'lxml')
print(soup.title.text)'''



# 17. Write a Python program to find and print all li tags of a given web page. Go to the editor
# Click me to see the sample solution

'''url = 'https://www.python.org/'

data=requests.get(url)
page=soupUse(data.text,'lxml')
p=page.html
li=[m.name for m in p.descendants if m.name == 'li']
print(li)'''


# 18. Write a Python program to print content of elements that contain a specified string of a given web page. Go to the editor
# Click me to see the sample solution
url = 'https://www.python.org/'
data=requests.get(url)
page=soupUse(data.content,'lxml')
print(page.title.parent)


# 19. Write a Python program to print the element(s) that has a specified id of a given web page. Go to the editor
# Click me to see the sample solution

# 20. Write a Python program to create a Beautiful Soup parse tree into a nicely formatted Unicode string, with a separate line for each HTML/XML tag and string. Go to the editor
# Click me to see the sample solution

# 21. Write a Python program to find the first tag with a given attribute value in an html document. Go to the editor
# Click me to see the sample solution

# 22. Write a Python program to find tag(s) beneath other tag(s) in a given html document. Go to the editor
# Click me to see the sample solution

# 23. Write a Python program to find tag(s) directly beneath other tag(s) in a given html document. Go to the editor
# Click me to see the sample solution

# 24. Write a Python program to find the siblings of tags in a given html document. Go to the editor
# Click me to see the sample solution

# 25. Write a Python program to find tags by CSS class in a given html document. Go to the editor
# Click me to see the sample solution

# 26. Write a Python program to change the tag's contents and replace with the given string. Go to the editor
# Click me to see the sample solution

# 27. Write a Python program to add to a tag's contents in a given html document. Go to the editor
# Click me to see the sample solution

# 28. Write a Python program to insert a new text within a url in a specified position. Go to the editor
# Click me to see the sample solution

# 29. Write a Python program to insert tags or strings immediately before specified tags or strings. Go to the editor
# Click me to see the sample solution

# 30. Write a Python program to insert tags or strings immediately after specified tags or strings. Go to the editor
# Click me to see the sample solution

# 31. Write a Python program to remove the contents of a tag in a given html document. Go to the editor
# Click me to see the sample solution

# 32. Write a Python program to extract a tag or string from a given tree of html document. Go to the editor
# Click me to see the sample solution

# 33. Write a Python program to remove a tag from a given tree of html document and destroy it and its contents. Go to the editor
# Click me to see the sample solution

# 34. Write a Python program to remove a tag or string from a given tree of html document and replace it with the given tag or string. Go to the editor
# Click me to see the sample solution

# 35. Write a Python program to wrap an element in the specified tag and create the new wrapper. Go to the editor
# Click me to see the sample solution

# 36. Write a Python program to replace a given tag with whatever's inside a given tag. Go to the editor
# Click me to see the sample solution



