"""import  requests,json

data=requests.get('https://api.github.com/users/pratikdeshmukh2004')

with open('data.json','w') as file:json.dump(data.json(),file,indent=3)
print('\n')
c,dic=1,{}
li2=['name','id',"company",'bio','blog','location','email','following_url','followers_url','followers','following','created_at','twitter_username']
for k,v in data.json().items():
  if k in li2:
    dic[k]=v
print(dic)
c,f=input('enter y:'),1
if  c=='y':
  for ele in  li2:
    print(f,ele)
    f+=1
  c=input('enter  followerslistwit  ames y|o')
  if  li2[c-1]  in  li2:
    for k,v in dic.items():
      print(li2)

    """
'''d={[{'prem':[{'jai:43'}],'giri':[{'lastame':9}]}]}
print(d)'''




